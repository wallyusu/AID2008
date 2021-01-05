"""
练习2：定义函数,根据总两数,计算几斤零几两.:
 提示：使用容器包装需要返回的多个数据
total_liang = int(input("请输入两:"))
jin = total_liang // 16
liang = total_liang % 16
print(str(jin) + "斤零" + str(liang) + "两")
"""


# def total_jl(t):
#     """
#
#     :param t:int类型
#     :return: 计算几斤几两
#     """
#     j = t // 16
#     l = t % 16
#     return (f'{j}斤零{l}两')
#
# total_liang = int(input('请输入两： '))
# print(total_jl(total_liang))

"""
练习3：创建函数,根据课程阶段计算课程名称.
number = input("请输入课程阶段数：")
if number == "1":
    print("Python语言核心编程")
elif number == "2":
    print("Python高级软件技术")
elif number == "3":
    print("Web全栈")
elif number == "4":
    print("网络爬虫")
elif number == "5":
print("数据分析、人工智能")
"""

def text(number):
    """
    查找课程目录
    :param number: 输入课程编号
    :return: 课程名称
    """
#     if number == '1':
#         return 'Python语言核心编程'
#     elif number == '2':
#         return 'python高级软件技术'
#     elif number == '3':
#         return 'web全栈'
#     elif number == '4':
#         return '网络爬虫'
#     elif number == '5':
#         return '数据分析、人工智能'
#
#
# print(text(str(4)))

"""
练习4：创建函数,计算梯形面积.
top_base = float(input("请输入上底："))
bottom_base = float(input("请输入下底："))
height = float(input("请输入高："))
result = (top_base + bottom_base) * height / 2
print("梯形面积是：" + str(result))
"""
# def area(top_base,bottom_base,height):
#     """
#     计算梯形面积
#     :param top_base: 上底
#     :param bottom_base: 下底
#     :param height: 高
#     :return:
#     """
#     return (top_base + bottom_base) * height / 2
#
#
# print('梯形面积为：',area(5, 4, 8))

"""
练习5：创建函数,计算IQ等级
ma = int(input("请输入你的心里年龄："))
ca = int(input("请输入你的实际年龄："))
iq = ma / ca * 100
if 140 <= iq:
    print("天才")
elif 120 <= iq:
    print("超常")
elif 110 <= iq:
    print("聪慧")
elif 90 <= iq:
    print("正常")
elif 80 <= iq:
    print("迟钝")
else:
    print("低能")
"""
# def your_iq(ma,ca):
#     """
#     计算IQ
#     :param ma: 输入心里年龄
#     :param ca: 输入实际年龄
#     :return: IQ值
#     """
#     iq = ma / ca * 100
#     if 140 <= iq:
#         return "天才"
#     if 120 <= iq:
#         return "超常"
#     if 110 <= iq:
#         return "聪慧"
#     if 90 <= iq:
#         return "正常"
#     if 80 <= iq:
#         return "迟钝"
#     return "低能"
#
# print(your_iq(30, 20))

"""
练习6：创建函数,根据年龄计算人生阶段
age = int(input("请输入年龄："))
if age <= 6:
    print("童年")
elif age <= 17:  # 程序能执行到本行,说明age一定大于6
    print("少年")
elif age <= 40:
    print("青年")
elif age <= 65:
    print("中年")
else:
    print("老年")
"""
# def stages_of_life(age):
#     """
#     计算人生阶段
#     :param age: 输入实际年龄
#     :return: 显示人生所在阶段
#     """
#     if age <= 6:
#         return "童年"
#     if age <= 17:  # 程序能执行到本行,说明age一定大于6
#       return "少年"
#     if age <= 40:
#       return "青年"
#     if age <= 65:
#       return "中年"
#     return "老年"


# print(stages_of_life(33))

"""
练习7：创建函数,根据年月计算天数.
        如果2月是闰年,则29天
        　　　 平年    28
month = int(input("请输入月份:"))
if 1 <= month <= 12:
    if month == 2:
        print("29天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30天")
    else:# 1 3 5 7 8 10 12
        print("31天")
else:
    print("月份有误")

year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day = 29
else:
    day = 28
"""
def all_days(year,month):
    """
    根据年月计算天数
    :param year: 年份
    :param month: 月份
    :return: 当月有多少天
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        day = 29
    else:
        day = 28
    if 1 <= month <= 12:
        if month == 2:
            return f"{day}天"
        if month == 4 or month == 6 or month == 9 or month == 11:
            return "30天"
        return "31天"
    

print(all_days(2010, 2))
