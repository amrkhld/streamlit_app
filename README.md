# 📊 Data Cleaning & EDA Tool

A comprehensive Streamlit application for data cleaning, exploration, and analysis with categorical encoding capabilities.

## Features

### 1. **📈 Dataset Overview**
- Display dataset dimensions (rows × columns)
- Show missing values and duplicates count
- Preview first/last N rows
- Display all rows
- View column names and data types
- Show dataset shape

### 2. **🔍 Data Exploration**
- **Summary Statistics**: Descriptive statistics for all columns
- **Data Types**: Column information with data types
- **Missing Values**: Identify and visualize missing data
- **Duplicates**: Find and display duplicate rows
- **Unique Values**: Analyze unique values per column with visualization

### 3. **🧹 Data Cleaning**
- **Convert Numeric Columns**: Remove units and convert to numeric format
- **Show Unique Values**: Explore categorical variables
- **Replace Missing Values**: Fill NaN with Mean, Median, Mode, Forward Fill, Backward Fill, or Custom Value
- **Drop Rows with NaN**: Remove rows with missing data
- **Drop Columns**: Remove unnecessary columns
- **Reset to Original**: Restore the original dataset

### 4. **🏷️ Categorical Encoding**
- **One-Hot Encoding**: Convert categorical variables to binary columns
- **Label Encoding**: Convert categorical variables to numeric labels

### 5. **📥 Download**
- Export processed data as CSV
- Export processed data as Excel (.xlsx)
- Export processed data as JSON

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Setup

1. Clone or navigate to the project directory:
```bash
cd streamlit_app
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Workflow

1. **Upload Data**: Use the sidebar to upload a CSV file
2. **Explore**: Navigate to "Dataset Overview" tab to understand your data
3. **Analyze**: Use "Data Exploration" tab for detailed analysis
4. **Clean**: Apply cleaning operations in "Data Cleaning" tab
5. **Encode**: Transform categorical variables in "Categorical Encoding" tab
6. **Download**: Export your processed data in your preferred format

## Supported File Formats

- CSV files (.csv)

## Data Cleaning Operations

### Convert Numeric Columns
- Removes common units (GB, kg, GHz, $)
- Converts to numeric type with error handling

### Replace Missing Values
- **Mean**: For numeric columns
- **Median**: For numeric columns
- **Mode**: For any column
- **Forward Fill**: For time-series data
- **Backward Fill**: For time-series data
- **Custom Value**: User-specified value

### Drop Operations
- Drop rows with any NaN
- Drop rows with all NaN
- Drop rows with custom threshold
- Drop selected columns

## Encoding Methods

### One-Hot Encoding
- Creates binary columns for each categorical value
- Suitable for machine learning algorithms
- Removes original column

### Label Encoding
- Assigns numeric labels (0, 1, 2, ...) to categories
- Preserves data structure
- More compact than one-hot encoding

## Example Workflow

1. Upload `laptopData.csv`
2. Review dataset in "Dataset Overview"
3. Check missing values in "Data Exploration"
4. Convert string columns to numeric in "Data Cleaning"
5. Apply label encoding to categorical columns in "Categorical Encoding"
6. Download the processed data as CSV

## Tips & Best Practices

- **Always Preview**: Check your data before and after operations
- **Missing Data**: Decide on imputation strategy based on data distribution
- **Categorical Encoding**: Choose based on use case:
  - One-Hot: Better for tree-based models
  - Label: Better for linear models and space efficiency
- **Download**: Export intermediate results for backup

## Troubleshooting

### File Upload Issues
- Ensure your CSV is properly formatted
- Check for encoding issues (use UTF-8)

### Memory Issues
- For very large datasets, consider sampling or chunking
- Use "Drop Columns" to remove unnecessary features

### Numeric Conversion Issues
- Review unique values before conversion
- Check for special characters or inconsistent formatting

## Future Enhancements

- Data visualization with multiple chart types
- Statistical testing
- Feature scaling and normalization
- Outlier detection and removal
- Feature engineering tools
- Machine learning model integration

## License

MIT License

## Author

Created for educational purposes - College DM Project
