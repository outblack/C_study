#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/body.csv", index_col=0)
df
# %%
# 기본 범위는 10개로 설정됨
df.plot(kind="hist", y="Height")
# %%
# 범위를 15개로 하고 싶다면
df.plot(kind="hist", y="Height", bins=15)
# %%
