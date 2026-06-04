# SELECTION BY COLUMN

import pandas as pd

df = pd.read_json(r'C:\Users\asus\Desktop\pandas_pro\json.txt') 

print(df[["model", "hp"]])

