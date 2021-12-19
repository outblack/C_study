#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/attendance.csv")
df
# %%
# 결측값이 있는 위치만 True
df.isnull()
# %%
df.isnull().sum()
# %%
# 결측값이 있는 해를 없애버림
df.dropna() # 기존 데이터프레임을 건들지 않음 inplace=True를 안에 넣어 줘야함
# %%
# 결측값이 있는 column을 다 지워버림
df.dropna(axis="columns") # 배구 사라짐
# %%
# 결측값이 있는 부분을 0으로
df.fillna(0)
# %%
# 결측값이 있는 부분을 평균값으로
df.fillna(df.mean())
# %%
# 결측값이 있는 부분을 중간값으로
df.fillna(df.median())
# %%
