"""
练习1：定义函数,根据年月日,计算星期。
输入：2020   9   15
输出：星期二
"""

import time

# def get_week(year,month,day):
#     result = time.strptime('%d-%d-%d'%(year,month,day),'%Y-%m-%d')
#     week = result[6]
#     list_week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#     print(list_week[week])
#
# get_week(2020,12,1)

"""
练习1：创建列表,使用迭代思想,打印每个元素.
"""
# list_01 = [6,5,8,4,7,4]
# class Num01():
#     def __iter__(self):
#         return generator_01
#
# generator_01 = list_01.__iter__()
# while True:
#     try:
#         print(generator_01.__next__())
#
#     except StopIteration:
#         break
#
# for i in Num01():
#     print(i)

"""
练习2：创建字典,使用迭代思想,打印每个键值对.
"""
#
# dict_01 = {'a':1,'b':2,'c':3,'d':4}
# generator_02 = dict_01.__iter__()
# while True:
#     try:
#         key = generator_02.__next__()
#         print(key,dict_01[key])
#
#     except StopIteration:
#         break

"""
练习1：遍历商品控制器
"""

class CommodityController:
    def add_commodity(self,num):
        dict_01 = []
        dict_01.append(num)

    def __next__(self):
        if not:
            raise StopIteration
        return add_commodity()



controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)