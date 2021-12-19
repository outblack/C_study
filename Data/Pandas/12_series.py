#%%
import pandas as pd  

df = pd.read_csv("/Users/jhkim/Desktop/Data//laptops.csv")
print(df)

#%%
# 브랜드 데이터 불러오기
print(df["brand"])

#%%
# 겹치는 데이터 없애기
print(df["brand"].unique())

#%%
# 각 value들의 횟수
print(df['brand'].value_counts())

#%%
# 기본 제공 정보 (요약본)
print(df["brand"].describe())


# %%
