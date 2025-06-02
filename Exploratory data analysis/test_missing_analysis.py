#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the smartphone dataset
df = pd.read_csv('smartphone_cleaned_v5.csv')

print("=== DATASET OVERVIEW ===")
print(f"Shape: {df.shape}")
print(f"Total missing values: {df.isnull().sum().sum()}")

print("\n=== MISSING VALUES BY COLUMN ===")
missing = df.isnull().sum()
for col, count in missing[missing > 0].items():
    print(f"{col}: {count} ({count/len(df)*100:.1f}%)")

# Test the comprehensive missing analysis function
def comprehensive_missing_analysis(df):
    """
    Detailed missing data analysis - key interview topic
    """
    print("\n=== COMPREHENSIVE MISSING DATA ANALYSIS ===")
    
    # Basic missing data statistics
    missing_data = df.isnull().sum()
    missing_percent = (missing_data / len(df)) * 100
    
    missing_df = pd.DataFrame({
        'Column': df.columns,
        'Missing_Count': missing_data,
        'Missing_Percentage': missing_percent,
        'Data_Type': df.dtypes,
        'Non_Missing_Count': len(df) - missing_data
    }).sort_values('Missing_Percentage', ascending=False)
    
    # Filter only columns with missing data
    missing_cols_df = missing_df[missing_df['Missing_Count'] > 0]
    
    if len(missing_cols_df) > 0:
        print("\n📊 MISSING DATA SUMMARY:")
        print(missing_cols_df[['Column', 'Missing_Count', 'Missing_Percentage', 'Data_Type']].to_string(index=False))
        
        print(f"\n📈 OVERALL STATISTICS:")
        print(f"Total missing values: {missing_data.sum():,}")
        print(f"Rows with any missing data: {df.isnull().any(axis=1).sum():,} ({df.isnull().any(axis=1).sum()/len(df)*100:.1f}%)")
        print(f"Complete rows: {df.dropna().shape[0]:,} ({df.dropna().shape[0]/len(df)*100:.1f}%)")
        print(f"Columns with missing data: {len(missing_cols_df)} out of {len(df.columns)}")
        
        return missing_cols_df
    else:
        print("\n✅ No missing data found!")
        return pd.DataFrame()

# Test the function
result = comprehensive_missing_analysis(df)
print("\n=== ANALYSIS COMPLETE ===")
print(f"Found {len(result)} columns with missing data")
