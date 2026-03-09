from flask import Flask, send_file, jsonify
import subprocess
import threading
import schedule
import time
import os
from datetime import datetime

app = Flask(__name__)

# Run pipeline every hour in background
def run_pipeline_job():
    subprocess.run(['python', 'run_pipeline.py', '1'])

def schedule_runner():
    schedule.every().hour.do(run_pipeline_job)
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start scheduler in background thread
threading.Thread(target=schedule_runner, daemon=True).start()

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather Pipeline</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 50px; }
            .button { padding: 10px 20px; background: #4CAF50; color: white; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>🌤️ Weather Data Pipeline</h1>
        <p>Running hourly automatically</p>
        <a href="/dashboard" class="button">View Dashboard</a>
    </body>
    </html>
    '''

@app.route('/dashboard')
def dashboard():
    subprocess.run(['python', 'run_pipeline.py', '2'])
    return send_file('/tmp/weather_dashboard.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)