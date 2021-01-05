# 练习使用numpy进行文件读写
# 创建一个数组并保存
import numpy as np

arr = np.arange(100).reshape(10,10)
# print(arr)
# np.save(file='save_arr',arr=arr)
# load_data = np.load('save_arr.npy')
# print(load_data)

# 创建两个数组并保存
arr1 = np.array([1,2,3,4])
np.savez('save_arr',arr,arr1)
load_data2 = np.load('save_arr.npz')
print(load_data2.files)
# 读取第一个数组
print(load_data2['arr_0'])
print(load_data2['arr_1'])