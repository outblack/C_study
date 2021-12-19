#%%
import pandas as pd  
two_dim = [["Alice",50,86], ["Kim",89,31],["Lim",32,11]]

my_gf = pd.DataFrame(two_dim, columns=["name","coding_score","English_score"], index=["a","b","c"])
print(my_gf)

print(my_gf.columns)
print(my_gf.index)
# %%
