"""
Simple demonstration of PreProPy functionality.

This script shows basic usage examples for all the package's main functions.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import sys
import os

# Add the root directory to Python path for direct imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import functions directly from modules for testing
from prepropy.nullsense import handle_nulls
from prepropy.duplichecker import drop_duplicates, get_duplicate_stats
from prepropy.scalenpipe import scale_pipeline, get_available_scalers

def test_nullsense():
    """Demonstrate NullSense functionality."""
    print("\n=== Testing NullSense ===")
    
    # Create sample data with missing values
    df = pd.DataFrame({
        'numeric1': [1, 2, None, 4, 5, 6, None],
        'numeric2': [10.5, None, 12.2, 13.5, None, 9.8, 8.5],
        'category1': ['A', 'B', None, 'B', 'C', None, 'A'],
        'category2': [None, 'Y', 'Z', 'Y', 'Y', 'X', None]
    })
    
    print("Original dataframe:")
    print(df)
    
    # Auto strategy (default)
    df_auto = handle_nulls(df)
    print("\nAuto strategy (median for numeric, mode for categorical):")
    print(df_auto)
    
    # Mean strategy
    df_mean = handle_nulls(df, strategy="mean")
    print("\nMean strategy:")
    print(df_mean)
    
    # Zero strategy
    df_zero = handle_nulls(df, strategy="zero")
    print("\nZero strategy:")
    print(df_zero)
    

def test_duplichecker():
    """Demonstrate DupliChecker functionality."""
    print("\n=== Testing DupliChecker ===")
    
    # Create sample data with duplicates
    df = pd.DataFrame({
        'id': [1, 2, 3, 2, 4, 5, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'Bob', 'David', 'Eve', 'Eve'],
        'value': [100, 200, 150, 200, 300, 250, 250]
    })
    
    print("Original dataframe:")
    print(df)
    
    # Get duplicate statistics
    stats = get_duplicate_stats(df)
    print("\nDuplicate statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Drop duplicates (all columns)
    df_unique = drop_duplicates(df)
    print("\nAfter dropping duplicates (all columns, keep first):")
    print(df_unique)
    
    # Drop duplicates based on subset
    df_unique_subset = drop_duplicates(df, subset=['name'])
    print("\nAfter dropping duplicates (by name only):")
    print(df_unique_subset)
    
    # Drop all duplicates
    df_no_dups = drop_duplicates(df, keep=False)
    print("\nAfter dropping all duplicates (no keeps):")
    print(df_no_dups)


def test_scalenpipe():
    """Demonstrate ScaleNPipe functionality."""
    print("\n=== Testing ScaleNPipe ===")
    
    # Create a simple dataset
    X = np.array([[-1, 2], [-0.5, 6], [0, 10], [1, 18], [2, 20]])
    y = np.array([0, 0, 0, 1, 1])
    
    # Create a model
    model = LogisticRegression(random_state=42)
    
    # Show available scalers
    scalers = get_available_scalers()
    print("Available scalers:")
    for name, desc in scalers.items():
        print(f"- {name}: {desc}")
    
    # Create pipelines with different scalers
    print("\nCreating pipelines with different scalers...")
    
    # Standard scaler
    std_pipeline = scale_pipeline(model, scaler="standard")
    std_pipeline.fit(X, y)
    print(f"Standard scaler pipeline accuracy: {std_pipeline.score(X, y):.4f}")
    
    # MinMax scaler
    minmax_pipeline = scale_pipeline(model, scaler="minmax")
    minmax_pipeline.fit(X, y)
    print(f"MinMax scaler pipeline accuracy: {minmax_pipeline.score(X, y):.4f}")
    
    # Robust scaler
    robust_pipeline = scale_pipeline(model, scaler="robust")
    robust_pipeline.fit(X, y)
    print(f"Robust scaler pipeline accuracy: {robust_pipeline.score(X, y):.4f}")


if __name__ == "__main__":
    print("PreProPy Demo\n")
    
    test_nullsense()
    test_duplichecker()
    test_scalenpipe()
    
    print("\nDemo completed!")
