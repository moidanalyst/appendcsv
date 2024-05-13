#!/usr/bin/env python
# coding: utf-8

# In[7]:

import os
import pandas as pd

# In[8]:

folder_path = r"D:\OneDrive_Data\OneDrive - The Citizens Foundation\Desktop\February 2024\Subsidy\csv"
fileslist = os.listdir(folder_path)

# In[9]:

dfs = []

for index, files in enumerate(fileslist):
    filepath = str(folder_path + "\\" + fileslist[index])
    df = pd.read_csv(filepath)
    df.rename(columns={'Unnamed: 0': ''}, inplace=True)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

# In[10]:

combined_df[combined_df["Account Description"] == "B1. Sub Total"]

# In[11]:

combined_df

# In[12]:

combined_df = combined_df[combined_df["Account Description"] != "B1. Sub Total"]

# In[13]:

combined_df

# In[14]:

combined_df.to_excel("subsidydata.xlsx")




