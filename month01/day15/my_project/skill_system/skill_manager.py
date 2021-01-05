from skill_system.skill_deployer import StudentView
class Student:
    def __init__(self):
        self.__view = StudentView()
    def print_stu(self):
        print('pirnt_stu')
        self.__view.input_stu()



# stu = Student()
# # print(stu.print_stu())