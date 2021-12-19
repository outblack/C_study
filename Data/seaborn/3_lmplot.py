#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/body.csv", index_col=0)
df
# %%
df.plot(kind="scatter", x="Height", y="Weight")
# %%
# 회귀선
sns.lmplot(data=df, x="Height", y="Weight")
# 키가 170인 학생은 몸무게가 70이라고 예측할 수 있다
# 점들이 대부분 선과 멀어져 있는데 이는 키와 몸무게가 상관관계가 크지 않다는 것을 의미한다
# %%
