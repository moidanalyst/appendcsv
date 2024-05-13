import os
import pandas as pd

folder_path = r"D:\OneDrive_Data\OneDrive\csv" # Your File Path Here
fileslist = os.listdir(folder_path)

# Create an empty list and append all data frames into it
dfs = []

for index, files in enumerate(fileslist):
    filepath = str(folder_path + "\\" + fileslist[index])
    df = pd.read_csv(filepath)
    df.rename(columns={'Unnamed: 0': ''}, inplace=True)
    dfs.append(df)

# Combine all dataframes in the list in one dataframe and generate excel file
combined_df = pd.concat(dfs, ignore_index=True)
combined_df.to_excel("data.xlsx")
