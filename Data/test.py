#%%
import seaborn as sns  
import pandas as pd  

df = pd.read_csv("/Users/jhkim/Downloads/titanic.csv")
df

# %%
survive = df[["Survived", "Pclass", "Fare"]]
survive
# %%
corr = survive.corr()
corr
# %%
sns.clustermap(corr)
# %%
df
# %%
fee = df[["Age","Fare"]]
fee.sort_index()
# %%
age.value_counts()
# %%
