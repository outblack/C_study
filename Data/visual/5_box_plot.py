#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/exam.csv")
df
# 박스 맨 끝에 달린 동그라미 점들은 이상점으로 분석에 도움이 안되는 데이터임
# %%
# 수학점수를 보고 싶다면
df.plot(kind="box", y="math score")
# %%
# 여러개 박스를 보고 싶다면
df.plot(kind="box", y=["math score", "reading score", "writing score"])
# %%
