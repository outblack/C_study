#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/young_survey.csv")
df
# %%
interence = df.loc[:, "History":"Pets"]
interence
# %%
corr = interence.corr()
corr 
# %%
interence.corr()["History"].sort_values(ascending=False)
# %%
sns.clustermap(corr)
# %%
