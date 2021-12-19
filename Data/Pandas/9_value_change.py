#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Desktop/Data/iphone.csv",index_col=0)

#%%
a = df.loc["iPhone 8", "메모리"]
print(a) # 2gb출력

#%%
# 값을 변경하기
df.loc["iPhone 8","메모리"] = "2.5GB" 
print(df.loc["iPhone 8", "메모리"]) # 2GB에서 2.5GB로 변경됨

#%%
# row데이터를 한번에 바꾸기
print(df)
df.loc["iPhone 8"] = ["2016-09-22", "4.7", "2GB", "ios 11.0", "No"]
print(df)

#%%
# 여러개의 column을 바꾸기
df.loc[:,["디스플레이", "Face ID"]] = "X"
print(df)

# 앞에서 했던 슬라이싱에다가 값을 지정하면 값을 바꿀 수 있다

#%%
# 값을 추가하기
df.loc["iPhone XR"] = ["2018-10-26", "6.1", "3GB", "ios 12.01", "Yes"]
print(df)

#%%
df.loc[:,"제조사"] = "Apple"
print(df)

#%%
# 값을 제거하기
df.drop("iPhone XR", axis="index", inplace=True)
print(df)

#%%
df.drop("제조사", axis="columns", inplace=True)
print(df)

#%%
# 여러값을 제거하기
df.drop(["iPhone XS", "iPhone X"], axis="index", inplace=True)
print(df)