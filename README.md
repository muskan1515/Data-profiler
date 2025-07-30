# 📊 Data Profiler

**Data Profiler** is a Python-based CLI tool that:
- Loads a CSV file
- Cleans the dataset (removes duplicates, fills missing values, normalizes cases, strips whitespace, parses dates)
- Generates automated EDA reports using Sweetviz
- Saves a Markdown summary report

---

## 🚀 Features

- Load dataset from a provided CSV path
- Clean and normalize the data:
  - Remove duplicate rows
  - Handle missing values:
    - Numeric columns → filled with **mean/median**
    - Categorical columns → filled with **mode**
  - Strip leading/trailing whitespaces
  - Normalize text to lowercase
  - Convert date-like columns to datetime format
- Visualize data using **Sweetviz**
- Save summary insights to `dataset_summary.md`

---
