import pandas as pd
from datetime import date
df = pd.DataFrame(date, index = ["no_1", "no_2", "no_3"])

# identify duplicates
print(df.duplicated().sum())

# Remove duplicates
df_no_duplicates = df.drop_duplicates
