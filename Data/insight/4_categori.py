#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/laptops.csv")
df
# %%
# 각 브랜드가 어떤 나라인지 
brand_nation = {
    "Dell": "U.S",
    "Apple": "U.S",
    "Acer": "Taiwan",
    "HP": "U.S",
    "Lenovo": "China",
    "Alienware": "U.S",
    "Microsoft": "U.S",
    "Asus": "Taiwan"
}

df["brand"]
# %%
# 브랜드를 나라이름으로 바꿔줌
nataion_info = df["brand"].map(brand_nation)
nataion_info
# %%
df["nation"] = nataion_info
df
# %%
# groupby
nation_group = df.groupby("nation")
nation_group.count()
# %%
nation_group.mean()
# %%
nation_group.first()
# %%
nation_group.last()
# %%
nation_group.plot(kind="box", y="price")
# %%
nation_group.plot(kind="hist", y="price")
# %%
