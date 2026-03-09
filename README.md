<div align="center">
  
  #  Weather Data Pipeline
  
  [![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
  [![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
  [![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
  [![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)
  [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MpiloG29/Weather-Data-Pipeline-Project-)

  <p align="center">
    <strong>A production-ready ETL pipeline that fetches real-time weather data, transforms it, and delivers beautiful interactive dashboards.</strong>
  </p>

  <p align="center">
    <a href="#-features">Features</a> •
    <a href="#-architecture">Architecture</a> •
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-docker-deployment">Docker</a> •
    <a href="#-dashboard-showcase">Dashboard</a> •
    <a href="#-deployment">Deployment</a> •
    <a href="#-technologies">Technologies</a>
  </p>

  

</div>

---

##  Features

<table>
  <tr>
    <td align="center">🌍</td>
    <td><b>Multi-City Support</b> - Tracks 8 major cities worldwide: New York, London, Tokyo, Sydney, Rio, Cape Town, Mumbai, Dubai</td>
  </tr>
  <tr>
    <td align="center">🔄</td>
    <td><b>Complete ETL Pipeline</b> - Extract, Transform, Load with data quality checks</td>
  </tr>
  <tr>
    <td align="center">🐳</td>
    <td><b>Docker Containerization</b> - Portable, reproducible environment</td>
  </tr>
  <tr>
    <td align="center">📊</td>
    <td><b>Interactive Dashboard</b> - 9 visualizations with Plotly</td>
  </tr>
  <tr>
    <td align="center">🚨</td>
    <td><b>Real-time Alerts</b> - Extreme weather notifications</td>
  </tr>
  <tr>
    <td align="center">🔄</td>
    <td><b>Automated Scheduling</b> - Runs hourly via cron jobs</td>
  </tr>
</table>

##  Architecture
    
   
Data Flow
Extract → Fetches current weather and 7-day forecasts from Open-Meteo API

Transform → Cleans JSON, handles missing values, standardizes formats

Load → Stores processed data in SQLite database

Visualize → Creates interactive Plotly dashboard

Deploy → Runs hourly on Render with persistent storage

 Quick Start
Prerequisites
bash
# Required installations
- Python 3.11+
- Docker (optional)
- Git
Local Installation
bash
# 1. Clone the repository
git clone https://github.com/MpiloG29/Weather-Data-Pipeline-Project-
cd weather-data-pipeline

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the ETL pipeline
python run_pipeline.py 1

# 5. Launch the dashboard
python run_pipeline.py 2
 Docker Deployment
Build and Run Locally
bash
# Build the Docker image
docker build -t weather-pipeline .

# Run the pipeline
docker run -it weather-pipeline python run_pipeline.py 1

# Run with persistent storage
docker run -it -v $(pwd)/data:/app/data weather-pipeline python run_pipeline.py 1
Docker Hub
bash
# Pull the image
docker pull mpilogumede/weather-pipeline

# Run the container
docker run -it mpilogumede/weather-pipeline python run_pipeline.py 1
# Dashboard Showcase
<img width="1537" height="450" alt="newplot (1)" src="https://github.com/user-attachments/assets/4be981c7-cbee-433e-9f0d-261e6e4cbc4d" />
<img width="1505" height="1450" alt="newplot (2)" src="https://github.com/user-attachments/assets/06c13261-7ec7-4e7a-a708-8c851d412a39" />


# Interactive Visualizations
 -Visualization	Description
 
 -Temperature Bar Chart	Compare temperatures across all 8 cities
 
 -Humidity Levels	Real-time humidity percentages
 
 -Wind Speed	Wind speed comparisons
 
 -Global Temperature Map	Geographic visualization with color-coded temperatures
 
 -Weather Conditions	Pie chart of current weather descriptions
 
 -Pressure Levels	Atmospheric pressure by city
 
 -Feels Like vs Actual	Scatter plot correlation
 
 -UV Index	UV levels across cities
 
 -Correlation Heatmap	Temperature, humidity, wind, UV correlations
 
# Alert System

The dashboard automatically detects extreme conditions:

🔥 Heat alerts (temperature ≥ 35°C)

💨 High wind alerts (wind speed ≥ 35 km/h)

🌧️ High humidity alerts (humidity ≥ 90%)

# Deployment
Render (Live Demo)
The pipeline is deployed on Render and runs automatically every hour:

Live URL: https://weather-pipeline.onrender.com

# Environment Variables

Variable	Description	Default

DATABASE_URL	Database connection string	sqlite:///weather_data.db

API_TIMEOUT	API request timeout (seconds)	30

LOG_LEVEL	Logging level	INFO


📁 Project Structure
text
weather-data-pipeline/

├── 📁 src/

│   ├── __init__.py

│   ├── extract.py   # API data extraction

│   ├── transform.py    # Data cleaning and transformation

│   ├── load.py         # Database loading

│   ├── quality.py      # Data quality checks

│   └── pipeline.py     # ETL orchestration

├── 📁 config/

│   └── settings.py     # Configuration and color schemes

├── 📁 dashboard/

│   └── weather_dashboard.py  # Plotly visualizations

├── 📁 notebooks/

│   └── exploration.ipynb     # Jupyter analysis

├── 📄 run_pipeline.py   # Main entry point

├── 📄 requirements.txt  # Python dependencies

├── 📄 Dockerfile        # Docker configuration

├── 📄 docker-compose.yml # Multi-container setup

├── 📄 render.yaml       # Render deployment config

├── 📄 .env.example      # Environment variables template

└── 📄 README.md         # This file

#  Performance

8 cities tracked simultaneously

1,344 hourly forecasts processed per run

56 daily forecasts per run

~15 seconds total execution time

Zero data loss with quality checks

# Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Contact

Celimpilo Gumede

Project Link: https://github.com/MpiloG29/Weather-Data-Pipeline-Project-

