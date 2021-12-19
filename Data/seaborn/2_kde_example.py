#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/body.csv", index_col=0)
df
# %%
# 히스토그램과 Kde를 동시에 표현
df.plot(kind="hist", y="Height", bins=15)
# %%
sns.distplot(df["Height"], bins=15)
# %%
sns.violinplot(y=df["Height"])
# %%
# 등고선 그래프
sns.kdeplot(df["Height"], df["Weight"])
# 선들이 가깝다는 것은 가파르다
# %%
