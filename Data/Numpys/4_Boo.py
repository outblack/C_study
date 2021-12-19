#%%
import numpy as np

array1 = np.array([2,4,12,33,21,31,45,32])
print(array1 > 4)
print(array1 % 2 == 0)

array2 = np.array([True,True,True,False,False,False,False,True])
print(np.where(array2)) # True면 1반환 False면 0 반환

array3 = np.where(array1 > 4)
filter = array3 
print(array3)
print(array1[filter]) # array3에 있는 인덱스 번호를 출력



# %%
