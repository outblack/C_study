#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/young_survey.csv")
df
# %%
music = df.iloc[:,:19]
music
# 1점부터 5점사이 좋아하는 정도 표현
# %%
# 히트맵 불러오기
sns.heatmap(music.corr())
# 오페라와 힙합은 서로 연관성이 엄청 적음
# %%
# 나이에 대한 연관성만 뽑기
df.corr()["Age"].sort_values(ascending=False)
# %%
