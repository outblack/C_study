#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/broadcast.csv", index_col=0)
df
# %%
df.loc[2017].plot(kind="pie")
# %%
