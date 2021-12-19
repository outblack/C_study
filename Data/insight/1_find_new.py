#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/broadcast.csv", index_col=0)
df
# %%
# 원본 그래프
df.plot()
# %%
# 한해의 방송사 시청률 모두 더하기
df["Total"] = df.sum(axis="columns")
df
# %%
df["Total"].plot()
# 시청률 해가 갈수록 하락
# %%
# 지상파 시청률
df["Group 1"] = df.loc[:,"KBS":"SBS"].sum(axis="columns")
df
df["Group 1"].plot()
# %%
# 종편 시청률
df["Group 2"] = df.loc[:,"TV CHOSUN":"MBN"].sum(axis="columns")
df
df["Group 2"].plot()
# %%
df.plot(y=["Group 1", "Group 2"])
# %%
