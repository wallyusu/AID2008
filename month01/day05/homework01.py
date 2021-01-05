"""
根据列表中的数字,重复生成*.
    list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    效果：
        *
        **
        ***
        ****
        *****
        ****
        ***
        **
        *
"""
# list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# for i in list01:
#     print('*' * i)


"""
将列表中的数字累乘
   list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
   结果：806400
"""
# list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
# num = 1
# for i in list02:
#     num *= i
# print('结果:',num)

"""
 将列表中整数的个位不是5和3的数字存入另外一个列表
   list03 = [25, 63, 27, 75, 70, 83, 27]
   结果:[27, 70, 27]
"""
# 方法1：
# list03 = [25, 63, 27, 75, 70, 83, 27]
# list_new = []
# for i in list03:
#     if i % 10 != 5 and i % 10 != 3:
#         list_new.append(i)
#     else:
#         continue
# print(list_new)
# 方法2：
# list03 = [25, 63, 27, 75, 70, 83, 27]
# list_new = []
# for i in list03:
#     if i % 10 == 5 or i % 10 == 3:
#         continue
#     list_new.append(i)
# print(list_new)

"""
计算列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
    字符串列表：words =["qtx","看一看","想啊想","练练"]
    结果:2
"""
# words =["qtx","看一看","想啊想","练练"]
# num = 0
# for i in words:
#     if len(i) > 2 and i[0] == i[-1]:
#         num += 1
#     else:
#         continue
# print('结果:',num)

"""
在终端中录入疫情地区名称，如果输入空字符串，则停止。
   最后倒序打印所有地区名称(一行一个)
   要求：录入的名称已经存在不要再次添加.
   提示： in
"""

# list_city = []
# while True:
#     city = input('请输入疫情地区名称： ')
#     if city == '':
#         for i in list_city[::-1]:# 切片方法不建议使用，会产生新的垃圾，正确语法：range(len(list_city)-1,-1,-1)
#             print(i)
#         break
#     if city in list_city:
#         continue
#     else:
#         list_city.append(city)

"""
在终端中录入5个疫情省份的确诊人数
   最后打印最大值、最小值、平均值.
   （使用内置函数实现）
"""
# list_people = []
# for i in range(5):
#     city_people = int(input('请输入省份确诊人数： '))
#     list_people.append(city_people)
# print(f'最大确诊人数为：{max(list_people)},最小确诊人数为：{min(list_people)},\n'
#       f'平均值为：{sum(list_people) / len(list_people) }')

"""
 # 画出下列代码内存图
import copy
list01 = [["烤鸭", "豆汁"],["火锅", "兔头"],["麻花", "包子"]]

list02 = list01
list03 = list01[:]
list04 = copy.deepcopy(list01)

list04[0] = ["全聚德", "大董"]
print(list04) # [["全聚德", "大董"],["火锅", "兔头"],["麻花", "包子"]]
print(list01) # [["烤鸭", "豆汁"],["火锅", "兔头"],["麻花", "包子"]]

list03[0][1] = ["全聚德", "大董"]
print(list03) # [["烤鸭", ["全聚德", "大董"]],["火锅", "兔头"],["麻花", "包子"]]
print(list01) # [["烤鸭", ["全聚德", "大董"]],["火锅", "兔头"],["麻花", "包子"]]

# 提示：看看切片原理
list02[0][:] = ["全聚德", "大董"]
print(list02) # [["全聚德", "大董"],["火锅", "兔头"],["麻花", "包子"]]
print(list01) # [["全聚德", "大董"],["火锅", "兔头"],["麻花", "包子"]]
"""

list = [1,2,3,6,5,8]
# print(list[1:-1])
import  numpy as np
arry = np.array(list)
print(arry)
m = np.median(list)
print(m)

import matplotlib