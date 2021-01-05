from bll import HouseManagerController
"""
    用户显示层
"""
class HouseManagerView:
    def __init__(self):
        self.__dao = HouseManagerController()

    def display_house(self):
        print('1.显示所有房源信息')
        print('2.显示总价最高的房源信息')
        print('3.显示面积最小的房源信息')
        print('4.根据总价升序显示房源信息')
        print('5.根据面积降序显示房源信息')
        print('6.查看所有“2室1厅”')
        print('7.显示所有6层以上房源信息')
        print('8.查看房源类型信息')
        print('9.根据编号删除多个信息')
        return self.input_infos()

    def input_infos(self):
        number = int(input('请输入编号按键： '))
        if number == 1:
            self.__show_house()
        elif number == 2:
            self.max_total_price()
        elif number == 3:
            self.min_area()
        elif number == 4:
            self.ascending_total_price()
        elif number == 5:
            self.descending_order_area()
        elif number == 6:
            self.check_room()
        elif number == 7:
            self.sex_floor_house()
        elif number == 8:
            self.housing_types()
        elif number == 9:
            self.delete_id()
        else:
            print('输入的编号有误，请重新输入')


    def main(self):
        self.display_house()
        self.input_infos()

    def __show_house(self):
        for item in self.__dao.list_house:
            """
                直接打印对象，由对象的__str__展示想要的的显示效果
            """
            print(item)
        return self.display_house()

    def max_total_price(self):
        return self.__dao.get_max_total_price()

    def min_area(self):
        return self.__dao.get_min_area()

    def ascending_total_price(self):
        for item in self.__dao.get_ascending_total_price():
            print(item)

    def descending_order_area(self):
        for item in self.__dao.get_descending_order_area():
            print(item)

    def check_room(self):
        for item in self.__dao.get_check_room():
            print(item)

    def sex_floor_house(self):
        for item in self.__dao.get_sex_floor_house():
            print(item)

    def housing_types(self):
        for key,value in self.__dao.get_housing_types().items():
            print(f'房型{key}有{value}套')

    def delete_id(self):
        number = input('请输入需要删除的编号,使用“,”号隔开： ')
        self.__dao.delete_all_id()






