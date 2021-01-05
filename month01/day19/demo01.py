"""
    复习
        内置高阶函数
            优点：知名度高，性能高
            缺点：功能不全
        集成操作框架IterableHelper
            优点：功能不全，便于调试
            缺点：在大量数据中性能较差
        排列：从n个数据中抽出m个数据，按顺序。
        组合：从n个数据中抽出m个数据。
"""
# def func01(a):
#     def func02():
#         nonlocal a
#         a += 1
#         print(a)
#
#     return func02
#
# result = func01(100)
# result()
# result()

"""
练习：使用闭包模拟以下情景：
    在银行开户存入10000
    购买xx商品花了xx元
    购买xx商品花了xx元
"""
# def open_account(money):
#     print(f'在银行存入{money}')
#     def buy(commodity,price):
#         nonlocal money
#         money -= price
#         print(f'购买{commodity}商品花了{price}元,还剩余{money}')
#
#     return buy

# result = open_account(10000)
# result('switch',2000)
# result('马里奥奥德赛',350)
# result('宝可梦剑盾',300)
# result('异度之刃2',450)
# 方法2：
# open_account(10000)('switch',2000)

"""
    装饰器：
        语法
            def 函数装饰器名称(func):
                def wrapper(*args, **kwargs):
                    需要添加的新功能
                    return func(*args, **kwargs)
                return wrapper
"""
"""
练习1：不改变插入函数与删除函数代码，为其增加验证权限的功能
"""
# def verify_permissions(func):
#     def jurisdiction():
#         print("验证权限")
#         func()
#
#     return jurisdiction
#
# @verify_permissions
# def insert():
#     print("插入")
# @verify_permissions
# def delete():
#     print("删除")
#
# insert()
# delete()

# def verify_permissions(func):
#     def jurisdiction(*args,**kwargs):
#         print("验证权限")
#         return func(*args,**kwargs)
#
#     return jurisdiction
#
# @verify_permissions
# def insert(id,name,age):
#     print("插入",id,name,age)
#     return 'ok'
# @verify_permissions
# def delete(id):
#     print("删除",id)
#     return 'no'


# print(insert(1001, '悟空',age=26))
# print(delete(1002))

"""
练习2：为sum_data,增加打印函数执行时间的功能.
        函数执行时间公式： 执行后时间 - 执行前时间
"""
# import time
# def verify_permissions(func):
#     def jurisdiction(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print('函数执行时间是',end_time-start_time)
#         return result
#     return jurisdiction
#
# @verify_permissions
# def sum_data(n):
#     sum_value = 0
#     for number in range(n):
#         sum_value += number
#     return sum_value

# print(sum_data(10))
# print(sum_data(1000000))
# import time
# def all_time():
#     start_time = time.time()
#     end_time = time.localtime(time.time())
#     return start_time,end_time
#
#
# print(all_time())



