import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import io
import warnings

warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(page_title="Data Cleaning & EDA Tool", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Data Cleaning & Exploratory Data Analysis Tool")
st.markdown("---")

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None
if 'df_original' not in st.session_state:
    st.session_state.df_original = None

# Sidebar for file upload
st.sidebar.header("📁 Data Upload")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        st.session_state.df = pd.read_csv(uploaded_file)
        st.session_state.df_original = st.session_state.df.copy()
        st.sidebar.success("✅ File loaded successfully!")
    except Exception as e:
        st.sidebar.error(f"Error reading file: {e}")

# Main content
if st.session_state.df is not None:
    df = st.session_state.df
    
    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📈 Dataset Overview",
        "🔍 Data Exploration",
        "🧹 Data Cleaning",
        "🏷️ Categorical Encoding",
        "📊 Visualizations & Analysis",
        "📥 Download"
    ])
    
    # ============ TAB 1: DATASET OVERVIEW ============
    with tab1:
        st.header("Dataset Overview")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📊 Rows", df.shape[0])
        with col2:
            st.metric("📋 Columns", df.shape[1])
        with col3:
            st.metric("❌ Missing Values", df.isnull().sum().sum())
        with col4:
            st.metric("🔁 Duplicates", df.duplicated().sum())
        
        st.subheader("Data Preview")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔝 Show Head (5 rows)"):
                st.write(df.head())
        
        with col2:
            if st.button("🔚 Show Tail (5 rows)"):
                st.write(df.tail())
        
        with col3:
            rows_to_show = st.number_input("Show custom rows:", min_value=1, max_value=len(df), value=10)
            if st.button("📄 Show Custom Rows"):
                st.write(df.head(rows_to_show))
        
        st.subheader("Show All Rows")
        if st.checkbox("Display full dataset (all rows)"):
            st.write(df)
        
        st.subheader("Column Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📝 Show Column Names"):
                st.write("**Column Names:**")
                for i, col in enumerate(df.columns, 1):
                    st.write(f"{i}. {col}")
        
        with col2:
            if st.button("📊 Show Data Types"):
                st.write(df.dtypes)
        
        st.subheader("Dataset Shape")
        st.info(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    
    # ============ TAB 2: DATA EXPLORATION ============
    with tab2:
        st.header("Data Exploration & Analysis")
        
        exploration_option = st.radio(
            "Select exploration type:",
            ["Summary Statistics", "Data Types", "Missing Values", "Duplicates", "Unique Values"]
        )
        
        if exploration_option == "Summary Statistics":
            st.subheader("Summary Statistics")
            st.write(df.describe(include='all'))
            
            # Display numeric summary
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                st.write("\n**Numeric Columns Summary:**")
                st.write(df[numeric_cols].describe())
        
        elif exploration_option == "Data Types":
            st.subheader("Data Types Info")
            dtype_info = pd.DataFrame({
                'Column': df.columns,
                'Data Type': df.dtypes.values,
                'Non-Null Count': df.count().values,
                'Null Count': df.isnull().sum().values
            })
            st.write(dtype_info)
        
        elif exploration_option == "Missing Values":
            st.subheader("Missing Values Analysis")
            
            missing_data = pd.DataFrame({
                'Column': df.columns,
                'Missing Count': df.isnull().sum().values,
                'Missing %': (df.isnull().sum().values / len(df) * 100).round(2)
            })
            missing_data = missing_data[missing_data['Missing Count'] > 0].sort_values('Missing Count', ascending=False)
            
            if len(missing_data) > 0:
                st.write(missing_data)
                
                # Visualize missing data
                fig, ax = plt.subplots(figsize=(12, 6))
                sns.heatmap(df.isnull(), cbar=False, cmap='viridis', ax=ax)
                plt.title("Missing Data Heatmap")
                st.pyplot(fig)
            else:
                st.success("✅ No missing values found!")
        
        elif exploration_option == "Duplicates":
            st.subheader("Duplicate Rows Analysis")
            dup_count = df.duplicated().sum()
            st.info(f"**Total duplicate rows:** {dup_count}")
            
            if dup_count > 0:
                st.write("**Sample of duplicate rows:**")
                st.write(df[df.duplicated(keep=False)].sort_values(by=list(df.columns)).head(10))
        
        elif exploration_option == "Unique Values":
            st.subheader("Unique Values per Column")
            
            col1, col2 = st.columns(2)
            
            with col1:
                selected_col = st.selectbox("Select column:", df.columns)
            
            with col2:
                max_unique = st.number_input("Max unique values to show:", min_value=5, value=20)
            
            unique_vals = df[selected_col].value_counts().head(max_unique)
            
            st.write(f"**Unique values in '{selected_col}':** {df[selected_col].nunique()}")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.write(unique_vals)
            
            with col2:
                fig, ax = plt.subplots(figsize=(10, 6))
                unique_vals.plot(kind='barh', ax=ax, color='skyblue')
                plt.title(f"Top {max_unique} Values in {selected_col}")
                plt.xlabel("Count")
                st.pyplot(fig)
    
    # ============ TAB 3: DATA CLEANING ============
    with tab3:
        st.header("Data Cleaning Tools")
        
        cleaning_option = st.selectbox(
            "Select cleaning operation:",
            [
                "Convert Numeric Columns",
                "Show Unique Values",
                "Replace Missing Values",
                "Drop Rows with NaN",
                "Drop Columns",
                "Reset to Original"
            ]
        )
        
        if cleaning_option == "Convert Numeric Columns":
            st.subheader("Convert Columns to Numeric")
            
            object_cols = df.select_dtypes(include=['object']).columns.tolist()
            
            if len(object_cols) > 0:
                selected_cols = st.multiselect("Select columns to convert to numeric:", object_cols)
                
                if st.button("🔄 Convert Selected Columns"):
                    for col in selected_cols:
                        # Remove common units
                        df[col] = df[col].astype(str).str.replace('GB', '', regex=False)
                        df[col] = df[col].astype(str).str.replace('kg', '', regex=False)
                        df[col] = df[col].astype(str).str.replace('GHz', '', regex=False)
                        df[col] = df[col].astype(str).str.replace('$', '', regex=False)
                        
                        # Convert to numeric
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                    
                    st.session_state.df = df
                    st.success(f"✅ Converted {len(selected_cols)} column(s) to numeric!")
                    st.write(df[selected_cols].dtypes)
            else:
                st.info("No object columns found.")
        
        elif cleaning_option == "Show Unique Values":
            st.subheader("Unique Values per Column")
            
            col_for_unique = st.selectbox("Select a column:", df.columns)
            unique_count = df[col_for_unique].nunique()
            
            st.write(f"**Unique values:** {unique_count}")
            st.write(df[col_for_unique].value_counts())
        
        elif cleaning_option == "Replace Missing Values":
            st.subheader("Handle Missing Values")
            
            cols_with_missing = df.columns[df.isnull().any()].tolist()
            
            if len(cols_with_missing) > 0:
                col1, col2 = st.columns(2)
                
                with col1:
                    selected_col = st.selectbox("Select column with missing values:", cols_with_missing)
                
                with col2:
                    fill_method = st.selectbox(
                        "Fill method:",
                        ["Mean", "Median", "Mode", "Forward Fill", "Backward Fill", "Custom Value"]
                    )
                
                if st.button("🔄 Fill Missing Values"):
                    if fill_method == "Mean":
                        if pd.api.types.is_numeric_dtype(df[selected_col]):
                            df[selected_col].fillna(df[selected_col].mean(), inplace=True)
                            st.success(f"✅ Filled with mean!")
                        else:
                            st.error("Column is not numeric!")
                    
                    elif fill_method == "Median":
                        if pd.api.types.is_numeric_dtype(df[selected_col]):
                            df[selected_col].fillna(df[selected_col].median(), inplace=True)
                            st.success(f"✅ Filled with median!")
                        else:
                            st.error("Column is not numeric!")
                    
                    elif fill_method == "Mode":
                        mode_val = df[selected_col].mode()[0]
                        df[selected_col].fillna(mode_val, inplace=True)
                        st.success(f"✅ Filled with mode: {mode_val}")
                    
                    elif fill_method == "Forward Fill":
                        df[selected_col].fillna(method='ffill', inplace=True)
                        st.success(f"✅ Applied forward fill!")
                    
                    elif fill_method == "Backward Fill":
                        df[selected_col].fillna(method='bfill', inplace=True)
                        st.success(f"✅ Applied backward fill!")
                    
                    elif fill_method == "Custom Value":
                        custom_val = st.text_input("Enter value to fill:")
                        if st.button("Fill with custom value"):
                            df[selected_col].fillna(custom_val, inplace=True)
                            st.success(f"✅ Filled with: {custom_val}")
                    
                    st.session_state.df = df
                    st.write(f"Remaining missing values: {df[selected_col].isnull().sum()}")
            else:
                st.success("✅ No missing values found!")
        
        elif cleaning_option == "Drop Rows with NaN":
            st.subheader("Drop Rows with Missing Values")
            
            col1, col2 = st.columns(2)
            
            with col1:
                drop_option = st.radio(
                    "Drop rows where:",
                    ["Any value is NaN", "All values are NaN", "Custom threshold"]
                )
            
            with col2:
                if drop_option == "Custom threshold":
                    threshold = st.slider("Min non-null values required:", 1, len(df.columns), len(df.columns))
            
            if st.button("🗑️ Drop Rows"):
                rows_before = len(df)
                
                if drop_option == "Any value is NaN":
                    df.dropna(inplace=True)
                elif drop_option == "All values are NaN":
                    df.dropna(how='all', inplace=True)
                elif drop_option == "Custom threshold":
                    df.dropna(thresh=threshold, inplace=True)
                
                rows_after = len(df)
                st.session_state.df = df
                st.success(f"✅ Dropped {rows_before - rows_after} row(s)!")
                st.info(f"Remaining rows: {rows_after}")
        
        elif cleaning_option == "Drop Columns":
            st.subheader("Drop Columns")
            
            cols_to_drop = st.multiselect("Select columns to drop:", df.columns)
            
            if st.button("🗑️ Drop Selected Columns"):
                if len(cols_to_drop) > 0:
                    df.drop(columns=cols_to_drop, inplace=True)
                    st.session_state.df = df
                    st.success(f"✅ Dropped {len(cols_to_drop)} column(s)!")
                else:
                    st.warning("Please select at least one column!")
        
        elif cleaning_option == "Reset to Original":
            if st.button("🔄 Reset to Original Dataset"):
                st.session_state.df = st.session_state.df_original.copy()
                st.success("✅ Dataset reset to original!")
    
    # ============ TAB 4: CATEGORICAL ENCODING ============
    with tab4:
        st.header("Categorical Encoding")
        
        encoding_option = st.selectbox(
            "Select encoding method:",
            ["One-Hot Encoding", "Label Encoding"]
        )
        
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        if len(categorical_cols) == 0:
            st.warning("No categorical columns found!")
        else:
            if encoding_option == "One-Hot Encoding":
                st.subheader("One-Hot Encoding")
                
                selected_cols = st.multiselect(
                    "Select columns for one-hot encoding:",
                    categorical_cols,
                    default=categorical_cols[:1] if len(categorical_cols) > 0 else []
                )
                
                if st.button("🔄 Apply One-Hot Encoding"):
                    if len(selected_cols) > 0:
                        # Create a copy to avoid SettingWithCopyWarning
                        df_encoded = df.copy()
                        
                        for col in selected_cols:
                            # One-hot encode
                            encoded = pd.get_dummies(df_encoded[col], prefix=col, drop_first=False)
                            df_encoded = pd.concat([df_encoded, encoded], axis=1)
                            df_encoded.drop(columns=[col], inplace=True)
                        
                        st.session_state.df = df_encoded
                        st.success(f"✅ Applied one-hot encoding to {len(selected_cols)} column(s)!")
                        st.info(f"New shape: {df_encoded.shape}")
                        st.write(df_encoded.head())
                    else:
                        st.warning("Please select at least one column!")
            
            elif encoding_option == "Label Encoding":
                st.subheader("Label Encoding")
                
                selected_cols = st.multiselect(
                    "Select columns for label encoding:",
                    categorical_cols,
                    default=categorical_cols[:1] if len(categorical_cols) > 0 else []
                )
                
                if st.button("🔄 Apply Label Encoding"):
                    if len(selected_cols) > 0:
                        df_encoded = df.copy()
                        encoder = LabelEncoder()
                        
                        for col in selected_cols:
                            df_encoded[col] = encoder.fit_transform(df_encoded[col].astype(str))
                        
                        st.session_state.df = df_encoded
                        st.success(f"✅ Applied label encoding to {len(selected_cols)} column(s)!")
                        st.write(df_encoded.head())
                    else:
                        st.warning("Please select at least one column!")
    
    # ============ VISUALIZATION FUNCTIONS ============
    def bar_plot(df, feature):
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.countplot(x=feature, data=df, order=df[feature].value_counts().index, palette="Set2", ax=ax)
        plt.xticks(rotation=90)
        plt.title(f"Bar Chart of {feature}")
        st.pyplot(fig)
    
    def box_plot(df, category, numeric):
        fig, ax = plt.subplots(figsize=(15, 7), dpi=150)
        sns.boxplot(x=df[category], y=df[numeric], palette="Set1", ax=ax)
        plt.xticks(rotation=90)
        plt.title(f"Box Plot of {numeric} by {category}")
        st.pyplot(fig)
    
    def histogram(df, feature, bins=30):
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(df[feature], bins=bins, kde=False, color='skyblue', ax=ax)
        plt.title(f"Histogram of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        st.pyplot(fig)
    
    def kde_plot(df, feature):
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.kdeplot(df[feature], shade=True, color='purple', ax=ax)
        plt.title(f"KDE Plot of {feature}")
        plt.xlabel(feature)
        st.pyplot(fig)
    
    def stacked_bar(df, cat1, cat2):
        fig, ax = plt.subplots(figsize=(12, 6))
        ctab = pd.crosstab(df[cat1], df[cat2])
        ctab.plot(kind='bar', stacked=True, ax=ax, colormap='Set3')
        plt.title(f"Stacked Bar Chart: {cat1} vs {cat2}")
        plt.xticks(rotation=90)
        plt.ylabel("Count")
        st.pyplot(fig)
    
    def scatter_plot(df, x, y, hue=None):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=df[x], y=df[y], hue=df[hue] if hue else None, ax=ax)
        plt.title(f"Scatter Plot: {x} vs {y}")
        st.pyplot(fig)
    
    def correlation_heatmap(df):
        fig, ax = plt.subplots(figsize=(14, 10))
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
        plt.title("Correlation Heatmap")
        st.pyplot(fig)
    
    def frequency_table(df, feature):
        freq = df[feature].value_counts().reset_index()
        freq.columns = [feature, "Count"]
        return freq
    
    def summary_table(df, feature):
        return df[feature].describe()
    
    # ============ TAB 6: VISUALIZATIONS & ANALYSIS ============
    with tab6:
        st.header("Visualizations & Statistical Analysis")
        
        st.subheader("📋 Column Names")
        st.write("**Available Columns:**")
        st.write(df.columns.tolist())
        
        visualization_option = st.selectbox(
            "Select visualization type:",
            [
                "Bar Plot",
                "Box Plot",
                "Histogram",
                "KDE Plot",
                "Stacked Bar Chart",
                "Scatter Plot",
                "Correlation Heatmap",
                "Frequency Table",
                "Summary Statistics",
                "Group By Analysis"
            ]
        )
        
        if visualization_option == "Bar Plot":
            st.subheader("Bar Plot")
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            if len(categorical_cols) > 0:
                feature = st.selectbox("Select column:", categorical_cols, key="bar_feature")
                if st.button("📊 Generate Bar Plot", key="bar_btn"):
                    bar_plot(df, feature)
            else:
                st.warning("No categorical columns found!")
        
        elif visualization_option == "Box Plot":
            st.subheader("Box Plot")
            col1, col2 = st.columns(2)
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            with col1:
                if len(categorical_cols) > 0:
                    category = st.selectbox("Select category column:", categorical_cols, key="box_cat")
                else:
                    st.warning("No categorical columns found!")
            
            with col2:
                if len(numeric_cols) > 0:
                    numeric = st.selectbox("Select numeric column:", numeric_cols, key="box_num")
                else:
                    st.warning("No numeric columns found!")
            
            if st.button("📊 Generate Box Plot", key="box_btn"):
                if len(categorical_cols) > 0 and len(numeric_cols) > 0:
                    box_plot(df, category, numeric)
        
        elif visualization_option == "Histogram":
            st.subheader("Histogram")
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) > 0:
                col1, col2 = st.columns(2)
                with col1:
                    feature = st.selectbox("Select numeric column:", numeric_cols, key="hist_feature")
                with col2:
                    bins = st.slider("Number of bins:", 5, 100, 30)
                
                if st.button("📊 Generate Histogram", key="hist_btn"):
                    histogram(df, feature, bins)
            else:
                st.warning("No numeric columns found!")
        
        elif visualization_option == "KDE Plot":
            st.subheader("KDE Plot")
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) > 0:
                feature = st.selectbox("Select numeric column:", numeric_cols, key="kde_feature")
                if st.button("📊 Generate KDE Plot", key="kde_btn"):
                    kde_plot(df, feature)
            else:
                st.warning("No numeric columns found!")
        
        elif visualization_option == "Stacked Bar Chart":
            st.subheader("Stacked Bar Chart")
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            
            if len(categorical_cols) >= 2:
                col1, col2 = st.columns(2)
                with col1:
                    cat1 = st.selectbox("Select first category:", categorical_cols, key="stack_cat1")
                with col2:
                    cat2 = st.selectbox("Select second category:", categorical_cols, key="stack_cat2")
                
                if st.button("📊 Generate Stacked Bar Chart", key="stack_btn"):
                    stacked_bar(df, cat1, cat2)
            else:
                st.warning("Need at least 2 categorical columns!")
        
        elif visualization_option == "Scatter Plot":
            st.subheader("Scatter Plot")
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            
            if len(numeric_cols) >= 2:
                col1, col2, col3 = st.columns(3)
                with col1:
                    x = st.selectbox("Select X-axis (numeric):", numeric_cols, key="scatter_x")
                with col2:
                    y = st.selectbox("Select Y-axis (numeric):", numeric_cols, key="scatter_y")
                with col3:
                    include_hue = st.checkbox("Add color by category?", key="scatter_hue_check")
                    if include_hue and len(categorical_cols) > 0:
                        hue = st.selectbox("Select category column:", categorical_cols, key="scatter_hue")
                    else:
                        hue = None
                
                if st.button("📊 Generate Scatter Plot", key="scatter_btn"):
                    scatter_plot(df, x, y, hue=hue)
            else:
                st.warning("Need at least 2 numeric columns!")
        
        elif visualization_option == "Correlation Heatmap":
            st.subheader("Correlation Heatmap")
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            
            if len(numeric_cols) > 1:
                if st.button("📊 Generate Correlation Heatmap", key="corr_btn"):
                    correlation_heatmap(df)
            else:
                st.warning("Need at least 2 numeric columns for correlation!")
        
        elif visualization_option == "Frequency Table":
            st.subheader("Frequency Table")
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            
            if len(categorical_cols) > 0:
                feature = st.selectbox("Select column:", categorical_cols, key="freq_feature")
                if st.button("📊 Generate Frequency Table", key="freq_btn"):
                    freq_table = frequency_table(df, feature)
                    st.write(freq_table)
            else:
                st.warning("No categorical columns found!")
        
        elif visualization_option == "Summary Statistics":
            st.subheader("Summary Statistics")
            selected_feature = st.selectbox("Select column for summary:", df.columns, key="summary_feature")
            
            if st.button("📊 Generate Summary", key="summary_btn"):
                summary = summary_table(df, selected_feature)
                st.write(summary)
        
        elif visualization_option == "Group By Analysis":
            st.subheader("Group By Analysis")
            
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            st.write("**Common Aggregations:**")
            
            if len(categorical_cols) > 0 and len(numeric_cols) > 0:
                col1, col2 = st.columns(2)
                with col1:
                    group_col = st.selectbox("Group by column:", categorical_cols, key="groupby_col")
                with col2:
                    agg_col = st.selectbox("Aggregate column:", numeric_cols, key="groupby_agg")
                
                if st.button("📊 Show Aggregations", key="groupby_btn"):
                    st.write("---")
                    
                    # Average
                    result = df.groupby(group_col)[agg_col].mean()
                    st.write(f"**Average {agg_col} per {group_col}:**")
                    st.write(result)
                    st.write("")
            
            # Predefined analyses if columns exist
            st.write("---")
            st.write("**Predefined Analyses:**")
            
            if 'Company' in df.columns and 'Price' in df.columns:
                st.write("**Average Price per Company:**")
                st.write(df.groupby('Company')['Price'].mean())
                
                st.write("**Number of Laptops per Company:**")
                st.write(df.groupby('Company')['Price'].count())
            
            if 'Cpu_Brand' in df.columns and 'Price' in df.columns:
                st.write("**Average Price per CPU Brand:**")
                st.write(df.groupby('Cpu_Brand')['Price'].mean())
            
            if 'Gpu_Brand' in df.columns and 'Price' in df.columns:
                st.write("**Average Price per GPU Brand:**")
                st.write(df.groupby('Gpu_Brand')['Price'].mean())
            
            if 'Company' in df.columns and 'Weight' in df.columns:
                st.write("**Average Weight per Company:**")
                st.write(df.groupby('Company')['Weight'].mean())
            
            if 'Ram' in df.columns and 'Price' in df.columns:
                st.write("**Average Price per RAM Size:**")
                st.write(df.groupby('Ram')['Price'].mean())
            
            if 'TypeName' in df.columns and 'Price' in df.columns:
                st.write("**Average Price per Laptop Type:**")
                st.write(df.groupby('TypeName')['Price'].mean())
            
            if 'OpSys' in df.columns and 'Price' in df.columns:
                st.write("**Number of Laptops per Operating System:**")
                st.write(df.groupby('OpSys')['Price'].count())
    
    # ============ TAB 7: DOWNLOAD ============
    with tab6:
        st.header("Download Processed Data")
        
        col1, col2, col3 = st.columns(3)
        
        # CSV download
        with col1:
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name="processed_data.csv",
                mime="text/csv"
            )
        
        # Excel download
        with col2:
            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False, engine='openpyxl')
            excel_buffer.seek(0)
            st.download_button(
                label="📥 Download as Excel",
                data=excel_buffer,
                file_name="processed_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        # JSON download
        with col3:
            json_data = df.to_json(orient='records', indent=2)
            st.download_button(
                label="📥 Download as JSON",
                data=json_data,
                file_name="processed_data.json",
                mime="application/json"
            )
        
        st.subheader("Data Summary Before Download")
        st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
        st.write(f"**Missing values:** {df.isnull().sum().sum()}")
        st.write(f"**Duplicates:** {df.duplicated().sum()}")
        
        st.subheader("Preview")
        st.write(df.head(10))

else:
    st.info("👈 Upload a CSV file to get started!")
    st.markdown("""
    ### Features:
    - 📁 Upload CSV files
    - 📊 Dataset overview and statistics
    - 🔍 Exploratory data analysis
    - 🧹 Data cleaning tools
    - 🏷️ Categorical encoding (One-Hot & Label)
    - 📥 Download processed data in multiple formats
    """)
