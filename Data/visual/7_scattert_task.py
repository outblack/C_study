#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/world_indexes.csv")
df
# %%
# 기대수명과 인터넷 사용자 비용 상관관계
df.plot(kind="scatter", x="Life expectancy at birth- years", y="Internet users percentage of population 2014")
# %%
# 숲면적 비율과 탄소배출 증가율 상관관계
df.plot(kind="scatter", x="Forest area percentage of total land area 2012", y="Carbon dioxide emissionsAverage annual growth")
# %%
# 인터넷 사용자 비율과 숲 면적 비율의 상관관계
df.plot(kind="scatter", x="Internet users percentage of population 2014", y="Forest area percentage of total land area 2012")
# %%
# 기대수명과 탄소배출 증가율
df.plot(kind="scatter", x="Life expectancy at birth- years", y="Carbon dioxide emissionsAverage annual growth")
# %%
# 기대수명과 숲면적 비율
df.plot(kind="scatter", x="Life expectancy at birth- years", y="Forest area percentage of total land area 2012")
# %%
