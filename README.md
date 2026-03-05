# 🌤️ Weather Data Pipeline 

## 🎯 Project Overview

A production-ready ETL pipeline that fetches weather data from Open-Meteo API, transforms it, and loads it into PostgreSQL running on Docker. Includes an interactive dashboard for data visualization.
<img width="1497" height="1400" alt="newplot" src="https://github.com/user-attachments/assets/7995e7ac-86ff-4270-a8df-c26600aa5e48" />

### ✨ Features

- **Real-time Weather Data**: Fetches current conditions and 7-day forecasts
- **Multi-city Support**: Tracks 8 major cities worldwide
- **Docker Containerization**: Clean, reproducible environment
- **Interactive Dashboard**: Built with Plotly for data visualization
- **Error Handling**: Robust error handling and logging
- **Colorful CLI**: User-friendly command-line interface

## 🏗️ Architecture
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Open- │────▶│ Python │────▶│ PostgreSQL │────▶│ Dashboard │
│ Meteo API │ │ ETL │ │ (Docker) │ │ (Plotly) │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/MpiloG29/Weather-Data-Pipeline-Project-
cd weather-data-pipeline

🌟 WEATHER DATA PIPELINE - ETL PROCESS 🌟

📤 STEP 1: EXTRACTION
🌍 Fetching weather for New York... ✅
🌍 Fetching weather for London... ✅
🌍 Fetching weather for Tokyo... ✅

📊 Current Weather Summary:
┌─────────────┬──────────────┬──────────┬─────────────┐
│ City        │ Temperature  │ Humidity │ Description │
├─────────────┼──────────────┼──────────┼─────────────┤
│ New York    │ 22.5°C       │ 65%      │ Partly cloudy│
│ London      │ 18.2°C       │ 78%      │ Light rain  │
│ Tokyo       │ 26.8°C       │ 70%      │ Clear sky   │
└─────────────┴──────────────┴──────────┴─────────────┘

weather-data-pipeline/
├── 📁 src/               # ETL pipeline source code
├── 📁 config/            # Configuration files
├── 📁 dashboard/         # Dashboard visualization
├── 📁 notebooks/         # Jupyter notebooks for exploration
├── 📄 docker-compose.yml # Docker configuration
├── 📄 requirements.txt   # Python dependencies
├── 📄 run_pipeline.py    # Main entry point
└── 📄 README.md          # This file

🔧 Technologies Used
Python 3.9+: Core programming language

PostgreSQL 15: Data storage

Docker: Containerization

Open-Meteo API: Free weather data source

Pandas: Data transformation

Plotly: Interactive visualizations

SQLAlchemy: Database ORM

Colorama: Colored CLI output

🎨 Dashboard Preview
The dashboard includes:

🌡️ Current temperature map

📊 Humidity and wind speed charts

📅 7-day forecasts for each city

📈 Interactive visualizations

🚢 Deployment Options
Local Development: Run with Docker Compose

Cloud Deployment: Deploy to AWS/GCP/Azure

Scheduled Pipeline: Set up cron jobs for automated runs

Kubernetes: Container orchestration for scaling

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
Celimpilo Gumede - https://www.linkedin.com/in/celimpilo-gumede-b5540522b/ - celimpilog200@gmail.com

Project Link: https://github.com/MpiloG29/weather-data-pipeline
