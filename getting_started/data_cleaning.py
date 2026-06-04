# Data cleaning = the process of fixing/removing:
#                 incomlete, incorrect, or irrelevant data.
#                 amlost 75% of work done with pandas is data cleaning.

import pandas as pd
df = pd.read_csv(r'C:\Users\asus\Desktop\pandas_pro\getting_started\sampled.csv')

# 1.Drop irrelevent columns
# df = df.drop(columns = ["Date", "Time"])


# 2.Handle missing values
# df = df.dropna(subset=["Time"])

# 3.Fix incorrect data
# df.Location[df.Location == "Albuqueque"]

# 4. Remove duplicates
# df = df.drop_duplicates()


print(df.to_string())