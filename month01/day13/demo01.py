"""
    需求
        创建一个员工管理器
            1.存储多个员工
            2.计算所有员工总薪资
"""

"""
练习2：创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.
"""
import sys
import math  # 调用π计算库


# 创建图形管理器
class GraphicsManager:
    def __init__(self):
        self.__all_graph = []

    def add_graph(self, gra):
        if isinstance(gra, Graph):
            self.__all_graph.append(gra)

    def total_area(self):
        total_area = 0
        for gra in self.__all_graph:
            total_area += gra.area()
        return total_area


# 创建父类（图形）
class Graph:
    def area(self):
        pass


# ——————————————————————————————————————————————————————————————————
# 创建子类（圆形,矩形...）
class Round(Graph):
    def __init__(self, r):
        self.r = r

    # 子重写
    def area(self):
        round_area = math.pi * self.r ** 2
        return round_area


class Rectangle(Graph):
    def __init__(self, long, wide):
        self.long = long
        self.wide = wide

    # 子重写
    def area(self):
        rectangle_area = self.long * self.wide
        return rectangle_area


# _______________________________________________________
# 调用
# manager = GraphicsManager()
# round01 = Round(5)
# rectangle01 = Rectangle(6, 5)
# print(round01.area())  # 显示圆形面积
# print(rectangle01.area())  # 显示矩形面积
# # 添加图形
# manager.add_graph(rectangle01)
# manager.add_graph(round01)
# # 计算总面积
# print(manager.total_area())

"""
    练习4：以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤(根据攻击力，减少血量,掉落装备).
        敌人攻击玩家,玩家受伤(根据攻击力，减少血量,闪现红屏).
        要求：
            再增加新角色,之前角色代码不变.
"""


class Character:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        print('攻击')
        target.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        print('血量为：', self.hp)


class Player(Character):
    def __init__(self, atk, hp):
        super().__init__(atk, hp)

    def attack(self, target):
        super().attack(target)

    def damage(self, value):
        super().damage(value)
        print('红屏闪现')


class Enemy(Character):
    def __init__(self, atk, hp):
        super().__init__(atk, hp)

    def attack(self, target):
        super().attack(target)

    def damage(self, value):
        super().damage(value)
        print('掉落装备')

# 调用
# p01 = Player(50, 60)
# e01 = Enemy(40, 100)
# p01.attack(e01)
# e01.attack(p01)

