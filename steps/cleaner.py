import pandas as pd

def cleanDataset(df):
    print("📊 Original Dataset Shape:", df.shape)

    #1. Strip leading and trailing spaces from all the string columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    #2. turns all the string into lowercase
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.lower()
    
    #3. Drop duplicate rows
    initial_rows = df.shape[0]
    df = df.drop_duplicates()
    print(f"🧹 Dropped {initial_rows - df.shape[0]} duplicate rows.")

    #4. remove all the null values
    null_summary = df.isnull().sum()
    print("\n🕳️ Null values before cleaning:\n", null_summary[null_summary > 0])
    for col in df.columns:
        
        if df[col].dtype == 'object':
            if df[col].isnull().sum() > 0:
                mode_value = df[col].mode()
                if not mode_value.empty:
                    df[col] = mode_value[0] # as can return multiple

        else:
            if df[col].isnull().sum() > 0:
                median_val = df[col].median()
                df[col] = df[col].fillna(median_val)

    print("\n✅ Null values after cleaning:\n", df.isnull().sum().sum(), "nulls remaining.")

    #5. auto-detect dates and convert
    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except:
                pass

    print("\n📦 Cleaned Dataset Shape:", df.shape)
    print(df.head(2))
    return df