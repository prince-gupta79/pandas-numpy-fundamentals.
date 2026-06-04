import pandas as pd

data = {
    "Name":["muji", "yoyo", "jhonny"],
    "place":["ktm", "simara", "Htd"]
}

df = pd.DataFrame(data, index = ["no_1", "no_2", "no_3"])


#print(df.iloc[2])


#Adding a new column

df["Age"] = [22,25,29]

#Adding a new row

df.loc["no_4"] = ["lol", "amj", 33]


print(df)