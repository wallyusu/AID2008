from typing import List
from model import EmployeeModel
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






