@echo off
REM Streamlit App Launcher for Windows
REM This script sets up and runs the Data Cleaning & EDA Tool

title Data Cleaning & EDA Tool - Streamlit App
echo.
echo =========================================
echo Data Cleaning & EDA Tool - Streamlit App
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Checking Python installation...
python --version
echo.

REM Check if venv exists
if not exist "venv" (
    echo [2/4] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
) else (
    echo [2/4] Virtual environment already exists!
)
echo.

REM Activate virtual environment
echo [3/4] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment!
    pause
    exit /b 1
)
echo Virtual environment activated!
echo.

REM Install requirements
echo [4/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)
echo Dependencies installed!
echo.

echo =========================================
echo Starting Streamlit App...
echo =========================================
echo.
echo The app will open in your browser at:
echo http://localhost:8501
echo.
echo Press Ctrl+C in this window to stop the app.
echo.

REM Run Streamlit app
streamlit run app.py
pause
