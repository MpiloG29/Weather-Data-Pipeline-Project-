from flask import Flask, send_file, jsonify, render_template_string
import subprocess
import os
import threading
from datetime import datetime
import time

app = Flask(__name__)

# HTML template for the home page
HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Data Pipeline</title>
    <style>
        body { 
            font-family: 'Segoe UI', Arial, sans-serif; 
            max-width: 1000px; 
            margin: 50px auto; 
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
        }
        .container {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        h1 { font-size: 3em; margin-bottom: 20px; }
        .button { 
            display: inline-block; 
            padding: 15px 30px; 
            margin: 10px; 
            background: white; 
            color: #667eea;
            text-decoration: none; 
            border-radius: 50px;
            font-weight: bold;
            transition: transform 0.3s;
            border: none;
            cursor: pointer;
            font-size: 1.1em;
        }
        .button:hover { transform: scale(1.05); }
        .status { 
            margin: 30px 0; 
            padding: 20px; 
            background: rgba(255,255,255,0.2); 
            border-radius: 10px;
            text-align: left;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .stat-card {
            background: rgba(255,255,255,0.15);
            padding: 20px;
            border-radius: 10px;
        }
        .stat-value { font-size: 2em; font-weight: bold; }
        .stat-label { font-size: 0.9em; opacity: 0.9; }
        pre { 
            background: #1e1e1e; 
            color: #d4d4d4; 
            padding: 15px; 
            border-radius: 5px; 
            overflow-x: auto;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌤️ Weather Data Pipeline</h1>
        <p>Real-time weather data for 8 global cities</p>
        
        <div class="stats" id="stats">
            <div class="stat-card">
                <div class="stat-value" id="city-count">8</div>
                <div class="stat-label">Cities Tracked</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="last-run">-</div>
                <div class="stat-label">Last Run</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="status">⚪</div>
                <div class="stat-label">Status</div>
            </div>
        </div>
        
        <div>
            <button class="button" onclick="runPipeline()">🚀 Run Pipeline Now</button>
            <a href="/dashboard" class="button">📊 View Dashboard</a>
        </div>
        
        <div class="status" id="output">
            <h3>Pipeline Output:</h3>
            <pre id="log">Click run to start the pipeline...</pre>
        </div>
    </div>

    <script>
        function updateStatus() {
            fetch('/status').then(r => r.json()).then(data => {
                document.getElementById('last-run').textContent = data.last_run || 'Never';
                document.getElementById('status').textContent = data.running ? '🟢 Running' : '⚪ Idle';
                if (data.last_output) {
                    document.getElementById('log').textContent = data.last_output;
                }
            });
        }
        
        function runPipeline() {
            document.getElementById('log').textContent = 'Starting pipeline...';
            document.getElementById('status').textContent = '🟡 Starting';
            fetch('/run-pipeline', {method: 'POST'}).then(r => r.json()).then(data => {
                if (data.success) {
                    setTimeout(updateStatus, 2000);
                }
            });
        }
        
        // Update status every 5 seconds
        setInterval(updateStatus, 5000);
        updateStatus();
    </script>
</body>
</html>
"""

# Store pipeline state
pipeline_state = {
    'running': False,
    'last_run': None,
    'last_output': 'No runs yet'
}

@app.route('/')
def home():
    return render_template_string(HOME_HTML)

@app.route('/status')
def status():
    return jsonify({
        'running': pipeline_state['running'],
        'last_run': pipeline_state['last_run'],
        'last_output': pipeline_state['last_output']
    })

@app.route('/run-pipeline', methods=['POST'])
def run_pipeline():
    if pipeline_state['running']:
        return jsonify({'success': False, 'message': 'Pipeline already running'})
    
    def run():
        pipeline_state['running'] = True
        pipeline_state['last_output'] = 'Starting...'
        
        try:
            # Run the pipeline with option 1
            result = subprocess.run(['python', 'run_pipeline.py', '1'], 
                                  capture_output=True, text=True, timeout=300)
            
            output = result.stdout + result.stderr
            pipeline_state['last_output'] = output[-2000:]  # Last 2000 chars
            pipeline_state['last_run'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
        except Exception as e:
            pipeline_state['last_output'] = f'Error: {str(e)}'
        finally:
            pipeline_state['running'] = False
    
    thread = threading.Thread(target=run)
    thread.start()
    
    return jsonify({'success': True, 'message': 'Pipeline started'})

@app.route('/dashboard')
def dashboard():
    # Generate the dashboard
    try:
        subprocess.run(['python', 'run_pipeline.py', '2'], timeout=60)
        return send_file('/tmp/weather_dashboard.html')
    except Exception as e:
        return f"Error generating dashboard: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)