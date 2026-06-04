# Data Cleaning is the process of refining the data by eliminating thee errors and
# making the data more raliable and readable

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\asus\Desktop\Data_cleacess\tested.csv")

# TO remove duplicates data
df = df.drop_duplicates()

# TO drop columns
df = df.drop(columns = "Not_useful_columns")

# TO take out values/data
df["Last_Name"] = df["Last_Name"].str.lstrip("...")
# Add anything after lstrip in("") to get rid of the unnecessary data

# TO replace something
df["Phone_number"] = df["Phone_number"].str.replace('[a-ZA-Z0-9]', '')

# To replace or to insert same thing at once use [lambda]
df["Phone_number"] = df['Phone_number'].apply(lambda x: x[0:3] + '-' + x:x[3:6] + '-' + x[6:10])
 
# To split a column into sub columns [split]
df[["x_Adress", "y", "z"]] = df["Adress"].str.split(',' , 1, expand=True)
# (x,y,z) are made into seperate columns from a single (adress) column

# To fill values
df = df.fillna('')

# To drop null values
df = df.dropna(subset="Phone_Number", inplace=True)



print(df.to_string())