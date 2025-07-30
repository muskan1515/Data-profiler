def guess_target_column(df):
    # Common names for target columns
    candidates = ['target', 'label', 'class', 'y', 'output', 'Salary']
    
    for col in df.columns:
        if col.lower() in candidates:
            return col

    # Try numeric or categorical with low unique values
    for col in df.select_dtypes(include=['int', 'float', 'object']).columns:
        if df[col].nunique() < 20:
            return col
    return ''
