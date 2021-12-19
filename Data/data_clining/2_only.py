#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/dust.csv", index_col=0)
df
# %%
# 날짜 받아오기
df.index
# %%
df.index.value_counts()
# %%
df.loc["07월 31일"]
# %%
df.drop_duplicates() # inplace=True 필요
# %%
# row랑 column이 바뀜
df.T
# %%
df.T.drop_duplicates().T
# %%
