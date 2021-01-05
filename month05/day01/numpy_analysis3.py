import numpy as np

# 直接排序
# data = np.array([2, 5, 6, 9, 1, 3, 4])
# data.sort()
# print(sorted(data))
# print(data)
# 间接排序
# data_sort = data.argsort()  # 使用索引进行排序
# print(data_sort)
# 创建二维数组
# data2 = np.array([[1, 5, 2, 7], [4, 8, 3, 6], [7, 8, 11, 10]])
# 横向排序
# data2.sort(axis=1)
# 纵向排序
# data2.sort(axis=0)
# print(data2)

# 使用numpy进行基础统计分析
arr=np.arange(20).reshape(4,5)
# print(arr)
# 计算数组总和
print(np.sum(arr))
# 计算每一行的平均值
# print(arr.mean(axis=1))
# 计算每一列的平均值
# print(arr.mean(axis=0))
# 计算整组数据标准差
# print(arr.std())
# 计算数据累积和
# data = np.cumsum(arr,axis=0)
# print(data)
# # 计算数据累计积
# data2 = np.cumprod(arr,axis=0)
# print(data2)