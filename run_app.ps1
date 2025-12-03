# Streamlit App Launcher for Windows PowerShell
# Data Cleaning & EDA Tool

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Data Cleaning & EDA Tool - Streamlit App" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "[1/4] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python version: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Python is not installed or not in PATH!" -ForegroundColor Red
    Write-Host "Please install Python 3.8+ from https://www.python.org/" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Check if venv exists
Write-Host "[2/4] Checking virtual environment..." -ForegroundColor Yellow
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ ERROR: Failed to create virtual environment!" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "✓ Virtual environment created successfully!" -ForegroundColor Green
} else {
    Write-Host "✓ Virtual environment already exists!" -ForegroundColor Green
}
Write-Host ""

# Activate virtual environment
Write-Host "[3/4] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ ERROR: Failed to activate virtual environment!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✓ Virtual environment activated!" -ForegroundColor Green
Write-Host ""

# Install requirements
Write-Host "[4/4] Installing dependencies from requirements.txt..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ ERROR: Failed to install dependencies!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✓ Dependencies installed!" -ForegroundColor Green
Write-Host ""

# Launch app
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Starting Streamlit App..." -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "The app will open in your browser at:" -ForegroundColor Cyan
Write-Host "http://localhost:8501" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C in this window to stop the app." -ForegroundColor Yellow
Write-Host ""

streamlit run app.py
