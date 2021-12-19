#%%
import pandas as pd  
import seaborn as sns
df = pd.read_csv("/Users/jhkim/Downloads/young_survey.csv")
df
# %%
# 기본정보는 마지막 7개의 colums에 존재한다
basic_info = df.iloc[:,140:]
basic_info
# %%
basic_info.describe()
# 숫자로 된 통계만을 보여줌
# %%
# 직접 데이터 정보를 알아보기
basic_info["Gender"].value_counts()
# 여성이 남성보다 많다는 것을 알 수 있음
# %%
basic_info["Handedness"].value_counts()
# 참여자중 오른손 잡이가 더 많다는 사실을 알 수 있음
# %%
# 참가자들의 최종 학력
basic_info["Education"].value_counts()
# 대학생들이 많기 때문에 대졸자는 적다
# %%
sns.violinplot(data=df, y="Age")
# %%
sns.violinplot(data=df, x="Gender", y="Age")
# 남녀 상관없이 둘이 나이대는 비슷하다
# %%
sns.violinplot(data=df, x="Gender", y="Age", hue="Handedness")
# %%
sns.jointplot(data=df, x="Height", y="Weight")
# 키 몸무게의 scatter값도 나오고 히스토그램도 나옴
# %%
