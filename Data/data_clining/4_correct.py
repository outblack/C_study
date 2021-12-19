#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/exam_outlier.csv")
df
# %%
# 읽기점수와 쓰기점수의 연관성을 알아보기 위함
df.plot(kind="scatter", x="reading score", y="writing score")
# %%
df.corr()
# %%
# 맨위에 있는 확실한 이상점 찾기
df[df["writing score"] > 100]
# %%
# 맨위에 있는 확실한 이상점 제거
df.drop(51, inplace=True)
# %%
# 다시 산점도 살펴보기
df.plot(kind="scatter", x="reading score", y="writing score")
# %%
df.corr()
# %%
# 또 하나의 이상점 제거를 위함
# 읽기점수 40이하 쓰기 점수 90이상
condition = (df["writing score"] > 90) & (df["reading score"] < 40)
df[condition]
# %%
df.drop(373, inplace=True)

# %%
df.plot(kind="scatter", x="reading score", y="writing score")
# %%
