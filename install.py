#!/usr/bin/env python3
"""
Installation script for Digital Twin Cybersecurity Simulation
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def check_pip():
    """Check if pip is available"""
    try:
        import pip
        print("✅ pip is available")
        return True
    except ImportError:
        print("❌ pip is not available")
        return False

def install_package(package):
    """Install a single package"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def install_requirements(requirements_file):
    """Install requirements from file"""
    print(f"\n📦 Installing dependencies from {requirements_file}...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print(f"✅ Successfully installed dependencies from {requirements_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies from {requirements_file}")
        print(f"   Error: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        "logs",
        "data/input",
        "data/output", 
        "data/backup",
        "models",
        "config"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ Created necessary directories")

def main():
    """Main installation function"""
    print("🔒 Digital Twin Cybersecurity Simulation - Installation")
    print("=" * 60)
    
    # Check prerequisites
    if not check_python_version():
        sys.exit(1)
    
    if not check_pip():
        print("Please install pip first")
        sys.exit(1)
    
    # Update pip
    print("\n🔄 Updating pip...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("✅ pip updated successfully")
    except subprocess.CalledProcessError:
        print("⚠️  Failed to update pip, continuing anyway...")
    
    # Try full installation first
    print("\n🚀 Attempting full installation...")
    if install_requirements("requirements.txt"):
        print("\n🎉 Full installation completed successfully!")
    else:
        print("\n⚠️  Full installation failed, trying minimal installation...")
        
        if install_requirements("requirements-minimal.txt"):
            print("\n✅ Minimal installation completed successfully!")
            print("   Note: Some advanced ML features may not be available")
        else:
            print("\n❌ Both installations failed")
            print("\n🔧 Manual installation steps:")
            print("1. Try installing core packages individually:")
            print("   pip install numpy pandas scikit-learn flask")
            print("2. Check your Python version and pip installation")
            print("3. Consider using a virtual environment")
            sys.exit(1)
    
    # Create directories
    print("\n📁 Setting up directories...")
    create_directories()
    
    # Test basic functionality
    print("\n🧪 Testing basic functionality...")
    try:
        import numpy
        import pandas
        import flask
        import sklearn
        print("✅ Core packages imported successfully")
    except ImportError as e:
        print(f"⚠️  Warning: Some packages may not be properly installed: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 Installation completed!")
    print("\n📋 Next steps:")
    print("1. Run the demo: python demo.py")
    print("2. Start the simulation: python src/main.py")
    print("3. Access the dashboard: http://localhost:5000")
    print("\n📚 For more information, see the README.md file")

if __name__ == "__main__":
    main() 