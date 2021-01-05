"""
创建commodity_info_system.py文件
创建商品信息管理系统
"""

from typing import List
# import sys
# sys.setrecursionlimit(1000000)
class CommodityModel:
    def __init__(self, name='', price=0, cid=0):
        self.name = name
        self.price = price
        # 全球唯一标识符：系统为数据赋予的编号
        self.cid = cid

    def __str__(self):
        return f'{self.cid}的{self.name}商品,价格为{self.price}'


class CommodityView:
    def __init__(self):
        self.controller = CommodityController()

    def main(self):
        while True:
            self.__display_commodity() # 批量修改变量名快捷键：Ctrl + F6
            self.__select_commodity()

    def __display_commodity(self):
        print('1 添加商品信息')
        print('2 显示商品信息')
        print('3 删除商品信息')
        print('4 修改商品信息')

    def __select_commodity(self):
        item = input('请选择选项：')
        if item == '1':
            self.input_commodity()
        elif item == '2':
            self.view_commodity()
        elif item == '3':
            self.del_commodity()
        elif item == '4':
            self.modify_commodity()

    def view_commodity(self):
        for item in self.controller.all_com:
            print(item)

    def input_commodity(self):
        com = CommodityModel()
        com.name = input('请输入商品名称: ')
        com.price = int(input('请输入商品价格: '))
        self.controller.add_commodity(com)

    def del_commodity(self):
        cid = int(input('请输入要删除的商品编号： '))
        if self.controller.remove_controller(cid):
            print('删除成功')
        else:
            print('删除失败')

    def modify_commodity(self):
        com = com = CommodityModel()
        com.cid = int(input('请输入商品编号： '))
        com.name = input('请输入商品名称： ')
        com.price = int(input('请输入商品价格： '))
        if self.controller.modify_controller(com):
            print('修改成功')
        else:
            print('修改失败')


class CommodityController:
    def __init__(self):
        self.all_com = [] # type:List[CommodityModel]
        self.start_cid = 1001
        # self.input_com = CommodityView()

    def add_commodity(self, new_com):
        new_com.cid = self.start_cid
        self.start_cid += 1
        self.all_com.append(new_com)

    @property # 只读商品信息
    def show_commodity(self):
        return self.all_com

    def remove_controller(self, cid):
        """
        for item in self.all_com:
            if item.cid == cid:
                # del item # 删除栈帧中的变量,与列表无关
                # remove内部会再次循环判断需要删除的商品
                self.all_com.remove(item)
        """
        for item in range(len(self.all_com)):
            if self.all_com[item].cid == cid:
                del self.all_com[item]
                return True
        return False

    def modify_controller(self, com):
        for item in self.all_com:
            if item.cid == com.cid:
                # item.name = com.name
                # item.price = com.price
                item.__dict__ = com.__dict__
                return True
        return False


# 入口
# view = CommodityView()
# view.main()

"""
练习：写出下列代码在终端中执行效果
class A:
    def func01(self):
        print("A")
        super().func01()


class B:
    def func01(self):
        print("B")


class C(A,B):
    def func01(self):
        print("C")
        super().func01()


class D(A, B):
    def func01(self):
        print("D")
        super().func01()


class E(C,D):
    def func01(self):
        print("E")
        super().func01()

e = E()
e.func01() # B
"""