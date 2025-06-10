from flask import Flask, render_template
from flask_socketio import SocketIO
import psycopg2
import time
import threading

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

@app.route('/')
def index():
    return render_template('index.html')  # Serve HTML from templates folder

def fetch_and_emit_data():
    while True:
        try:
            cursor.execute(
                "SELECT * FROM public.cpu WHERE cpu = 'cpu-total' ORDER BY time DESC LIMIT 1"
            )
            row = cursor.fetchone()
            if row:
                # Assuming usage_idle is at column index 4 (adjust if needed)
                usage_idle = float(row[5])
                cpu_utilized = 100 - usage_idle
                socketio.emit('cpu_data', {
                    'time': str(row[0]),
                    'usage': f"{cpu_utilized:.2f}%"
                })
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

