#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/sports.csv", index_col=0)
df
# %%
df.plot(kind="bar")
# %%
# 막대그래프를 가로로 표현
df.plot(kind="barh")
# %%
# 남자데이터와 여자데이타가 쌓여서 보임
df.plot(kind="bar", stacked=True)
# %%
# 여성데이터만 가져오고 싶다면
df["Female"].plot(kind="bar")
# %%
