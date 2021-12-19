#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Desktop/Data/iphone.csv",index_col=0)

#%%
a = df.iloc[2,4] # iPhone 8의 Face ID 지원 여부
print(a) # no 출력

#%%
# 여러개 출력
a = df.iloc[[1,3], [1,4]]
print(a)

#%%
# 연속적으로 출력
a = df.iloc[3:,1:4]
print(a)
# %%
