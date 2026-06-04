
# series = A pandas 1-D labeled arry that can hold any data type 
# Think of it like a single column in a spreadsheet(1-D)


import pandas as pd

data = [100, 55, 904]

series = pd.Series(data, index=["a", "b", "c"])

print(series)
