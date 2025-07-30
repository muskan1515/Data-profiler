import pandas as pd

def loadDataset(filePath):
    try:
        df = pd.read_csv(filePath)
        return df
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except pd.errors.ParserError:
        print("❌ Could not parse the file. Is it a proper CSV?")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
