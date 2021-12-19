#%%
import pandas as pd  
price = pd.read_csv("/Users/jhkim/Downloads/vegetable_price.csv")
qu = pd.read_csv("/Users/jhkim/Downloads/vegetable_quantity.csv")

price

# %%
qu
# %%
# 2개 데이터 합치기
# inner join
pd.merge(price,qu, on="Product")
# %%
# left outer join
pd.merge(price,qu, on="Product",how="left")
# %%
# right outer join
pd.merge(price,qu, on="Product",how="right")

# %%
# full outer join
pd.merge(price,qu, on="Product",how="outer")
# %%
