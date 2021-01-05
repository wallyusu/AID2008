"""
    编程三大范式：
        面向过程：考虑软件问题从步骤出（具体/细节/实现）出发
            数据 + 算法
        面向对象：考虑软件问题从对象角度（谁？干嘛？）出发
            数据 + 交互
        函数式编程：传递函数解决问题（参数/返回值）
            如果参数是可迭代对象，意味着传递数据（灵活的）
            如果参数是函数，意味着传递逻辑（灵活的）
            def 通用功能（可迭代对象,函数）

    函数式编程
        函数作为参数
            def 功能1():
                通用代码
                变化点1

            ded 功能2():
                通用代码
                变化点2

        函数作为返回值

            def 通用代码(参数):
                # 变化点1()
                参数()

            通用代码(变化点1)
            通用代码(lambda)

        函数作为返回值
"""

""" 
    可迭代对象工具类：
        教学角度：深入内置高阶函数原理，学习函数式变成思想
        实用角度：功能更全面，将来在变成生活中还可以不断增加
        面试角度：基于微软公司linq框架思想演变而来
                集成操作框架
                1.根据需求，写出函数
                2.因为主题逻辑相同，核心算法不同。
                  所以实用函数式变成思想（分、隔、做）
                3.创建通用函数，并存入common包的iterable_tools模块的IterableHelper中。
                    
"""
"""
练习：
    1. 在商品列表，获取所有名称与单价
    2. 在商品列表中，获取所有单价小于10000的商品
    3. 对商品列表，根据单价进行降序排列
    4. ([1,1],[2,2,2],[3,3,3])
       获取元组中长度最大的列表
"""
class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
# 1. 在商品列表，获取所有名称与单价
# for i in map(lambda item:(item.name,item.price),list_commodity_infos):
#     print(i)
# 2. 在商品列表中，获取所有单价小于10000的商品
# for i in filter(lambda item:item.price < 10000,list_commodity_infos):
#     print(i.__dict__)
# 3. 对商品列表，根据单价进行降序排列
# for i in sorted(list_commodity_infos,key=lambda item:item.price,reverse=True):
#     print(i.__dict__)
# 4. ([1,1],[2,2,2],[3,3,3])
#        获取元组中长度最大的列表
# re = max(([1,1],[2,2,2],[3,3,3,3]),key=lambda item:len(item))
# print(re)

"""
    排列组合
        全排列（笛卡尔积）
        生成器 = itertools.product(多个可迭代对象)
"""
list01 = ['香蕉','苹果','桔子']
list02 = ['咖啡','牛奶','雪碧','可乐']
list03 = [['香蕉','苹果','桔子'],['咖啡','牛奶','雪碧','可乐']]
import itertools
# list_result = list(itertools.product(list01,list02))
# print(list_result)

# list_result = list(itertools.product(*list03))
# print(list_result)

"""
    使用全排列
        两个色子range(1,7)能掷出多少数字组合
        三个色子range(1,7)能掷出多少种数字组合
"""

# list_result = list(itertools.product(range(1,7),repeat=3))
# print(len(list_result))

"""
    排列 
        从N个元素中去除M个元素,并按照顺序进行排列。     
        n! / (n-m)!
        语法：
        生成器 = itertools.permutations(可迭代对象,数量) 
"""
# 练习：得知某人设置密码的所有字符"abcdefghi0123"    密码为6位
# key = "abcdefghi0"
# # list_key = list(key)
# list_result = list(itertools.permutations(key,6))
# print(len(list_result))

"""
    组合
        从n个元素中取出m个元素。
        不考虑m个元素顺序
        语法：
            生成器 = itertools.combinations(可迭代对象,数字)
            
"""
# 练习：在5张扑克牌中，不考虑顺序抽出3张，有多少可能。
# list_poke = list(itertools.combinations(range(5),3))
# print(len(list_poke))