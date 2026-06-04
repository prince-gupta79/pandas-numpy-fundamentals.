from datetime import date
import pandas as pd

df = pd.DataFrame(date, index = ["no_1", "no_2", "no_3"])

# Disp;ay the first few rows of the dataset
print(df.head())

# Summary statistics
print(df.describe())

# INformation about the dataset
print(df.into())

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values and place it in a new variable "df_cleaned"
df_cleaned = df.dropna()

# Fill missing values with mean for numerical data and palce 
# it in a new variable called df_filled
df_filled = df.fillna(df.mean())
