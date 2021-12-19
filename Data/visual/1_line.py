#%%
import pandas as pd   

df = pd.read_csv("/Users/jhkim/Downloads/broadcast.csv", index_col=0)
pd.DataFrame(df)
# %%
# 하나만 골라서 하고 싶다면
df.plot(y="KBS")

# %%
# 두개 이상을 보고 싶다면
df.plot(y=["KBS", "JTBC"])
# %%
# 인덱싱을 plot하기
df[["KBS", "JTBC"]].plot()

# 이 모든 그래프들은 선그래프로써 수치에서만 사용할 수 있다
# %%
