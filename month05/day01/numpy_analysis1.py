import numpy as np
# 创建一维数组
# arr=np.arange(10)
# print(arr)
# # 访问单个值
# print(arr[-1])
# print(arr[3])
# # 访问范围
# print(arr[2:8:2])
# print(arr[8:2:-2])
# # 数组的修改
# arr[2:4] = 12,11
# print(arr)

# 二维数组的访问
arr2 = np.arange(12).reshape(3,4)
# print(arr2)
# print(arr2[0:2,1:3])
# 按照行的条件选择数据
print(arr2[0:2])
# 按照列选择数据
print(arr2[:,1:3])
