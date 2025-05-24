"""
Script to generate a sample dataset for demonstrating PreProPy.

This script creates a CSV file with a mix of numeric and categorical data
that has missing values and duplicates, perfect for showing PreProPy's features.
"""
import pandas as pd
import numpy as np
import os

def create_sample_dataset(output_file="sample_data.csv", rows=100, missing_rate=0.1):
    """
    Create a sample dataset with missing values and duplicates.
    
    Parameters:
    -----------
    output_file : str, default="sample_data.csv"
        File path to save the dataset
    rows : int, default=100
        Number of rows to generate
    missing_rate : float, default=0.1
        Percentage of missing values to introduce
    
    Returns:
    --------
    None
    """
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate data
    data = {
        'id': range(1, rows + 1),
        'age': np.random.randint(18, 80, size=rows),
        'income': np.random.normal(50000, 15000, size=rows).astype(int),
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], size=rows),
        'job_category': np.random.choice(['Tech', 'Finance', 'Healthcare', 'Education', 'Other'], size=rows),
        'satisfaction': np.random.randint(1, 11, size=rows),
        'years_experience': np.random.randint(0, 40, size=rows)
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Introduce missing values randomly
    total_cells = rows * (len(df.columns) - 1)  # Exclude id column from missing values
    missing_cells = int(total_cells * missing_rate)
    
    # Get indices for cells to set as missing (excluding 'id' column)
    for _ in range(missing_cells):
        col = np.random.choice(df.columns[1:])  # Skip the 'id' column
        row = np.random.randint(0, rows)
        df.loc[row, col] = np.nan
    
    # Introduce duplicates (about 5% of the data)
    num_duplicates = int(rows * 0.05)
    for _ in range(num_duplicates):
        # Pick a random row to duplicate
        source_idx = np.random.randint(0, rows)
        # Pick a random row to overwrite
        target_idx = np.random.randint(0, rows)
        # Avoid duplicating the same row
        while target_idx == source_idx:
            target_idx = np.random.randint(0, rows)
            
        # Copy values except 'id'
        for col in df.columns[1:]:
            df.loc[target_idx, col] = df.loc[source_idx, col]
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Sample dataset created: {output_file}")
    print(f"Total rows: {rows}")
    print(f"Missing values: {df.isna().sum().sum()} (~{missing_rate*100:.1f}%)")
    
    # Count duplicates (excluding id)
    subset = list(df.columns[1:])
    duplicate_count = df.duplicated(subset=subset).sum()
    print(f"Duplicate rows (based on non-id columns): {duplicate_count} (~{duplicate_count/rows*100:.1f}%)")


if __name__ == "__main__":
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "sample_data.csv")
    create_sample_dataset(output_file)
