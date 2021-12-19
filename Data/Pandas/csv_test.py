import pandas as pd  

df = pd.read_csv("Pandas/world_cities.csv")


a = df["Country"].value_counts() == 4
print(a[a==True])
