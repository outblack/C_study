#%%
import numpy
# 1차원 배열
array1 = numpy.array([x for x in range(1,10)])
print(array1)
print(type(array1)) # numpy.ndarray
print(numpy.size(array1)) # 요소개수 9개

#%%
# 2차원 배열
array2 = numpy.array([[x for x in range(1,5)], [x for x in range(12,16)], [123,21,32,54]])
print(array2)
print(type(array2)) # numpy.ndarray
print(numpy.size(array2)) # 요소개수 12개

#%%
# 한가지 값으로 생성 full(몇개, 무슨숫자)
array3 = numpy.full(6,7)
print(array3) # 7이 6개

#%%
# 모든 값이 0인 numpy array 생성
array4 = numpy.full(6,0)
array5 = numpy.zeros(6,dtype=int)
print(array4)
print(array5)

#%%
# 랜던값으로 생성
array6 = numpy.random.random(6)
array7 = numpy.random.random(6)
print(array6)
print(array7)

#%%
# 연속한 값들이 담긴 numpy array 
# 파라미터 1개
array8 = numpy.arange(6)
print(array8) # [0,1,2,3,4,5]

#%%
# 파마리터 2개
array8 = numpy.arange(2,7)
print(array8) # [2,3,4,5,6]

#%%
# 파라미터 3개
array8 = numpy.arange(3,17,3)
print(array8) # [3,6,8,12,15]

