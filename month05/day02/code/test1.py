import numpy as np
arr=np.arange(20).reshape(4,5)
print(arr)
# 计算每一行的平均值 横向计算
print(arr.sum(axis=1))
# 计算每一列的平均值 纵向计算
print(arr.sum(axis=0))