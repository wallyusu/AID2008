import numpy as np
# 读取国民经济季度核算数据

load_data = np.load('国民经济核算季度数据.npz',allow_pickle=True)
print(load_data.files)
# 列名称
print(load_data['columns'])
# 数据
print(load_data['values'])