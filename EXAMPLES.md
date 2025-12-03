# Example Usage Scenarios

## Scenario 1: Clean Laptop Dataset

### Goal: Prepare laptop data for analysis

### Steps:

1. **Upload Data**
   - Upload `laptopData.csv` from sidebar

2. **Dataset Overview**
   - Check shape: ~300 rows, 13 columns
   - Note any missing values or duplicates

3. **Data Exploration**
   - View missing values → Identify problematic columns
   - Check data types → Ensure correct types
   - Analyze unique values → Understand categories

4. **Data Cleaning**
   - Convert numeric columns:
     - Select: Ram, Weight, Price, Inches
     - Removes units (GB, kg, $)
     - Converts to numeric
   
   - Handle missing values:
     - For numeric: Use median
     - For categorical: Use mode
   
   - Drop duplicates:
     - Remove exact duplicates

5. **Categorical Encoding**
   - Select: Company, TypeName, OpSys
   - Apply: Label Encoding (more compact)
   - Result: All columns now numeric

6. **Download**
   - Export as CSV: `laptopData_cleaned.csv`
   - Ready for machine learning!

---

## Scenario 2: Sales Data Analysis

### Goal: Prepare sales data for visualization and reporting

### Steps:

1. **Upload Data**
   - Upload sales CSV with columns: Date, Region, Product, Sales, Status

2. **Exploratory Analysis**
   - Summary Statistics → Understand sales range
   - Unique Values → Find regions and products
   - Missing Values → Check data completeness

3. **Data Cleaning**
   - Remove invalid entries (negative sales)
   - Fill missing dates with forward fill
   - Standardize region names

4. **Categorical Encoding**
   - One-Hot Encoding for Region → Create binary columns
   - One-Hot Encoding for Product → Separate features
   - Label Encoding for Status → Simple numeric

5. **Download**
   - Export as Excel: Share with team
   - Create visualizations with cleaned data

---

## Scenario 3: Customer Survey Data

### Goal: Prepare survey responses for statistical analysis

### Steps:

1. **Upload Data**
   - Survey with questions 1-10 (numeric 1-5 scale)
   - Demographic columns (text)

2. **Data Exploration**
   - Check response distribution
   - Verify scale (1-5)
   - Identify missing responses

3. **Data Cleaning**
   - Convert responses to numeric (handle typos)
   - Fill missing with median response
   - Remove incomplete surveys (>3 missing)

4. **Categorical Encoding**
   - Label encode demographics
   - Result: All numeric for correlation analysis

5. **Download**
   - Export as CSV for SPSS or R

---

## Common Patterns

### Pattern 1: Unit Removal
```
Before: "16GB", "2.5kg", "$999"
After:  16, 2.5, 999
```
**Action**: Data Cleaning → Convert Numeric Columns

### Pattern 2: Missing Data Strategy
```
Numeric columns → Median (less affected by outliers)
Categorical → Mode (most frequent value)
Date columns → Forward fill (time-series logic)
```
**Action**: Data Cleaning → Replace Missing Values

### Pattern 3: Encoding for ML
```
One-Hot → Tree models (Random Forest, XGBoost)
Label → Linear models, compact representation
```
**Action**: Categorical Encoding

---

## Tips & Tricks

### Tip 1: Preview Before Committing
- Use "Show Unique Values" before converting
- Check "Missing Values" heatmap before filling
- Don't drop columns without review

### Tip 2: Incremental Cleaning
- Don't apply all operations at once
- Test on sample first
- Download intermediate results

### Tip 3: Encoding Strategy
- Check cardinality (number of unique values)
- Low cardinality (<10) → One-Hot Encoding
- High cardinality (>100) → Label Encoding or drop
- Binary → Label Encoding sufficient

### Tip 4: Reset Anytime
- Made a mistake? No problem!
- Click "Reset to Original" in Data Cleaning
- Start over without re-uploading

---

## Before and After Examples

### Example 1: Price Column

**Before:**
```
Company     Price       Ram
Dell        $50,000     16GB
HP          $75,000     NaN
Lenovo      InvalidPrr  8GB
```

**After:**
```
Company     Price   Ram
0           50000   16
1           75000   16    (filled with median)
2           62500   8     (fixed, filled)
```

**Operations Applied:**
1. Remove $ symbol
2. Convert to numeric
3. Fill NaN with median

---

### Example 2: Categorical Data

**Before:**
```
Company    TypeName    
Dell       Laptop      
HP         LAPTOP      (inconsistent case)
Lenovo     Ultrabook   
```

**After (One-Hot):**
```
Company_0  Company_1  Company_2  TypeName_0  TypeName_1
1          0          0          0           1
0          1          0          0           1
0          0          1          1           0
```

**After (Label):**
```
Company  TypeName
0        1
1        1
2        0
```

---

## Workflow Recommendations

### For Machine Learning
1. ✅ Dataset Overview
2. ✅ Check Missing Values
3. ✅ Convert to Numeric
4. ✅ One-Hot Encoding
5. ✅ Download

### For Statistical Analysis
1. ✅ Summary Statistics
2. ✅ Check Duplicates
3. ✅ Fill Missing (median)
4. ✅ Label Encoding
5. ✅ Download

### For Reporting
1. ✅ Dataset Overview
2. ✅ Show Unique Values
3. ✅ Summary Statistics
4. ✅ Download

---

## Q&A

**Q: Should I remove all rows with missing values?**
A: No! Use summary stats first. Often better to impute strategically.

**Q: One-Hot or Label Encoding?**
A: One-Hot if features could interact (category combinations matter). Label if ordinal or for memory efficiency.

**Q: How to handle outliers?**
A: This tool focuses on missing data. Use external scripts for outlier detection.

**Q: Can I upload multiple files?**
A: Upload one at a time. Download results and re-upload for combining.

**Q: What if conversion fails?**
A: Check "Show Unique Values" - data may have unexpected format.

---

## Next Steps After Cleaning

1. **Load into Python/R** for advanced analysis
2. **Build ML Models** with cleaned data
3. **Create Visualizations** with matplotlib/ggplot2
4. **Share Results** with stakeholders
5. **Iterate** as needed for better results

Enjoy your data cleaning journey! 🎉
