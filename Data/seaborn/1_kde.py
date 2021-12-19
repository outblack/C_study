#%%
# 특정하지 않은 무한한 데이터를 매끄럽게 바꿔줌
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/body.csv", index_col=0)
df
# %%
# 키 그래프 원래
df["Height"].value_counts().sort_index().plot()
# %%
# KDE사용
sns.kdeplot(df["Height"])
# 부드러운 곡선이 나옴
# %%
# 추측 정도를 정해줄 수 있음
sns.kdeplot(df["Height"], bw=0.05)
# %%
