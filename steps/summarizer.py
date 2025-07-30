import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_summary_markdown(df: pd.DataFrame, target_col: str = None, output_file: str = "dataset_summary.md"):
    os.makedirs("summary_plots", exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 📊 Dataset Summary Report\n\n")
        f.write(f"**Total Rows:** {df.shape[0]}\n\n")
        f.write(f"**Total Columns:** {df.shape[1]}\n\n")

        f.write("## 🔎 Column Summary\n\n")
        for col in df.columns:
            f.write(f"### ➤ {col}\n")
            f.write(f"- **Type**: {df[col].dtype}\n")
            f.write(f"- **Missing Values**: {df[col].isnull().sum()} ({(df[col].isnull().mean() * 100):.2f}%)\n")
            f.write(f"- **Unique Values**: {df[col].nunique()}\n")
            
            if df[col].dtype == 'object':
                top_vals = df[col].value_counts().head(3).to_dict()
                f.write(f"- **Top Categories**: {top_vals}\n")
            elif pd.api.types.is_numeric_dtype(df[col]):
                f.write(f"- **Mean**: {df[col].mean():.2f}\n")
                f.write(f"- **Median**: {df[col].median():.2f}\n")
                f.write(f"- **Std Dev**: {df[col].std():.2f}\n")
            else:
                f.write("- Stats not available for non-numeric column.\n")

            f.write("\n")

        # 🎯 Target-specific insights
        if target_col and target_col in df.columns:
            f.write("## 🎯 Target-Based Insights\n\n")
            if df[target_col].dtype == 'object':
                for val in df[target_col].dropna().unique():
                    subset = df[df[target_col] == val]
                    f.write(f"### Target: `{val}`\n")
                    f.write(f"- Rows: {len(subset)}\n")
                    f.write(f"- Avg values of numerical columns:\n")
                    for col in df.select_dtypes(include='number').columns:
                        if col != target_col:
                            f.write(f"  - {col}: {subset[col].mean():.2f}\n")
                    f.write("\n")
            else:
                f.write(f"- **Target is numeric — showing correlations:**\n\n")
                corr = df.corr(numeric_only=True)[target_col].sort_values(ascending=False)
                for feat, val in corr.items():
                    if feat != target_col:
                        f.write(f"  - {feat}: {val:.2f}\n")
                f.write("\n")

        # 📉 Correlation heatmap
        num_df = df.select_dtypes(include='number')
        if not num_df.empty:
            f.write("## 🔥 Correlation Heatmap\n\n")
            heatmap_path = "summary_plots/correlation_heatmap.png"
            plt.figure(figsize=(10, 8))
            sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
            plt.title("Correlation Heatmap")
            plt.tight_layout()
            plt.savefig(heatmap_path)
            plt.close()

            f.write(f"![Correlation Heatmap]({heatmap_path})\n")

        f.write("\n✅ **Report Generated Successfully.**\n")

    print(f"📝 Markdown report saved to: {output_file}")
