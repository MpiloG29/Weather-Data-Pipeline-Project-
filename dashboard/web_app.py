import os
import sys
import shutil
import threading
import time
from datetime import datetime
from flask import Flask, send_file, jsonify

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pipeline import WeatherPipeline
from dashboard.weather_dashboard import WeatherDashboard

app = Flask(__name__)

DASHBOARD_PATH = '/tmp/weather_dashboard.html'

_status = {
    'last_run': None,
    'state': 'starting',
    'error': None,
}


def _run_pipeline():
    _status['state'] = 'running'
    _status['error'] = None
    try:
        WeatherPipeline().run()
        db = WeatherDashboard()
        path = db.create_dashboard()
        if path and os.path.exists(path):
            shutil.copy(path, DASHBOARD_PATH)
        _status['last_run'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        _status['state'] = 'success'
    except Exception as exc:
        _status['state'] = 'error'
        _status['error'] = str(exc)


def _scheduler():
    """Run pipeline on startup, then every 6 hours."""
    while True:
        _run_pipeline()
        time.sleep(6 * 3600)


# Start background scheduler (single daemon thread; gunicorn --workers 1)
threading.Thread(target=_scheduler, daemon=True).start()


@app.route('/')
def home():
    state = _status['state']
    last_run = _status['last_run'] or 'Not yet'
    error = _status['error'] or ''
    return f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Weather Data Pipeline</title>
  <style>
    body {{font-family:Segoe UI,sans-serif;background:#0f0c29;color:#fff;text-align:center;padding:60px 20px;}}
    h1 {{font-size:2.5rem;margin-bottom:8px;}}
    .badge {{display:inline-block;padding:6px 16px;border-radius:20px;font-weight:700;margin:10px;}}
    .success {{background:#43e97b;color:#000;}}
    .running {{background:#FFD740;color:#000;}}
    .error   {{background:#ff5252;color:#fff;}}
    .starting{{background:#90CAF9;color:#000;}}
    a.btn {{display:inline-block;margin:10px;padding:12px 28px;border-radius:8px;text-decoration:none;font-size:1rem;font-weight:600;}}
    .btn-green {{background:#43e97b;color:#000;}}
    .btn-blue  {{background:#2196F3;color:#fff;}}
  </style>
</head>
<body>
  <h1>🌈 Weather Data Pipeline</h1>
  <p>Pipeline state: <span class="badge {state}">{state}</span></p>
  <p>Last successful run: {last_run}</p>
  {"<p style='color:#ff5252'>"+error+"</p>" if error else ""}
  <br>
  <a class="btn btn-green" href="/dashboard">View Dashboard</a>
  <a class="btn btn-blue"  href="/run">Run Pipeline Now</a>
</body>
</html>'''


@app.route('/status')
def status():
    return jsonify({
        'status': 'ok',
        'pipeline': _status,
        'timestamp': datetime.now().isoformat(),
    })


@app.route('/run')
def run_now():
    if _status['state'] != 'running':
        threading.Thread(target=_run_pipeline, daemon=True).start()
    return '''<h2 style="font-family:sans-serif;text-align:center;margin-top:80px;">
        Pipeline triggered! <a href="/">Go back</a>
    </h2>'''


@app.route('/dashboard')
def dashboard():
    if not os.path.exists(DASHBOARD_PATH):
        return '''<h2 style="font-family:sans-serif;text-align:center;margin-top:80px;">
            Dashboard not ready yet — pipeline is still running.
            <a href="/">Go back</a>
        </h2>'''
    return send_file(DASHBOARD_PATH)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
