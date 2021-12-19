#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/parks.csv")
df
# %%
# 문자열 분리
df["소재지도로명주소"].str.split()
# %%
# 광역시까지만 분리하기
df["소재지도로명주소"].str.split(n=1)
# %%
# 새로운 데이터프레임 생성
adress = df["소재지도로명주소"].str.split(n=1, expand=True)
adress
# %%
# 광역시 정보를 새로운 데이터 프레임에
df["관할구역"] = adress[0]
df
# %%
