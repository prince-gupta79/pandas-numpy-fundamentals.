

import pandas as pd

df = pd.read_csv(r'C:\Users\asus\Desktop\pandas_pro\advanced_pandas\tested.csv')

# Option 1: Assign the sorted result to a variable
sorted_df = df.sort_values(by=["PassengerId",  "Name"], ascending=[True, False])
print(sorted_df)

# Option 2: Modify the original DataFrame in place
# df.sort_values(by="PassengerId", ascending=True, inplace=True)
# print(df)