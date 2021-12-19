#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/laptops.csv", index_col=0)
df
# %%
# 각 os별 가격을 알고 싶다면
sns.catplot(data=df, x="os", y="price", kind="box")
# 리눅스 노트북들이 비교적 저렴
# %%
sns.catplot(data=df, x="os", y="price", kind="violin")
# %%
sns.catplot(data=df, x="os", y="price", kind="strip")
# %%
# 어떤 프로세서들이 있을까?
df["processor_brand"].unique()
sns.catplot(data=df, x="os", y="price", kind="strip", hue="processor_brand")
# %%
# 위의 데이터가 보기 불편함
sns.catplot(data=df, x="os", y="price", kind="swarm", hue="processor_brand")
# %%
