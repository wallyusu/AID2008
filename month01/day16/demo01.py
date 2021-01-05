"""
    创建技能类
        实力变量：技能名称   攻击力    法力
                        0--100    0--50
    要求：如果攻击力或者法力超过范围（构建对象的过程失败）
        则在终端中重新打印（重新构建）
"""


class Skill:
    def __init__(self, atk=0, ace=0):
        self.atk = atk
        self.ace = ace

    def __str__(self):
        return f'攻击力为{self.atk},法力值为{self.ace}'

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 < value < 100:
            self.__atk = value
        else:
            raise Exception('攻击力超范围')

    @property
    def ace(self):
        return self.__ace

    @ace.setter
    def ace(self, value):
        if 0 < value < 50:
            self.__ace = value
        else:
            raise Exception('法力超范围')


# while True:
#     try:
#         atk01 = int(input('请输入攻击力: '))
#         ace01 = int(input('请输入法力值： '))
#         skill = Skill(atk01,ace01)
#         print(skill)
#         break
#     except Exception as e:
#         print(e.args)

"""
    迭代
        迭代Iteration:每次获取下一个元素的过程
        迭代器iterator：执行迭代过程的对象
                具有__next__函数
        可迭代对象iterable：可以被迭代的对象
                具有__iter__函数
"""
#  面试题：
#  能够参与for循环的条件是什么？
#  对象具有__iter__函数、因为对象可以获取迭代器对象，只有获取迭代器，才能获取下一个元素。

"""
练习1：创建列表,使用迭代思想,打印每个元素.
练习2：创建字典,使用迭代思想,打印每个键值对.
"""

# list_message = ['我','是','孙','悟','空']
# iterator = list_message.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#
#     except StopIteration:
#         break

# item = iterator.__next__()
# print(item)
# item = iterator.__next__()
# print(item)

# 面试题：不使用for循环，获取字典中所有键值对。
# dict_message = {1:'我',2:'是',3:'徐'}
# iterator = dict_message.__iter__()
# while True:
#     try:
#         item = iterator.__next__() # item为获取的键
#         print(item,dict_message[item]) # 获取键item和值dict_message[item]
#
#     except StopIteration:
#         break

'''
    自定义迭代器
        需求：for 自定义需求
'''
"""
练习1：遍历商品控制器
class CommodityController:
		pass
controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)
"""
# class CommodityIterator: # 技能迭代器
#     def __init__(self, data):
#         self.__data = data
#         self.__index = -1
#
#     def __next__(self):
#         # 如果索引是最大的或者超过了，则停止迭代
#         if self.__index >= len(self.__data) - 1:
#             raise StopIteration()
#         self.__index += 1
#         return self.__data[self.__index]
#
#
# class CommodityController: # 技能可迭代对象
#     def __init__(self):
#         self.__controller = []
#
#     def add_commodity(self, commodity):
#         self.__controller.append(commodity)
#
#     def __iter__(self):
#         return CommodityIterator(self.__controller)
#
#
# controller = CommodityController()
# controller.add_commodity("屠龙刀")
# controller.add_commodity("倚天剑")
# controller.add_commodity("芭比娃娃")
#
# for item in controller:
#     print(item)
#
# iterator = controller.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)  #
#     except StopIteration:
#         break

"""
练习2：遍历图形控制器
class GraphicController:
		pass
controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic ("三角形")

for item in controller:
print(item)
"""
# class GraphicIterator:
#     def __init__(self, data):
#         self.__data = data
#         self.__index = -1
#     def __next__(self):
#         if self.__index >= len(self.__data)-1:
#             raise StopIteration()
#         self.__index += 1
#         return self.__data[self.__index]
#
# class GraphicController:
#     def __init__(self):
#         self.controller = []
#
#     def add_graphic(self,graphic):
#         self.controller.append(graphic)
#
#     def __iter__(self):
#         return GraphicIterator(self.controller)
#
# graphic = GraphicController()
# graphic.add_graphic('圆形')
# graphic.add_graphic('矩形')
# graphic.add_graphic('三角形')

# for item in graphic:
#     print(item)

# iterator = graphic.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break

"""
    练习3.创建自定义range类，实现下列功能：
    class MyRange:
        pass
        
    for number in MyRange(5):
        print(number) # 0 1 2 3 4
    
"""


# class MyRangeIterator:
#     def __init__(self, data):
#         self.__data = data
#         self.__index = -1
#
#     def __next__(self):
#         if self.__index >= self.__data - 1:
#             raise StopIteration()
#         self.__index += 1
#         return self.__index
#
#
# class MyRange:
#     def __init__(self, value):
#         self.value = value
#
#     def __iter__(self):
#         return MyRangeIterator(self.value)
#
#
# for number in MyRange(5):
#     print(number)  # 0 1 2 3 4

"""
    练习1,：修改商品管理器
"""
class CommodityController: # 技能可迭代对象
    def __init__(self):
        self.__controller = []

    def add_commodity(self, commodity):
        self.__controller.append(commodity)

    def __iter__(self):
        for item in self.__controller:
            yield item


controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

# for item in controller:
#     print(item)

# iterator = controller.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)  #
#     except StopIteration:
#         break

"""
生成器应用：
    
"""
"""
练习1,定义函数，在列表中找出所有偶数
list = [43,43,54,56,76,87,98]
"""
# list01 = [43,43,54,56,76,87,98]
# def even_number():
#     for number in list01:
#         if number % 2 == 0:
#             yield number
#
# data = even_number()
# for item in data:
#     print(item)

"""
练习2,定义函数，在列表中找出所有数字
    list02 = [43,'悟空',True,56,'八戒',87.5,98]
"""
# list02 = [43,'悟空',True,56,'八戒',87.5,98]
# def int_number():
#     for number in list02:
#         if type(number) == int or type(number) == float:
#             yield number
#
# data01 = int_number()
# for i in data01:
#     print(i)
"""
    获取索引和元素
"""
# list01 = [89,45,54,65,6,7,89]
# for i,item in enumerate(list01):
#     print(i,item)

# 需求：将列表中大于10的数字设置为10
# for i,item in enumerate(list01):
#     if item > 10:
#         list01[i] = 10
# print(list01)

"""
练习1：将列表中所有奇数设置为None
练习2：将列表中所有偶数自增1
"""
# list01 = [89,45,54,65,6,7,89]
# for i,item in enumerate(list01):
#     if item % 2: # bool 判断有值
#         list01[i] = None
# print(list01)

# for i,item in enumerate(list01):
#     if item % 2 == 0:
#         list01[i] += 1
# print(list01)

# dict_number = {1:'我',2:'是',3:'许'}
# for i, number in enumerate(dict_number):
#     print(number,dict_number[number])

"""
练习：使用学生列表封装以下三个列表中数据 
list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]
list_student_sex = ["男", "男", "女"]
"""
list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]
list_student_sex = ["男", "男", "女"]

# for item in zip(list_student_name,list_student_age,list_student_sex):
#     print(item)

# class Student:
#     def __init__(self, name='', age=0, sex=0):
#         self.name = name
#         self.age = age
#         self.sex = sex
# list_stu = [Student(*item) for item in zip(list_student_name,list_student_age,list_student_sex)]
# print(list_stu)

# list_stu01 = []
# for item in zip(list_student_name,list_student_age,list_student_sex):
#     stu = Student(*item)
#     list_stu01.append(stu)
# print(list_stu01)
