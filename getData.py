from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import psycopg2
import time
import datetime
import threading
from decimal import Decimal
from flask_cors import CORS
import pytz 

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow WebSocket
CORS(app)
# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="metrics",
    user="postgres",
    password="dharan06#",
    port=5432
) 
cursor = conn.cursor()
def row_to_dict(cursor, row):
    result = {}
    for index, col in enumerate(cursor.description):
        value = row[index]
        # Convert datetime to ISO string
        if isinstance(value, (datetime.datetime, datetime.date)):
            value = value.isoformat()
        # Convert Decimal to float
        elif isinstance(value, Decimal):
            value = float(value)
        result[col.name] = value
    return result
@app.route('/api/history/<instance>')
def get_instance_history(instance):
    try:
        result = {}

        # Get all distinct roles under this instance
        cursor.execute("""
            SELECT DISTINCT role FROM public.cpu
            WHERE instance = %s
        """, (instance,))
        roles = [row[0] for row in cursor.fetchall()]

        for role in roles:
            # Fetch CPU data
            cursor.execute("""
                           SELECT * FROM (
    SELECT time, usage_idle
    FROM public.cpu
    WHERE instance = %s AND role = %s AND cpu = 'cpu-total'
    ORDER BY time DESC
    LIMIT 5
) AS sub
ORDER BY time ASC;
            """, (instance, role))
            cpu_rows = cursor.fetchall()

            # Fetch MEM data
            cursor.execute("""
                           SELECT * FROM (
                SELECT time, used_percent FROM public.mem
                WHERE instance = %s AND role = %s
                ORDER BY time DESC LIMIT 5
) AS sub
ORDER BY time ASC;
            """, (instance, role))
            mem_rows = cursor.fetchall()
            # Prepare structured output
            result[role] = {
                "cpu": [
                    {
                        "time": pytz.utc.localize(row[0]).astimezone(pytz.timezone('Asia/Kolkata')).isoformat(),
                        "cpu_idle": float(row[1])
                    } for row in cpu_rows
                ],
                "mem": [
                    {
                        "time": pytz.utc.localize(row[0]).astimezone(pytz.timezone('Asia/Kolkata')).isoformat(),
                        "mem_used_percent": float(row[1])
                    } for row in mem_rows
                ]
            }

        return jsonify(result)

    except Exception as e:
        print("Error fetching history:", e)
        return jsonify({"error": "Internal server error"}), 500

@app.route('/')
def index():
    return render_template('index.html')  # Serve HTML from templates folder


def fetch_and_emit_data():
    while True:
        try:
            # Step 1: Get all unique (instance, role) pairs
            cursor.execute("""
                SELECT DISTINCT instance, role FROM public.cpu
            """)
            instance_role_pairs = cursor.fetchall()

            for instance, role in instance_role_pairs:
                cpu_data = disk_data = mem_data = {}

                # CPU data
                cursor.execute("""
                    SELECT * FROM public.cpu
                    WHERE cpu = 'cpu-total' AND instance = %s AND role = %s
                    ORDER BY time DESC LIMIT 1
                """, (instance, role))
                row = cursor.fetchone()
                if row:
                    cpu_data = row_to_dict(cursor, row)

                # Disk data
                cursor.execute("""
                    SELECT DISTINCT ON (device) * 
                    FROM public.disk
                    WHERE instance = %s AND role = %s
                    ORDER BY device, time DESC
                """, (instance, role))
                rows = cursor.fetchall()
                disk_data = [row_to_dict(cursor, row) for row in rows]

                # Mem data
                cursor.execute("""
                    SELECT * FROM public.mem
                    WHERE instance = %s AND role = %s
                    ORDER BY time DESC LIMIT 1
                """, (instance, role))
                row = cursor.fetchone()
                if row:
                    mem_data = row_to_dict(cursor, row)
                net_data = {}  # Add this line before executing the query

                # NET data — adjust based on interface and null role handling
                if role is None or role == '':
                    cursor.execute("""
                        SELECT * FROM public.net
                        WHERE interface = 'WiFi' AND instance = %s AND role IS NULL
                        ORDER BY time DESC LIMIT 1
                    """, (instance,))
                else:
                    cursor.execute("""
                        SELECT * FROM public.net
                        WHERE interface = 'WiFi' AND instance = %s AND role = %s
                        ORDER BY time DESC LIMIT 1
                    """, (instance, role))

                row = cursor.fetchone()
                net_data = row_to_dict(cursor, row) if row else {}

                # Merge and emit
                if cpu_data or disk_data or mem_data:
                    raw_time = (
                        cpu_data.get('time') or
                        disk_data.get('time') or
                        mem_data.get('time')
                    )

                    if isinstance(raw_time, str):
                        raw_time = datetime.datetime.fromisoformat(raw_time)
                    # Convert to IST using pytz
                    if raw_time.tzinfo is None:
                        raw_time = pytz.utc.localize(raw_time)
                    ist = pytz.timezone('Asia/Kolkata')
                    raw_time = raw_time.astimezone(ist)

                    formatted_time = raw_time.strftime("%d/%m/%y - %H:%M:%S") if raw_time else None
                    # formatted_time = raw_time.strftime("%d/%m/%y - %H:%M:%S") if raw_time else None

                    merged = {
                        'time': formatted_time,
                        'host': cpu_data.get('host') or mem_data.get('host') or disk_data.get('host'),
                        'ip': cpu_data.get('ip'),
                        'instance': instance,
                        'role': role,
                        'cpu_idle': cpu_data.get('usage_idle'),
                        'mem_used_percent': mem_data.get('used_percent'),
                        'disks': [
                            {
                                'device': d.get('device'),
                                'path': d.get('path'),
                                'used_percent': d.get('used_percent')
                            } for d in disk_data
                        ],
                        'net_interface': net_data.get('interface'),
                        'net_bytes_recv': net_data.get('bytes_recv'),
                        'net_bytes_sent': net_data.get('bytes_sent'),
                    }

                    socketio.emit('system_metrics', merged)
                    # print(merged)

        except Exception as e:
            print("Database error:", e)

        time.sleep(2)



@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    print("Starting Flask server...")
    threading.Thread(target=fetch_and_emit_data, daemon=True).start()
    socketio.run(app, host='0.0.0.0', port=3000, debug=True)

