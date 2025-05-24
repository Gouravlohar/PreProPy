# PreProPy

A Python package combining three essential preprocessing tools for data science: NullSense, DupliChecker, and ScaleNPipe.

[![PyPI version](https://badge.fury.io/py/prepropy.svg)](https://badge.fury.io/py/prepropy)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Overview

PreProPy is a comprehensive data preprocessing toolkit designed to streamline your data science workflow. It combines three powerful tools:

- **🧩 NullSense**: Intelligent handling of missing values based on column types
- **🔍 DupliChecker**: Duplicate record detection and removal with configurable options
- **⚖️ ScaleNPipe**: Feature scaling and model pipeline creation for machine learning workflows

## 🔧 Installation

```bash
pip install prepropy
```

## 🚀 Features

PreProPy provides three core components:

### 1. NullSense

Intelligently handle missing values in your data based on column types:

```python
import pandas as pd
from prepropy import handle_nulls

# Create a sample dataframe with missing values
df = pd.DataFrame({
    'numeric': [1, 2, None, 4, 5],
    'categorical': ['A', 'B', None, 'B', 'C']
})

# Fill missing values with intelligent defaults
df_filled = handle_nulls(df, strategy="auto")
# Numeric columns filled with median, categorical with mode

# Other available strategies
df_mean = handle_nulls(df, strategy="mean")  # Fill numeric with mean
df_median = handle_nulls(df, strategy="median")  # Fill numeric with median
df_mode = handle_nulls(df, strategy="mode")  # Fill all columns with mode
df_zero = handle_nulls(df, strategy="zero")  # Fill numeric with 0, categorical with ""
```

### 2. DupliChecker

Identify and remove duplicate records with configurable options:

```python
import pandas as pd
from prepropy import drop_duplicates, get_duplicate_stats

# Create a sample dataframe with duplicates
df = pd.DataFrame({
    'A': [1, 2, 2, 3, 3],
    'B': ['x', 'y', 'y', 'z', 'z']
})

# Get duplicate statistics
stats = get_duplicate_stats(df)
print(stats)
# Output: {'duplicate_count': 2, 'duplicate_percent': 40.0, 'unique_count': 3, 'total_count': 5}

# Drop duplicates (keeping first occurrence)
df_unique = drop_duplicates(df)

# Drop duplicates based on specific columns
df_unique_subset = drop_duplicates(df, subset=['B'])

# Keep the last occurrence instead of first
df_unique_last = drop_duplicates(df, keep='last')

# Drop all duplicates
df_no_dups = drop_duplicates(df, keep=False)
```

### 3. ScaleNPipe

Create scikit-learn pipelines with feature scaling and your model:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from prepropy import scale_pipeline, get_available_scalers

# Load sample data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a model
model = LogisticRegression()

# Create a pipeline with standard scaling
pipeline = scale_pipeline(model, scaler="standard")

# Train the pipeline
pipeline.fit(X_train, y_train)

# Make predictions
predictions = pipeline.predict(X_test)

# See available scalers
scalers = get_available_scalers()
print(scalers)
```

## 🖥️ Command Line Interface

PreProPy provides a command-line interface for quick data processing:

```bash
# Handle missing values
prepropy nulls input.csv output.csv --strategy auto

# Handle duplicates
prepropy dups input.csv output.csv --subset col1,col2 --keep first

# Get information about available scalers
prepropy scale --list-scalers
```

## 📁 Project Structure

The PreProPy package is organized as follows:

```
prepropy/
├── __init__.py       # Package initialization and exports
├── nullsense.py      # Missing values handling functionality
├── duplichecker.py   # Duplicate records handling functionality  
├── scalenpipe.py     # Scaling and pipeline creation functionality
└── cli.py            # Command-line interface implementation
```

For a more detailed explanation of the project structure, please refer to [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md).

## 📝 Documentation

For more detailed documentation and examples:

1. Check the [usage guide](docs/usage.md) for comprehensive API documentation
2. Explore the [examples directory](examples/) for Jupyter notebooks with practical use cases
3. Review the [test directory](tests/) to understand the expected behavior

## 📦 Dependencies

- Python 3.7+
- pandas >= 1.0.0
- scikit-learn >= 0.24.0

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to help improve PreProPy.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Gourav Lohar
