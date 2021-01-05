"""
    业务逻辑层
""" 
from dal import HouseDao
from month01.day20.common import IterableHelper
from model import HouseModel


class HouseManagerController:
    """
        房源信息管理系统控制器：负责处理业务逻辑
    """
    def __init__(self):
        """
            创建房源系统控制器
        """
        self.__list_houses = HouseDao.load()

    @property
    def list_house(self):
        """
        :return: 显示所有房源信息
        """
        return self.__list_houses

    def get_max_total_price(self):
        # 写法1：简单但不灵活
        # 重写模型的__gt__方法
        max_total_price =  max(self.__list_houses)
        print(max_total_price)
        # 写法2： 内置高阶函数(性能高)
        # return max(self.__list_houses,key = lambda house:house.total_price)
        # 写法3： 自定义高阶函数(调试方便)
        # return IterableHelper.get_max(self.__list_houses, lambda house: house.total_price)

    def get_min_area(self):
        result = min(self.__list_houses,key=lambda house:house.area)
        print(result)

    def get_ascending_total_price(self):
        return sorted(self.__list_houses,key=lambda house:house.total_price)


    def get_descending_order_area(self):
        return sorted(self.__list_houses,key=lambda house:house.area,reverse=True)


    def get_check_room(self):
        # for item in self.__list_houses:
        #     if item.house_type == '2室1厅':
        #         print(item)
        return filter(lambda house:house.house_type == '2室1厅',self.__list_houses)

    def get_sex_floor_house(self):
        return filter(self.__condition_gt_sex_floor,self.__list_houses)

    def __condition_gt_sex_floor(self,house:HouseModel):
        # 从左到右查找
        begin = house.floor.index("共")
        # 从右到左查找
        end = house.floor.rfind("层")
        return int(house.floor[begin + 1: end]) > 6

    def get_housing_types(self):
        # 如果存在该房源类型，计数增加
        housingtype = {}
        for item in self.__list_houses:
            if item.house_type in housingtype:
                housingtype[item.house_type] += 1
            else:
                housingtype[item.house_type] = 1
        return housingtype

    def delete_all_id(self):
        all_id = []
        number = input('请输入需要删除的编号： ')
        IterableHelper.delete_all()












