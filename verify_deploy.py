import os
import sys

def check_structure():
    required_files = [
        'run_pipeline.py',
        'requirements.txt',
        'Dockerfile',
        'docker-compose.yml',
        'config/settings.py',
        'src/pipeline.py',
        'src/extract.py',
        'src/transform.py',
        'src/load.py',
        'src/quality.py',
        'dashboard/weather_dashboard.py'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print("❌ Missing files:")
        for f in missing:
            print(f"  - {f}")
        return False
    else:
        print("✅ All required files present!")
        return True

def check_docker():
    try:
        import subprocess
        result = subprocess.run(['docker', 'build', '-t', 'test', '.'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Docker build successful!")
            return True
        else:
            print("❌ Docker build failed:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Docker check failed: {e}")
        return False

if __name__ == '__main__':
    print("🔍 Verifying project structure...")
    if check_structure():
        print("\n🐳 Testing Docker build...")
        check_docker()
    else:
        print("\n❌ Please fix missing files before deploying")
