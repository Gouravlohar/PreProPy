"""
Example ML workflow script using the PreProPy package.

This script demonstrates how to use PreProPy in a typical machine learning workflow:
1. Handle missing values
2. Remove duplicates
3. Create a scaled pipeline
4. Train and evaluate a model
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import os
import sys

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import PreProPy functions
from prepropy import handle_nulls, drop_duplicates, scale_pipeline


def prepare_data(data_file):
    """
    Prepare the dataset for machine learning.
    
    Parameters:
    -----------
    data_file : str
        Path to the CSV data file
    
    Returns:
    --------
    X_train, X_test, y_train, y_test
        Split datasets for model training and evaluation
    """
    print("Loading data...")
    df = pd.read_csv(data_file)
    
    # Display basic info
    print(f"\nDataset shape: {df.shape}")
    print("\nMissing values per column:")
    print(df.isna().sum())
    
    # Step 1: Handle missing values
    print("\nHandling missing values...")
    df_filled = handle_nulls(df, strategy="auto")
    print("Missing values after filling:", df_filled.isna().sum().sum())
    
    # Step 2: Remove duplicates
    print("\nRemoving duplicates...")
    df_unique = drop_duplicates(df_filled)
    print(f"Rows before: {len(df_filled)}, Rows after: {len(df_unique)}")
    
    # For this example, we'll try to predict if income is above median
    # based on other features
    median_income = df_unique['income'].median()
    df_unique['high_income'] = (df_unique['income'] > median_income).astype(int)
    
    # Select features and target
    features = ['age', 'education', 'job_category', 'satisfaction', 'years_experience']
    target = 'high_income'
    
    # Convert categorical columns to one-hot encoding
    df_encoded = pd.get_dummies(df_unique[features])
    
    # Split data
    X = df_encoded
    y = df_unique[target]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"\nTraining set shape: {X_train.shape}")
    print(f"Test set shape: {X_test.shape}")
    
    return X_train, X_test, y_train, y_test


def train_model(X_train, X_test, y_train, y_test):
    """
    Train and evaluate models with different scaling approaches.
    
    Parameters:
    -----------
    X_train, X_test, y_train, y_test : DataFrame, Series
        Training and test datasets
    
    Returns:
    --------
    None, prints evaluation metrics
    """
    # Base model (LogisticRegression)
    model = LogisticRegression(random_state=42, max_iter=1000)
    
    # Test with different scalers
    scalers = ["standard", "minmax", "robust"]
    
    for scaler_type in scalers:
        print(f"\n===== Using {scaler_type} scaler =====")
        
        # Step 3: Create a pipeline with scaling
        pipeline = scale_pipeline(model, scaler=scaler_type)
        
        # Train model
        print(f"Training model...")
        pipeline.fit(X_train, y_train)
        
        # Evaluate model
        print(f"Evaluating model...")
        y_pred = pipeline.predict(X_test)
        
        # Print results
        accuracy = accuracy_score(y_test, y_pred)
        print(f"\nAccuracy with {scaler_type} scaler: {accuracy:.4f}")
        print("\nClassification report:")
        print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    # Get the data file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, "sample_data.csv")
    
    if not os.path.exists(data_file):
        print(f"Error: Sample data file not found at {data_file}")
        print("Please run generate_sample_data.py first to create the sample dataset.")
        sys.exit(1)
    
    print("=" * 50)
    print("PreProPy ML Workflow Example")
    print("=" * 50)
    
    # Prepare data
    X_train, X_test, y_train, y_test = prepare_data(data_file)
    
    # Train and evaluate model
    train_model(X_train, X_test, y_train, y_test)
    
    print("\nWorkflow complete!")
