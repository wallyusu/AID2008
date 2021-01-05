"""
        张无忌教赵敏九阳神功
        赵敏教张无忌玉女心经
        张无忌工作挣了5000元
        赵敏工作挣了10000元
        提示：张无忌与赵敏是数据不同
             行为相同
"""
class Person:
    def __init__(self,name):
        self.name = name
    def teacher(self,other,teach):
        print(self.name,'教',other.name,teach)
    def work_money(self,money):
        print(f'{self.name}工作挣了{money}')

# zwj = Person('张无忌')
# zm = Person('赵敏')
# zwj.teacher(zm,'九阳神功')
# zwj.work_money(5000)
# zm.teacher(zwj,'玉女心经')
# zm.work_money(10000)


"""
6. (选做) 2048 核心算法
    3. 定义向左移动函数,改变list_map中的数据
       思路：将list_map每行赋值给list_merge
            调用合并函数(练习2)

    4. 定义向右移动函数,改变list_map中的数据
       思路：将list_map每行,反转,赋值给list_merge
            调用合并函数
            将list_merge反转后赋值给list_map
"""
