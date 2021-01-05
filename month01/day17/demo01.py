"""
    生成器推导式
"""

"""
练习1：使用生成器表达式在列表中获取所有字符串.
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
练习2：在列表中获取所有整数,并计算它的平方.
"""
# list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
# # generator01 = (item for item in list01 if type(item) == str)
# # for i in generator01:
# #     print(i)
#
# generator02 = (item ** 2 for item in list01 if type(item) == int)
# for i in generator02:
#     print(i)

"""
练习1：
    需求：
        定义函数，在列表中查找奇数
    定义函数，在列表中查找能被3或5整除的数字
    步骤：
            1. 根据需求，写出函数。
            2. 因为主体逻辑相同,核心算法不同.
               所以使用函数式编程思想(分、隔、做)
               创建通用函数find_all 
            3. 在当前模块中调用
"""
"""
    调用common/iterable_tools.py中的静态方法
    查找列表中的所有奇数
    查找列表中各位是4,5的所有数字
"""

# from day17.common.iterable_tools import IterableHelper
# list01 = [43, 16, 5, 69, 6, 7, 89, 9, 20]
# def condition01(item):
#     return item % 2 != 0
#
# def condition02(item):
#     return item % 10 in (4,5)
#
# for item in IterableHelper.find_all(list01,condition02):
#     print(item)
"""
练习2：
需求：
    定义函数，在员工列表中查找编号是1003的员工
    定义函数，在员工列表中查找姓名是孙悟空的员工
"""
# from day17.common.iterable_tools import IterableHelper
#
# class Employee:
#     def __init__(self, eid, did, name, money):
#         self.eid = eid  # 员工编号
#         self.did = did  # 部门编号
#         self.name = name
#         self.money = money
#
# def condition01(item):
#     return item.eid == 1003
#
# list_employees = [
#     Employee(1001, 9002, "师父", 60000),
#     Employee(1002, 9001, "孙悟空", 50000),
#     Employee(1003, 9002, "猪八戒", 20000),
#     Employee(1004, 9001, "沙僧", 30000),
#     Employee(1005, 9001, "小白龙", 15000),
# ]


# def find_single01():
#     for item in list_employees:
#         if item.eid == 1003:
#             return item

# class IterableHelper:
#
#     @staticmethod
#     def find_single(iterable,func_condition):
#         """
#         在可迭代对象中,根据指定条件查找所有元素
#         :param iterable:可迭代对象
#         :param func_condition:函数类型的条件,一个参数,一个bool返回值
#         :return:生成器,负责显示满足条件的数据
#         """
#         for item in iterable:
#             if func_condition(item):
#                 return item



# for item in IterableHelper.find_all(list_employees,condition01):
#     print(item.__dict__)

"""
    lambda  表达式
        匿名函数
"""
# func01 = lambda p1, p2: p1 > p2
#
# print(func01(1,2))
"""
    在员工列表中查询编号为1003的员工
    在员工列表中查询编号为孙悟空的员工
"""
# re = IterableHelper.find_single(list_employees,lambda item:item.eid == 1003)
# print(re.__dict__)
#
# re01 = IterableHelper.find_single(list_employees,lambda item:item.name == '孙悟空'):
# print(re.__dict__)
#
# re02 = IterableHelper.find_single(list_employees,lambda item:item.did == 9001):
# print(re.__dict__)
#
# re03 = IterableHelper.find_single(list_employees,lambda item:item.money < 50000):
# print(re.__dict__)
"""
    定义函数：在员工列表中查找所有员工的姓名
    定义函数，在员工列表中查找所有员工的编号和薪资
"""

class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


# def select(list01):
#     for item in list01:
#         print(item.name)
#
# select(list_employees)

# class IterableHelper:
#
#     @staticmethod
#     def select(list01,func_condiction):
#         for item in list01:
#             yield func_condiction(item)
#
# for item in IterableHelper.select(list_employees,lambda item:(item.eid,item.money)):
#     print(item)

"""
定义函数，在员工列表查找薪资大于20000元的员工数量
定义函数，在员工列表中查找部门编号是9002的数量
"""
# class IterableHelper:
#
#     @staticmethod
#     def get_count(list01,func_condiction):
#         count = 0
#         for item in list01:
#             if func_condiction(item):
#                 count += 1
#         return count

# re = IterableHelper.get_count(list_employees,lambda item:item.money > 20000)
# print(re)

# re = IterableHelper.get_count(list_employees,lambda item:item.did == 9002)
# print(re)

# re = IterableHelper.get_count(list_employees,lambda item:item.did == 9002)
# print(re)
"""
    删除所有大于30000的员工信息
"""
# class IterableHelper:
#
#     @staticmethod
#     def delete_all(list01,func_condiction):
#         for item in range(len(list01)-1,-1,-1):
#             if func_condiction(list01[item]):
#                 del list01[item]
#         return list01
#
# for item in IterableHelper.delete_all(list_employees,lambda item:item.money > 30000):
#     print(item.__dict__)
"""
    获取工资最高的员工
    获取员工编号最大的员工
"""
# class IterableHelper:
#
#     @staticmethod
#     def get_max(iterable, func_handle):
#         max_value = iterable[0]
#         for item in range(1, len(iterable)):
#             if func_handle(max_value) < func_handle(iterable[item]):
#                 max_value = iterable[item]
#         return max_value
#
#
# re = IterableHelper.get_max(list_employees,lambda item:item.money)
# print(re.__dict__)
"""
    根据工资对员工列表员工进行升序排序
    根据部门编号对员工列表进行升序排序
"""
# class IterableHelper:
#
#     @staticmethod
#     def order_by(iterable,func_condition):
#         for r in range(len(iterable) - 1):
#             for c in range(r + 1, len(iterable)):
#                 if func_condition(iterable[r]) > func_condition(iterable[c]):
#                     iterable[r], iterable[c] = iterable[c], iterable[r]
#         return iterable
#
# for i in IterableHelper.order_by(list_employees,lambda item:item.did):
#     print(i.__dict__)
property