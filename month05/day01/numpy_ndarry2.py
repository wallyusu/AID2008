import numpy as np
# 创建特殊数组
# 生成等差数组
a = np.arange(1,10,2)
print(a)
print(type(a))
# 生成全是0的两行三列数组
print(np.zeros((2,3)))
print(np.zeros(10))
# 生成全是1的三行四列的二维数组
print(np.ones((3,4)))