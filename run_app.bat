@echo off
echo 🔒 Digital Twin Cybersecurity Simulation
echo ================================================
echo Starting Streamlit application...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

REM Check if streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo ❌ Streamlit not found. Installing...
    python -m pip install streamlit
    if errorlevel 1 (
        echo ❌ Failed to install Streamlit. Please install manually: pip install streamlit
        pause
        exit /b 1
    )
    echo ✅ Streamlit installed successfully
)

echo 🚀 Launching Streamlit app...
echo.
echo 📱 The app will open in your default browser
echo 🌐 If it doesn't open automatically, navigate to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo ================================================

REM Run streamlit
python -m streamlit run app.py --server.port 8501 --server.address localhost

echo.
echo 👋 Application stopped
pause 