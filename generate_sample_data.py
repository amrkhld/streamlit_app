"""
Sample Data Generator for Testing the Streamlit App
Creates a sample laptop dataset similar to laptopData.csv
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Sample data
companies = ['Dell', 'HP', 'Lenovo', 'Asus', 'Apple', 'MSI', 'Razer', 'Acer']
type_names = ['Ultrabook', 'Laptop', 'Gaming', 'Convertible', 'Workstation']
cpu_brands = ['Intel', 'AMD']
cpu_models = ['Core i3', 'Core i5', 'Core i7', 'Core i9', 'Ryzen 3', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9']
gpu_brands = ['Intel', 'Nvidia', 'AMD']
gpu_models = ['UHD', 'GeForce GTX 1050', 'GeForce RTX 3060', 'Radeon RX', 'M1', 'M2']
os_types = ['Windows 10', 'Windows 11', 'macOS', 'Linux']
memory_types = ['512GB SSD', '256GB SSD', '1TB SSD', '512GB HDD', '256GB SSD+512GB HDD', '1TB SSD+512GB HDD']

# Generate sample data
n_samples = 100

data = {
    'Company': [random.choice(companies) for _ in range(n_samples)],
    'TypeName': [random.choice(type_names) for _ in range(n_samples)],
    'Inches': np.random.uniform(13.3, 17.3, n_samples).round(1),
    'Ram': [f"{random.choice([4, 8, 16, 32])}GB" for _ in range(n_samples)],
    'Weight': [f"{random.uniform(1.5, 5.0):.2f}kg" for _ in range(n_samples)],
    'Cpu': [f"{random.choice(cpu_brands)} {random.choice(cpu_models)} {random.uniform(1.5, 3.5):.1f}GHz" 
            for _ in range(n_samples)],
    'Memory': [random.choice(memory_types) for _ in range(n_samples)],
    'Gpu': [f"{random.choice(gpu_brands)} {random.choice(gpu_models)}" for _ in range(n_samples)],
    'OpSys': [random.choice(os_types) for _ in range(n_samples)],
    'Price': np.random.uniform(20000, 200000, n_samples).round(-2),  # Round to nearest 100
}

# Create DataFrame
df = pd.DataFrame(data)

# Introduce some missing values (10%)
missing_percentage = 0.1
for col in ['Ram', 'Weight', 'Price']:
    missing_indices = np.random.choice(df.index, size=int(len(df) * missing_percentage), replace=False)
    df.loc[missing_indices, col] = np.nan

# Introduce some duplicates (5%)
n_duplicates = int(len(df) * 0.05)
duplicate_indices = np.random.choice(df.index, size=n_duplicates, replace=False)
df = pd.concat([df, df.loc[duplicate_indices]], ignore_index=True)

# Save to CSV
df.to_csv('sample_laptop_data.csv', index=False)
print(f"✅ Sample dataset created: sample_laptop_data.csv")
print(f"\nDataset Info:")
print(f"- Shape: {df.shape}")
print(f"- Missing values: {df.isnull().sum().sum()}")
print(f"- Duplicates: {df.duplicated().sum()}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nData types:")
print(df.dtypes)
