"""
3. 员工管理系统
    需求：对员工信息进行(增查删改)
    class Employee:
        def __init__(self, eid, did, name, money):
            self.eid = eid # 员工编号
            self.did = did # 部门编号
            self.name = name # 姓名
            self.money = money # 工资
"""
class EmployeeModel:
    def __init__(self, name='',eid=0, did=0, money=0):
        self.name = name  # 姓名
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.money = money  # 工资

    def __str__(self):
        return f'{self.eid}的员工{self.name},部门编号为{self.did},工资为{self.money}'

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
        elif item == '2':
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

class EmployeeController:
    def __init__(self):
        self.__all_employee = [] # type:List[EmployeeModel]
        self.start_eid = 1001

    @property
    def all_emp(self):
        return self.__all_employee

    def add_employee(self,new_emp):
        new_emp.eid = self.start_eid
        self.start_eid += 1
        self.__all_employee.append(new_emp)



# 入口
view = EmployeeView()
view.main()