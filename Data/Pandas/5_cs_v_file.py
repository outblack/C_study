#%%
import pandas as pd  

file = pd.read_csv("/Users/jhkim/Desktop/Data/iphone.csv", index_col=0) # 헤더가 없을 땐 header=None 추가
print(file)

# index_col=0 제품명이 row들의 이름으로 바뀜 (원래는 0,1,2 ...)

# df.loc[row, column]
#%%
# 위치 받아오기 (한 부분만)
iphone_df = file.loc["iPhone 8", "메모리"]
print(iphone_df) # 정상적으로 2GB 출력

#%%
# 위치 받아오기 (모든 column을 가져옴)
iphone_df = file.loc["iPhone X", :] # 클론(:)은 그 row에 해당하는 전체 column을 가져온다는 뜻
# iphone_df = file.loc["iPhone X"]
print(iphone_df) # 클론이 없어도 전체를 받아온다

#%%
# 위치 받아오기 (모든 row들을 가져옴)
iphone_df = file.loc[:,"출시일"]
print(iphone_df)
# %%
iphone_df = file.loc[["iPhone X", "iPhone XS"],"출시일"]
print(iphone_df)
# %%
