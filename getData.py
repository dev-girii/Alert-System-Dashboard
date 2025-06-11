from flask import Flask, render_template
from flask_socketio import SocketIO
import psycopg2
import time
import datetime
import threading
from decimal import Decimal


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow WebSocket

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
@app.route('/')
def index():
    return render_template('index.html')  # Serve HTML from templates folder


def fetch_and_emit_data():
    while True:
        try:
            cpu_data = disk_data = mem_data = {}

            # Fetch latest CPU
            cursor.execute("""
                SELECT * FROM public.cpu 
                WHERE cpu = 'cpu-total' 
                ORDER BY time DESC LIMIT 1
            """)
            row = cursor.fetchone()
            if row:
                cpu_data = row_to_dict(cursor, row)

            # Fetch latest Disk
            cursor.execute("""
                SELECT * FROM public.disk 
                WHERE device = 'efivarfs' 
                ORDER BY time DESC LIMIT 1
            """)
            row = cursor.fetchone()
            if row:
                disk_data = row_to_dict(cursor, row)

            # Fetch latest Mem
            cursor.execute("""
                SELECT * FROM public.mem 
                ORDER BY time DESC LIMIT 1
            """)
            row = cursor.fetchone()
            if row:
                mem_data = row_to_dict(cursor, row)

            # Merge all into one dictionary
            if cpu_data or disk_data or mem_data:
                raw_time = cpu_data.get('time') or disk_data.get('time') or mem_data.get('time')
                if isinstance(raw_time, str):
                    raw_time = datetime.datetime.fromisoformat(raw_time)

                formatted_time = raw_time.strftime("%d/%m/%y - %H:%M:%S") if raw_time else None
                merged = {
                    'time': formatted_time,
                    'host': cpu_data.get('host'),
                    'instance': cpu_data.get('instance'),
                    'role': cpu_data.get('role'),
                    'cpu_idle': cpu_data.get('usage_idle'),
                    'mem_used_percent': mem_data.get('used_percent'),
                    'disk_path': disk_data.get('path'),
                    'disk_used_percent': disk_data.get('used_percent'),
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

