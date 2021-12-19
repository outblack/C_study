#%%
import pandas as pd  

df = pd.read_csv("/Users/jhkim/Desktop/Data//laptops.csv")
print(df)

#%%
# 맨앞 3줄만 출력하기
print(df.head(3))

#%%
# 맨뒤 3줄만 출력하기
print(df.tail(3))

#%%
# 데이터 프레임의 크기
print(df.shape) # (167,15)
#%%
# column이 무엇인지 확인
print(df.columns)

#%%
# 정보확인
print(df.info())

#%%
# 각 column에 대하여 통계값
print(df.describe())

#%%
# 가격을 기준으로 정렬

print(df)

#%%
print(df.sort_values(by="price")) # 가격이 작은 순
#%%
print(df.sort_values(by="price", ascending=False)) # 가격이 큰 순
#print(df.sort_values(by="price", ascending=False, inplace=True)) # inplace = True가 있어야 원래 값을 변경
#print(df.index)
# %%
