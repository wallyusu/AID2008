"""
跨类调用
    class 类名1：
        def __init__(self,参数):
            self.数据1 = 参数

        def 方法名1(self):
            对象名 = 类名2(实参)
            对象名.方法名2()

    class 类名2：
        def __init__(self,参数):
            self.数据2 = 参数

        def 方法名2(self):
            self.数据2
    类名(实参)

"""
"""
    内置可重写函数
        __str__
    体会：
        多台(重写) -- 彰显子类的个性
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    # 对象 --> 字符串
    def __str__(self):
        return "%s的编号是%d,单价是%d" % (self.name, self.cid, self.price)


class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    # 对象 --> 字符串
    def __str__(self):
        return f"{self.name}的攻击力是{self.atk},血量是{self.hp}"


# 调用
# qb = Commodity(9001,'铅笔',3)
# lx = Enemy('老徐',10000,999)
# print(qb)
# print(lx)
"""
    运用算数运算符练习：
"""


class Count:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Count(x, y)

    def __str__(self):
        return f'x的分量是{self.x},y的分量是{self.y}'


# post01 = Count(5, 9)
# post02 = Count(3, 6)
# print(post01 - post02)

class Count:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __str__(self):
        return f'x的分量是{self.x},y的分量是{self.y}'


# post01 = Count(5, 9)
# post02 = Count(3, 6)
# post01 *= post02
# print(post01)


# class Employee:
#     def __init__(self, eid, did, name, money):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#     def __eq__(self, other):
#         return self.did == other.did
#
#     def __lt__(self, other):
#         return self.money < other.money


# class Department:
#     def __init__(self, did, title):
#         self.did = did
#         self.title = title

    # def __eq__(self, other):
    #     return self.did == other.did
    #
    # def __lt__(self, other):
    #     return self.money < other.money


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    # def __gt__(self, other):
    #     return self.money > self.money
    # 比较是否相同的判断标准
    def __eq__(self, other):
        return self.name == other.name
    # 比较是否大小的判断标准，从小到大排序
    def __lt__(self, other):
        return self.money < other.money

# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# 部门列表
# list_departments = [
#     Department(9001, "教学部"),
#     Department(9002, "销售部")
# ]
# 取最大值
# max_emp = max(list_employees)
# print(max_emp.__dict__)
# 从小到大排序
# list_employees.sort()
# print(list_employees)
#寻找字段name在列表第几个索引
# target = Employee(1003, 9002, "猪八戒", 20000)
# print(list_employees.index(target))
"""
练习1：以面向对象思想，描述下列情景：
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
"""
class Thunder:
    def __init__(self,name):
        self.name = name


    def bomb(self,damage):
        print(self.name,'爆炸')
        damage.be_injured()

class Target:
    def be_injured(self):
        pass

class Player:
    def be_injured(self):
        print('碎屏')

class Building(Target):
    def be_injured(self):
        print('着火')

# class Tree:
# grenade = Thunder('手雷')
# build = Building()
# player = Player()
# grenade.bomb(player)
"""
    多态
        语法
            class 爸爸:
                def 功能():
                    pass
                    
            class 儿子1(爸爸)：
                #2.子重写
                def 功能():
                    ....
                    
            def 客户端代码(爸爸类型的参数):
                # 1.调用父
                爸爸类型的参数.功能()
            # 创建子
            客户端代码(儿子1())          
"""
