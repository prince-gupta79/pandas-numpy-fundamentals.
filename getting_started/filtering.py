import pandas as pd

df = pd.read_json(r'C:\Users\asus\Desktop\pandas_pro\json.txt') 

filtered_df = df[df["qsec"] > 20]

print(filtered_df)

# FILTERING ROWS BASED ON A CONDITION 