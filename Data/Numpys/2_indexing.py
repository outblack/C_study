# 슬라이싱 방식은 파이썬 리스트와 동일
#%%
import numpy as np

array1 = np.array([12,23,32,11,32,23])
print(array1[3]) # 11
print(array1[[1,2,5]]) # 23,32,23
print(array1[:3])
print(array1[1:5:2]) # 23 11


# %%
