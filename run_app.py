#!/usr/bin/env python3
"""
Launcher script for Digital Twin Cybersecurity Simulation Streamlit App
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Launch the Streamlit app"""
    print("🔒 Digital Twin Cybersecurity Simulation")
    print("=" * 50)
    print("Starting Streamlit application...")
    print()
    
    # Check if streamlit is installed
    try:
        import streamlit
        print(f"✅ Streamlit version {streamlit.__version__} found")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        print("✅ Streamlit installed successfully")
    
    # Get the app.py path
    app_path = Path(__file__).parent / "app.py"
    
    if not app_path.exists():
        print(f"❌ Error: {app_path} not found")
        print("Please ensure app.py exists in the current directory")
        sys.exit(1)
    
    print(f"🚀 Launching app from: {app_path}")
    print()
    print("📱 The app will open in your default browser")
    print("🌐 If it doesn't open automatically, navigate to: http://localhost:8501")
    print()
    print("Press Ctrl+C to stop the application")
    print("=" * 50)
    
    try:
        # Run streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(app_path),
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 