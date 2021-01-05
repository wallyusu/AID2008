class CommodityModel:
    def __init__(self, name, price, cid):
        self.name = name
        self.price = price
        self.cid = cid


class CommodityView:
    def __init__(self):
        self.controller = CommodityController()

    def main(self):
        while True:
            self.display_commodity()
            self.select_commodity()

    def display_commodity(self):
        print('1 添加商品信息')
        print('2 显示商品信息')
        print('3 删除商品信息')
        print('4 修改商品信息')

    def select_commodity(self):
        item = input('请选择选项：')
        if item == '1':
            self.input_commodity()
        # elif item == '2':
        #     print(self.controller.show_commodity())
        # elif item == '3':
        #     self.controller.del_commodity()
        # elif item == '4':
        #     self.controller.alter_commodity()

    def input_commodity(self):
        com = CommodityModel(name='',price=0,cid=0)
        com.name = input('请输入商品名称: ')
        com.price = int(input('请输入商品价格: '))
        self.controller.add_commodity(com)


class CommodityController:
    def __init__(self):
        self.all_com = []
        self.start_cid = 1001
        self.input_com = CommodityView()

    def add_commodity(self, new_com):
        new_com.cid = self.start_cid
        self.start_cid += 1
        self.all_com.append(new_com)

view = CommodityView()
view.main()
