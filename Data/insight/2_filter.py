#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/albums.csv")
df
# %%
# 장르만 모아보기
df["Genre"].unique()
# %%
# blues만 불러오기
df[df["Genre"] == "Blues"]
# 이러면 장르가 딱 블루즈 인것만 나옴
# %%
# blues가 포함된 장르 뺴오기
df[df["Genre"].str.contains("Blues")]
# %%
# 블루즈가 앞에 오는 것만 불러오기
df[df["Genre"].str.startswith("Blues")]
# %%
# blues를 포함하는 앨범이면 True
df["Contains Blues"] = df["Genre"].str.contains("Blues")
df
# %%
