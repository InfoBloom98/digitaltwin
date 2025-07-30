#!/usr/bin/env python3
"""
Installation script for Digital Twin Cybersecurity Simulation
Automatically detects Python version and installs compatible dependencies
"""

import sys
import subprocess
import platform
from pathlib import Path

def get_python_version():
    """Get Python version as tuple (major, minor)"""
    return sys.version_info[:2]

def check_python_compatibility():
    """Check if Python version is compatible"""
    version = get_python_version()
    print(f"🐍 Python version: {version[0]}.{version[1]}")
    
    if version < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"   Current version: {version[0]}.{version[1]}")
        return False
    
    if version >= (3, 13):
        print("✅ Python 3.13+ detected - will use compatible requirements")
        return "python313"
    elif version >= (3, 8):
        print("✅ Python version compatible - will use full requirements")
        return "standard"
    
    return False

def install_requirements(requirements_file):
    """Install requirements from specified file"""
    print(f"📦 Installing dependencies from {requirements_file}...")
    
    try:
        # Check if pip is available
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: pip not found. Please install pip first.")
        return False
    
    try:
        # Install requirements
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", requirements_file
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully!")
            return True
        else:
            print("❌ Error installing dependencies:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def install_streamlit():
    """Install Streamlit if not already installed"""
    print("🔍 Checking Streamlit installation...")
    
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} already installed")
        return True
    except ImportError:
        print("📦 Installing Streamlit...")
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", "streamlit>=1.28.0"
            ], check=True)
            print("✅ Streamlit installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing Streamlit: {e}")
            return False

def main():
    """Main installation function"""
    print("🔒 Digital Twin Cybersecurity Simulation")
    print("=" * 50)
    print("🚀 Starting installation...")
    print()
    
    # Check Python compatibility
    compatibility = check_python_compatibility()
    if not compatibility:
        sys.exit(1)
    
    print()
    
    # Determine requirements file
    if compatibility == "python313":
        requirements_file = "requirements-python313.txt"
        print("📋 Using Python 3.13+ compatible requirements")
        print("   Note: TensorFlow/PyTorch replaced with compatible alternatives")
    else:
        requirements_file = "requirements.txt"
        print("📋 Using standard requirements (includes TensorFlow/PyTorch)")
    
    print()
    
    # Check if requirements file exists
    if not Path(requirements_file).exists():
        print(f"❌ Error: {requirements_file} not found")
        print("   Please ensure you're running this script from the project directory")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements(requirements_file):
        print("\n💡 Troubleshooting tips:")
        print("   1. Try updating pip: python -m pip install --upgrade pip")
        print("   2. Use virtual environment: python -m venv venv")
        print("   3. Check your internet connection")
        sys.exit(1)
    
    print()
    
    # Install Streamlit
    if not install_streamlit():
        print("⚠️  Warning: Streamlit installation failed")
        print("   You can try installing it manually: pip install streamlit")
    
    print()
    print("🎉 Installation completed successfully!")
    print()
    print("🚀 To run the simulation:")
    print("   streamlit run app.py")
    print()
    print("📚 For more information, see README.md")
    print("=" * 50)

if __name__ == "__main__":
    main() 