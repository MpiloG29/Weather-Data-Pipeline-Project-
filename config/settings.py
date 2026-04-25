import os
from dotenv import load_dotenv
from colorama import Fore, Style, init

init(autoreset=True)
load_dotenv()

class Colors:
    HEADER = Fore.MAGENTA + Style.BRIGHT
    INFO = Fore.CYAN
    SUCCESS = Fore.GREEN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT

# --- SQLite Configuration ---
DB_PATH = os.path.abspath('weather_data.db')
# Use DATABASE_URL env var if set (e.g. on Render), otherwise fall back to local file
DATABASE_URL = os.environ.get('DATABASE_URL', f"sqlite:///{DB_PATH}")

# Keep DB_CONFIG for any legacy code
DB_CONFIG = {
    'database': DB_PATH
}

# --- API Configuration ---
OPEN_METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"

CITIES = [
    {"name": "New York", "country": "USA", "lat": 40.7128, "lon": -74.0060},
    {"name": "London", "country": "UK", "lat": 51.5074, "lon": -0.1278},
    {"name": "Tokyo", "country": "Japan", "lat": 35.6762, "lon": 139.6503},
    {"name": "Sydney", "country": "Australia", "lat": -33.8688, "lon": 151.2093},
    {"name": "Rio de Janeiro", "country": "Brazil", "lat": -22.9068, "lon": -43.1729},
    {"name": "Cape Town", "country": "South Africa", "lat": -33.9249, "lon": 18.4241},
    {"name": "Mumbai", "country": "India", "lat": 19.0760, "lon": 72.8777},
    {"name": "Dubai", "country": "UAE", "lat": 25.2048, "lon": 55.2708},
]

WEATHER_PARAMS = {
    "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", 
                "precipitation", "weather_code", "wind_speed_10m", "wind_direction_10m",
                "pressure_msl", "uv_index", "visibility"],
    "hourly": ["temperature_2m", "relative_humidity_2m", "apparent_temperature",
               "precipitation_probability", "precipitation", "weather_code",
               "wind_speed_10m", "wind_direction_10m"],
    "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min",
              "sunrise", "sunset", "precipitation_sum", 
              "precipitation_probability_max", "wind_speed_10m_max"],
    "timezone": "auto",
    "forecast_days": 7
}