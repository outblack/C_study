#%%
import pandas as pd
import seaborn as sns
df = pd.read_csv('/Users/jhkim/Downloads/exam.csv')

df.corr()
# 상관계수를 데이터 프레임으로 표현
# 상관계수가 1과 가까울수록 연관성이 높고
# 상관계수가 -1과 가까워지면 그 데이터는 연관성이 높지만 서로 반대작용을 함
# %%
# 상관계수를 잘 보이게 하기 위해서 히트맵 사용
sns.heatmap(df.corr())
# 색이 더 밝을 수록 상관계수가 높다
# %%
# 각 지점에 숫자도 같이 표현해줌
sns.heatmap(df.corr(), annot=True)
# %%
