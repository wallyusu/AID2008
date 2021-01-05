"""
练习1：
创建2个模块module_exercise.py与exercise.py
	将下列代码粘贴到module_exercise模块中，并在exercise中调用。
"""
from module_exercise import func01
# func01()
#方法1,更适合面向过程（全局变量,函数）
# import module_exercise
# module_exercise.func01()
# module_exercise.MyClass().func02()
# module_exercise.MyClass().func03()
# print(module_exercise.data)
# 方法2：更适合面向对象(类)
#注意 导入的成员可能和当前模块成员有冲突
# from module_exercise import *
# # func01()
# print(data)
# myclass = MyClass()
# myclass.func02()
# myclass.func03()