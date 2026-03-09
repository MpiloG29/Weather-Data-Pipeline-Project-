#!/usr/bin/env python3
"""
Weather Data Pipeline - Main Entry Point
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from src.pipeline import WeatherPipeline
    from config.settings import Colors
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure you're in the correct environment and have installed requirements")
    sys.exit(1)

def print_banner():
    """Print colorful banner"""
    banner = f"""
{Colors.HEADER}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🌤️  WEATHER DATA PIPELINE - PORTFOLIO PROJECT            ║
║                                                              ║
║   Extract • Transform • Load • Visualize                    ║
║                                                              ║
║   Built with: Python • SQLite • Docker • Plotly             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.RESET}
    """
    print(banner)

def main():
    """Main function"""
    print_banner()
    
    # Check for command line argument
    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        # Interactive mode
        while True:
            print(f"\n{Colors.BOLD}Options:{Colors.RESET}")
            print(f"{Colors.INFO}1. Run ETL Pipeline (Extract, Transform, Load)")
            print("2. Launch Dashboard")
            print("3. Run Pipeline + Dashboard")
            print("4. Exit")
            
            choice = input(f"\n{Colors.BOLD}Enter your choice (1-4): {Colors.RESET}")
            
            if choice in ['1', '2', '3', '4']:
                break
            print(f"{Colors.ERROR}Invalid choice. Please try again.{Colors.RESET}")
    
    if choice == '1':
        pipeline = WeatherPipeline()
        pipeline.run()
    elif choice == '2':
        try:
            from dashboard.weather_dashboard import WeatherDashboard
            dashboard = WeatherDashboard()
            dashboard.create_dashboard()
        except Exception as e:
            print(f"{Colors.ERROR}❌ Dashboard error: {e}")
    elif choice == '3':
        pipeline = WeatherPipeline()
        pipeline.run()
        try:
            from dashboard.weather_dashboard import WeatherDashboard
            dashboard = WeatherDashboard()
            dashboard.create_dashboard()
        except Exception as e:
            print(f"{Colors.ERROR}❌ Dashboard error: {e}")
    elif choice == '4':
        print(f"{Colors.SUCCESS}👋 Goodbye!{Colors.RESET}")
        sys.exit(0)
    else:
        print(f"{Colors.ERROR}Invalid choice.{Colors.RESET}")

if __name__ == "__main__":
    main()