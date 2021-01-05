import numpy as np
# 定义一个列表
lis1=[1,2,3,4]  #lis1是列表类型
# 定义一个数组
a = np.array([1,2,3,4])  #a是数组类型
# 进行四则运算
print("list",lis1,lis1[0],'\n','array',a,a[0])
print("list+list",lis1+lis1,'\n','array+array',a+a)
# 查看数据类型
print(type(lis1))
print(type(a))