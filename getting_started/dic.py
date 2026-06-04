import pandas as pd

calories = {"Day 1": 1804, "Day 2": 2053, "Day 3": 2100}

series = pd.Series(calories)

print(series)

# For specific data only
print(series.loc["Day 1"])

print(series[series >2000])