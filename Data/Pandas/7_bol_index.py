#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Desktop/Data/iphone.csv",index_col=0)

#%%
# row를 조건 인덱싱
a = df.loc[[True,False,True,True,False,True,False]]
print(a) # iphone 7,8,8 plus,xs만 출력됨 True값들

#%%
# column을 조건 인덱싱
a = df.loc[:,[True,False,True,False,False]]
print(a) # 출시일과 메모리만 출력

#%%
# 디스플레이가 5보다 큰 애들만 출력
a = df.loc[df["디스플레이"] > 5]
print(a)

#%%
# Face ID가 되는 애들만 출력하고 싶다면
a = df.loc[df["Face ID"] == 'Yes']
print(a)

#%%
# 디스플레이가 5보다 크고 Face id가 되는 제품을 찾을려면?
condition = (df["디스플레이"]>5) & (df["Face ID"] == "Yes") # 둘중 하나의 조건만 하고 싶으면 |
a = df.loc[condition]
print(a)



# %%
