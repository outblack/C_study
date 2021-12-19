#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/exam.csv")
df
# %%
# 수학점수와 읽기점수의 연관성
df.plot(kind="scatter", x="math score", y="reading score")
# 분포를 보아 어느정도는 연관성이 있다
# %%
# 읽기 점수와 쓰기점수의 연관성 
df.plot(kind="scatter", x="reading score", y="writing score")
# 거의 일직선이라서 연관성이 매우 크다고 봄
# %%
