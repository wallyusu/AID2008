class EmployeeModel:
    def __init__(self, name='',eid=0, did=0, money=0):
        self.name = name  # 姓名
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.money = money  # 工资

    def __str__(self):
        return f'{self.eid}的员工{self.name},部门编号为{self.did},工资为{self.money}'


