import argparse 
from steps.loader import loadDataset
from steps.cleaner import cleanDataset
from steps.profiler import profile_dataset
from steps.summarizer import generate_summary_markdown
from utils import guess_target_column

def main():
    parser = argparse.ArgumentParser(description="Data Profiler Tools")
    parser.add_argument("filepath", type=str, help="Enter Path to csv dataset" )

    args = parser.parse_args()

    ##load the csv dataset
    dataset = loadDataset(args.filepath)

    ##clean dataset with null , duplicate values
    cleanedDataFrame = cleanDataset(dataset)

    ##now profilling the dataset
    target_col = guess_target_column(cleanedDataFrame)
    profile_dataset(cleanedDataFrame, target_col)
    print("File saved successfully on your reports/dynamic_report.html form")

    ##summarize with insights and save
    generate_summary_markdown(cleanedDataFrame, target_col)



if __name__ == "__main__" :
    main()