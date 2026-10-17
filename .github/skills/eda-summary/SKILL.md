---
name: eda-summary
description: Inspects small CSV datasets, generates comprehensive Exploratory Data Analysis (EDA) summaries, checks for missing data/outliers, and outputs a clean markdown report.
---

# Exploratory Data Analysis (EDA) Skill

When asked to summarize, inspect, or run EDA on a CSV file, execute a Python command to analyze the dataset and return a structured summary.

## Execution Steps

1. **Inspect Dataset via Terminal**:
   Run a short inline Python command to read the target CSV and extract details:
   ```bash
   python -c "import pandas as pd; df = pd.read_csv('TARGET_FILE.csv'); print('SHAPE:', df.shape); print('\nTYPES:\n', df.dtypes); print('\nMISSING:\n', df.isnull().sum()); print('\nSUMMARY:\n', df.describe(include='all'))"