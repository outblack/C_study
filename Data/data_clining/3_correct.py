#%%
import pandas as pd  
df = pd.read_csv("/Users/jhkim/Downloads/beer.csv", index_col=0)
df
# %%
# 알콜 도수 데이터 박스 플롯 그리기
df.plot(kind="box", y="abv")
# %%
# 25% 지점을 알아보기
df.describe()
# %%
q1 = df["abv"].quantile(0.25)
q3 = df["abv"].quantile(0.75)
iqr = q3 - q1
# %%
# 이상점 찾기 공식
condition = (df["abv"] < q1 - 1.5 * iqr) | (df["abv"] > q3 + 1.5 * iqr)
# %%
df[condition] # 이상점 3개가 나옴
# %%
# 위의 데이터 문제점은 1번과 2번은 맥주가 아닌 소주와 보드카임 그리고 3번째는 도수 잘못 입력
# 3번째 것이 맥주는 맞고 도수만 틀리게 작성임으로 도수만 바꿔준다
df.loc[2250,"abv"] = 0.055
df.loc[2250]
# %%
condition = (df["abv"] < q1 - 1.5 * iqr) | (df["abv"] > q3 + 1.5 * iqr)
df[condition]
# %%
df[condition].index
# %%
df.drop(df[condition].index, inplace=True)

# %%
# 이상점 제거
condition = (df["abv"] < q1 - 1.5 * iqr) | (df["abv"] > q3 + 1.5 * iqr)
df[condition]
# %%
df.plot(kind="box", y="abv")
# %%
