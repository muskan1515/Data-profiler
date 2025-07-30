import sweetviz as sv
import pandas as pd

def profile_dataset(df, target_col=None):
    output_file = '../reports/dynamic_report.html'
    """
    Automatically profiles the dataset with or without a target column using Sweetviz.
    """
    if target_col and target_col in df.columns:
        print(f"🔍 Target column '{target_col}' detected. Performing target-based profiling...")
        report = sv.analyze(df, target_feat=target_col)
    else:
        print("📊 No target column provided or found. Performing general profiling...")
        report = sv.analyze(df)

    report.show_html(output_file)
    print(f"✅ Report saved as {output_file}")
