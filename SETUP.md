# 🚀 Complete Setup & Installation Guide

## System Requirements

- **Operating System**: Windows 7+ (any version)
- **Python**: 3.8 or higher
- **Disk Space**: ~500 MB (for dependencies)
- **RAM**: 2 GB minimum (4 GB recommended)
- **Internet**: Required for pip package installation

## Installation Methods

### Method 1: Automated Setup (Recommended)

#### Using PowerShell (Windows 10/11)

1. **Open PowerShell as Administrator**
   - Press `Win + X` and select "Windows PowerShell (Admin)"
   - Or right-click Start Menu → Windows PowerShell (Admin)

2. **Navigate to project directory**
   ```powershell
   cd "g:\BIZ\Testing Knowledge\College\DM\streamlit_app"
   ```

3. **Run the setup script**
   ```powershell
   .\run_app.ps1
   ```

4. **What happens**
   - ✅ Checks Python installation
   - ✅ Creates virtual environment
   - ✅ Installs all dependencies
   - ✅ Launches Streamlit app
   - ✅ Opens browser automatically

#### Using Command Prompt (All Windows Versions)

1. **Open Command Prompt**
   - Press `Win + R` → Type `cmd` → Press Enter

2. **Navigate to project directory**
   ```cmd
   cd "g:\BIZ\Testing Knowledge\College\DM\streamlit_app"
   ```

3. **Run the batch script**
   ```cmd
   run_app.bat
   ```

---

### Method 2: Manual Setup (Step-by-Step)

#### Step 1: Navigate to Project Directory

```powershell
cd "g:\BIZ\Testing Knowledge\College\DM\streamlit_app"
```

#### Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

**Why virtual environment?**
- Isolates project dependencies
- Prevents conflicts with other projects
- Easy to manage versions
- Professional practice

#### Step 3: Activate Virtual Environment

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

**Expected output**: You should see `(venv)` at the start of your prompt:
```
(venv) C:\path\to\streamlit_app>
```

#### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

**What gets installed:**
- streamlit (web framework)
- pandas (data manipulation)
- numpy (numerical computing)
- matplotlib (plotting)
- seaborn (statistical visualization)
- scikit-learn (machine learning)
- openpyxl (Excel support)

**Expected time**: 2-5 minutes depending on internet speed

#### Step 5: Run the Application

```powershell
streamlit run app.py
```

**Expected output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501

  For better stability, install Python 3.10 or higher.
```

**Browser opens automatically** at `http://localhost:8501`

---

## Python Installation (If Not Already Installed)

### Download Python

1. Go to https://www.python.org/downloads/
2. Click the yellow "Download Python 3.x.x" button
3. Version 3.10+ is recommended (3.8+ minimum)

### Install Python

1. Run the installer
2. **IMPORTANT**: Check "Add Python to PATH" ✅
3. Click "Install Now"
4. Wait for installation to complete

### Verify Installation

Open Command Prompt and type:
```cmd
python --version
```

Should output: `Python 3.x.x` (version number)

---

## Usage After Installation

### Starting the App

**First Time (with all setup):**
```powershell
.\run_app.ps1
```

**Subsequent Times (just run the app):**
```powershell
.\venv\Scripts\Activate.ps1
streamlit run app.py
```

### Stopping the App

- Press `Ctrl + C` in the terminal window
- The browser tab will remain but won't respond
- Close browser tab normally

### Restarting the App

```powershell
streamlit run app.py
```

No need to create virtual environment again - it persists!

---

## File Structure After Installation

```
streamlit_app/
├── venv/                           # Virtual environment (created during setup)
│   ├── Scripts/
│   ├── Lib/
│   └── ...
├── app.py                          # Main application
├── requirements.txt                # Dependencies list
├── run_app.ps1                     # PowerShell launcher
├── run_app.bat                     # Batch launcher
├── generate_sample_data.py         # Sample data generator
├── README.md                       # Full documentation
├── QUICKSTART.md                   # Quick start
├── EXAMPLES.md                     # Usage examples
├── PROJECT_SUMMARY.md              # Project overview
└── .streamlit_config.toml         # Configuration
```

---

## Troubleshooting

### Issue 1: "Python is not recognized"

**Problem**: Command Prompt doesn't recognize Python command

**Solution**:
1. Reinstall Python
2. **During installation**: Check "Add Python to PATH" ✅
3. Restart Command Prompt
4. Try again

**Test**: `python --version`

---

### Issue 2: "ModuleNotFoundError: No module named 'streamlit'"

**Problem**: Dependencies not installed

**Solution**:
1. Ensure virtual environment is active (see `(venv)` prefix)
2. Run: `pip install -r requirements.txt`
3. Wait for completion
4. Run app: `streamlit run app.py`

---

### Issue 3: "Permission denied" when running .ps1

**Problem**: PowerShell execution policy

**Solution** (PowerShell as Admin):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try again:
```powershell
.\run_app.ps1
```

---

### Issue 4: Port 8501 already in use

**Problem**: Another process using the same port

**Solution - Option 1** (Stop other process):
```powershell
streamlit run app.py --logger.level=debug
```

**Solution - Option 2** (Use different port):
```powershell
streamlit run app.py --server.port 8502
```

---

### Issue 5: App runs very slowly

**Problem**: Low system resources

**Solutions**:
- Close other applications
- Use a smaller CSV file for testing
- Try dropping some columns
- Increase available RAM

---

### Issue 6: CSV upload fails

**Problem**: File format or encoding issue

**Solutions**:
- Ensure file is .csv format (not .xlsx)
- Check encoding is UTF-8
- Verify file is not corrupted
- Try with sample_laptop_data.csv first

---

## Performance Optimization

### For Better Performance:

1. **Close unnecessary programs** (browser tabs, etc.)
2. **Use fewer columns** (drop unused ones)
3. **Sample large datasets** (first 10,000 rows)
4. **Restart the app** occasionally (clear cache)
5. **Upgrade RAM** if system has < 4 GB

### Recommended Specs:

| Task | Minimum | Recommended |
|------|---------|------------|
| Dataset size | < 10,000 rows | < 100,000 rows |
| RAM | 2 GB | 4 GB |
| CPU | Dual-core | Quad-core |
| Storage | 500 MB | 2 GB |

---

## Virtual Environment Management

### Deactivate Virtual Environment

```powershell
deactivate
```

### Delete Virtual Environment (to start fresh)

```powershell
Remove-Item -Recurse venv
```

Then recreate:
```powershell
python -m venv venv
```

### Using Different Python Version

If you have multiple Python versions:
```powershell
py -3.10 -m venv venv
```

---

## Updating Dependencies

If you want to upgrade packages:

```powershell
.\venv\Scripts\Activate.ps1
pip install --upgrade -r requirements.txt
```

### Generate Updated Requirements

```powershell
pip freeze > requirements.txt
```

---

## Sample Data Generation

Test the app with sample laptop data:

```powershell
.\venv\Scripts\Activate.ps1
python generate_sample_data.py
```

This creates `sample_laptop_data.csv` ready to upload!

---

## IDE Setup (Optional)

### Using VS Code

1. Install VS Code from https://code.visualstudio.com/
2. Install Python extension
3. Open project folder
4. Streamlit extension available too

### Using PyCharm

1. Install PyCharm from https://www.jetbrains.com/pycharm/
2. Open project folder
3. Configure venv interpreter
4. Run with Alt+Shift+F10

---

## Security Notes

- 🔒 Never share your virtual environment with credentials
- 🔒 Keep Python and packages updated
- 🔒 Don't upload sensitive data files to public repositories
- 🔒 Use .gitignore to exclude venv/ and data files

---

## Additional Resources

- **Streamlit Docs**: https://docs.streamlit.io/
- **Pandas Docs**: https://pandas.pydata.org/docs/
- **Python Docs**: https://docs.python.org/3/
- **Stack Overflow**: https://stackoverflow.com/

---

## Getting Help

1. **Check QUICKSTART.md** for fast setup
2. **Read README.md** for features
3. **Review EXAMPLES.md** for usage
4. **Check troubleshooting** above
5. **Search error message** online

---

## Quick Reference Card

### Essential Commands

```powershell
# Activate environment
.\venv\Scripts\Activate.ps1

# Deactivate environment
deactivate

# Install packages
pip install -r requirements.txt

# Run application
streamlit run app.py

# Generate sample data
python generate_sample_data.py

# Run with custom port
streamlit run app.py --server.port 8502

# Clear cache
streamlit cache clear
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl + C | Stop Streamlit server |
| r | Rerun app |
| c | Clear cache |
| F5 | Browser refresh |

---

## Uninstallation

To completely remove the project:

```powershell
cd ..
Remove-Item -Recurse streamlit_app
```

Or keep the folder and just delete virtual environment:

```powershell
Remove-Item -Recurse venv
```

---

## Success Checklist

- ✅ Python installed (3.8+)
- ✅ Project folder accessible
- ✅ Virtual environment created
- ✅ Dependencies installed
- ✅ App runs without errors
- ✅ Browser opens at localhost:8501
- ✅ Can upload CSV files
- ✅ All tabs working properly

---

## Next Steps

1. ✅ Install and run the app
2. 📊 Generate sample data: `python generate_sample_data.py`
3. 📁 Upload sample CSV
4. 🔍 Explore all tabs and features
5. 📚 Read EXAMPLES.md for use cases
6. 💾 Start cleaning your real data!

---

## Support

Need help? Check these files in order:
1. **PROJECT_SUMMARY.md** - Overview
2. **QUICKSTART.md** - Fast setup
3. **README.md** - Full documentation
4. **EXAMPLES.md** - Real scenarios

Happy data cleaning! 🎉

---

**Last Updated**: December 2, 2025  
**Tested On**: Windows 10/11, Python 3.9+, Streamlit 1.28.1
