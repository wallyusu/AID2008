from bll import EmployeeController
from model import EmployeeModel
class EmployeeView:
    def __init__(self):
        self.__controller = EmployeeController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print('1 添加员工信息')
        print('2 显示员工信息')
        print('3 删除员工信息')
        print('4 修改员工信息')

    def __select_menu(self):
        item = input('请选择选项：')
        if item == '1':
            self.input_employee()
        if item == '2':
            self.show_employee()



    def input_employee(self):
        emp01 = EmployeeModel()
        emp01.did = int(input('请输入部门编号： '))
        emp01.name = input('请输入员工姓名： ')
        emp01.money = int(input('请输入员工工资： '))
        self.__controller.add_employee(emp01)

    def show_employee(self):
        for item in self.__controller.all_emp:
            print(item)






