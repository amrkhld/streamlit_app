# Quick Start Guide for Data Cleaning & EDA Tool

## Installation Steps

### 1. Install Python (if not already installed)
- Download from https://www.python.org/
- Ensure Python 3.8+ is installed

### 2. Navigate to Project Directory
```powershell
cd "g:\BIZ\Testing Knowledge\College\DM\streamlit_app"
```

### 3. Create Virtual Environment (Recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 5. Run the App
```powershell
streamlit run app.py
```

The app will automatically open in your default browser at:
```
http://localhost:8501
```

## Using the App

### Step 1: Upload Your Data
1. Look for the "📁 Data Upload" section in the left sidebar
2. Click "Browse files" and select your CSV file
3. Wait for the success message "✅ File loaded successfully!"

### Step 2: Explore Your Dataset
1. Navigate to the "📈 Dataset Overview" tab
2. Review key metrics (rows, columns, missing values, duplicates)
3. Click buttons to preview data
4. Check column names and data types

### Step 3: Analyze Data
1. Go to "🔍 Data Exploration" tab
2. Choose from:
   - Summary Statistics
   - Data Types
   - Missing Values Analysis
   - Duplicates
   - Unique Values

### Step 4: Clean Your Data
1. Open "🧹 Data Cleaning" tab
2. Select a cleaning operation:
   - Convert numeric columns (remove units)
   - View unique values
   - Fill missing values
   - Drop rows with NaN
   - Remove columns
   - Reset to original

### Step 5: Encode Categorical Data
1. Go to "🏷️ Categorical Encoding" tab
2. Choose encoding method:
   - **One-Hot Encoding**: For multi-class categories
   - **Label Encoding**: For ordinal or binary categories
3. Select columns and apply

### Step 6: Download Processed Data
1. Navigate to "📥 Download" tab
2. Choose format:
   - CSV (most common)
   - Excel (.xlsx)
   - JSON
3. Click the download button

## Common Tasks

### Task 1: Basic Data Cleaning
1. Upload CSV
2. Go to "Missing Values" → Note which columns have NaN
3. Go to "🧹 Data Cleaning" → "Replace Missing Values"
4. Select column → Choose "Mean" or "Median" → Apply
5. Download cleaned CSV

### Task 2: Prepare Data for Machine Learning
1. Upload CSV
2. In "Data Cleaning" → "Convert Numeric Columns" (remove units)
3. In "Categorical Encoding" → "One-Hot Encoding" (convert categories)
4. Download processed data

### Task 3: Exploratory Data Analysis
1. Upload CSV
2. Review "Dataset Overview" metrics
3. Explore "Missing Values" and "Unique Values"
4. Analyze "Summary Statistics"
5. Export findings

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Install packages: `pip install -r requirements.txt`

### Issue: "File not found" or upload fails
**Solution**: 
- Ensure CSV file is in UTF-8 encoding
- Check file permissions
- Try a different CSV file

### Issue: App runs slowly with large files
**Solution**:
- Reduce dataset size (sample first 10,000 rows)
- Close other applications
- Use "Drop Columns" to remove unnecessary features

### Issue: Numeric conversion shows errors
**Solution**:
- Check "Show Unique Values" to see data format
- Manually clean values before converting
- Use "Replace Missing Values" with appropriate method

## Data Format Requirements

### CSV File Format
- Comma-separated values (.csv)
- UTF-8 encoding preferred
- First row should contain column headers
- Consistent data types per column

Example:
```
Company,TypeName,Price,Ram,Weight
Dell,Laptop,50000,8,1.8
HP,Desktop,75000,16,4.2
Lenovo,Laptop,45000,4,1.5
```

## Advanced Features

### Custom Value Filling
When filling missing values, you can enter any custom value, not just statistical measures.

### Multi-Column Operations
Select multiple columns for simultaneous encoding or conversion.

### Reset Functionality
Always have the option to reset to your original dataset - no permanent changes!

## Performance Tips

1. **Large Files**: Consider sampling data first
2. **Many Columns**: Use "Drop Columns" to keep only relevant features
3. **Missing Data**: Fill strategically, don't fill everything
4. **Encoding**: One-hot encoding can increase dimensionality significantly

## Export Formats

- **CSV**: Best for Excel and other tools
- **Excel**: Preserves formatting and multiple sheets
- **JSON**: Best for web applications and APIs

## Next Steps

After cleaning and exploring your data:
- Use cleaned CSV for machine learning models
- Share processed data with team members
- Create visualizations using the data
- Build predictive models

## Help & Support

- Check README.md for detailed feature documentation
- Review code comments in app.py
- Test with sample data first before production use

Happy data cleaning! 📊
