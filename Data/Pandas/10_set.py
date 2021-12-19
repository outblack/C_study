#%%
import pandas as pd  

df = pd.read_csv("/Users/jhkim/Desktop/Data/liverpool.csv",index_col=0)
print(df)

#%%
# column의 이름을 바꾸기 => 새로운 데이터프레임 형성
a = df.rename(columns={"position" : "POSITION"})
print(a)
# 새로운 데이터프레임이 아닌 기존의 데이터 프레임을 바꾸려면 a = df.rename(columns={"position" : "POSITION"}, inplace = True)
# 여러값을 바꾸고 싶으면 a = df.rename(columns={"position" : "POSITION", "born": "BRON"}, inplace = True)

#%%
# index 이름 지어주기
df.index.name = "Player Name"
print(df)

#%%
# 기존의 인덱스 저장하기
a = df.index
df["Player"] = a 
print(df)

#%%
# 인덱스 바꾸기
df.set_index('number', inplace=True)
print(df) # 선수이름이 날라가 버림


# %%
