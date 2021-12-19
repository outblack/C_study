#%%
import pandas as pd  
# DataFrame 인덱싱

df = pd.read_csv("/Users/jhkim/Desktop/Data/iphone.csv", index_col=0)

#%%
# iPhone X의 값만 들고오기
a = df.loc["iPhone X"]
print(a)

#%%
# iPhone X와 iPhone 8의 값을 들고오기
a = df.loc[["iPhone X", "iPhone 8"]]
print(a) # data type은 Series가 아닌 DataFrame임

#%%
# column정보를 가져오기
a = df.loc[:,"Face ID"]
print(a)

#%%
# 여러개의 column정보 가져오기
a = df.loc[:,["Face ID", "출시일", "메모리"]]
print(a)

#%%
# row데이터 슬라이싱
a = df.loc["iPhone 8":"iPhone XS"]
print(a)

# 이후 슬라이싱은 일반 리스트 슬라이싱이나 넘파이 슬라이싱과 동일함
# %%
