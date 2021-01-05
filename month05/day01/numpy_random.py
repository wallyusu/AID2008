"""
随机数生成
"""
import numpy as np
# 生成一组随机的三行三列符合标准正态分布的数据
# np.random.seed(123)
# print(np.random.randn(3,3))
# 1-100以内生成五行五列随机整数
np.random.seed(123)
print(np.random.random(10))
# print(np.random.randint(1, 100, [5, 5]))
# 0-1之间生成10个随机数
np.random.seed(123)
print(np.random.random(10))
# np.random.seed(123)
print(np.random.random(10))