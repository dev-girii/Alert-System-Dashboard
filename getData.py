from flask import Flask, render_template
from flask_socketio import SocketIO
import psycopg2
import time
import datetime  # Add at top of file
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
            # ----- CPU -----
            cursor.execute("""
                SELECT * FROM public.cpu 
                WHERE cpu = 'cpu0' 
                ORDER BY time DESC LIMIT 1
            """)
            cpu_row = cursor.fetchone()
            if cpu_row:
                cpu_data = row_to_dict(cursor, cpu_row)
                socketio.emit('cpu_data', cpu_data)

            # ----- DISK -----
            cursor.execute("""
                SELECT * FROM public.disk 
                WHERE device = 'efivarfs' 
                ORDER BY time DESC LIMIT 1
            """)
            disk_row = cursor.fetchone()
            if disk_row:
                disk_data = row_to_dict(cursor, disk_row)
                socketio.emit('disk_data', disk_data)

            # ----- MEMORY -----
            cursor.execute("""
                SELECT * FROM public.mem 
                ORDER BY time DESC LIMIT 1
            """)
            mem_row = cursor.fetchone()
            if mem_row:
                mem_data = row_to_dict(cursor, mem_row)
                socketio.emit('mem_data', mem_data)

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

