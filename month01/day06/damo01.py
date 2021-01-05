"""
列表推导式
"""
# 语法：
# 列表 = [变量 for 变量 in 可迭代对象 if 对变量的判断]

"""
练习： 
生成10--30之间能被3或者5整除的数字
[10, 12, 15, 18, 20, 21, 24, 25, 27]
生成5 -- 20之间的数字平方
[25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
"""

# list_num = [item for item in range(10,30) if item % 3 == 0 or item % 5 == 0]
# print(list_num)
# list_num01 = [item ** 2 for item in range(5,20)]
# print(list_num01)

"""
    元组
"""
# for .. in ..快捷键 iter + 回车键

'''
name = "张无忌"
names = ["赵敏", "周芷若"]
tuple01 = ("张翠山", name, names)
name = "无忌哥哥"
tuple01[2][0] = "敏儿"
print(tuple01)  # ('张翠山', '张无忌', ['敏儿', '周芷若'])
'''

'''
练习2：
    根据月日,计算是这一年的第几天.
    公式：前几个月总天数 + 当月天数
例如：5月10日
    计算：31  29  31  30 + 10
'''
# month02 = 0
# day_of_month = (31,29,31,30,31,30,31,31,30,31,30,31)
# month01 = int(input('请输入月份：'))
# day = int(input('请输入日期：'))
# day_sum = sum(day_of_month[:month01 - 1]) # 方法2
# for i in range(month01 - 1):
#     month02 += day_of_month[i]
# day_sum = month02 + day
# print(day_sum)

"""
列表转换成字典
语法：[(  ,  ),(  ,  )]
注意：列表内的元素必须能够一分为二
字典名 = dict(可迭代对象)
"""
# 添加(不存在)    字典名[键] = 值
# if 'money' not in dict_lsw:
#     dict_lsw['money'] = 100000

# 定位
# 键
# value = dict_lsw['age']
# print(value)

# 修改(键存在)
# dict_lsw['age'] = 38

"""
练习1：
创建字典存储香港信息、字典存储上海信息、字典存储新疆信息
"""
dict_hk = {'地区':'香港','新增':15,'现有':393,'累计':4801,'治愈':4320,'死亡':88}
dict_sh = {'地区':'上海','新增':6,'现有':61,'累计':903,'治愈':835,'死亡':7}
dict_xj = {'地区':'新疆','新增':0,'现有':49,'累计':902,'治愈':850,'死亡':3}



"""
    练习2：
        在终端中打印香港的现有人数
        在终端中打印上海的新增和现有人数
        新疆新增人数增加1
"""
# print(dict_hk['现有'])

# print(dict_sh['新增'],dict_sh['现有'])

# dict_xj['新增'] += 1
# print(dict_xj['新增'])

"""
练习3：
        删除香港现有人数信息
        删除新疆新增人数信息
        删除上海的新增和现有信息
"""
# del dict_hk['现有'],dict_xj['新增'],dict_sh['新增'],dict_sh['现有']
# print(dict_hk,dict_sh,dict_xj,sep='\n')
# cdf = """jh
# sd"""
# print(cdf)

'''
    遍历
    删除
'''

'''
    练习4：
        在终端中打印香港字典的所有键(一行一个)
        在终端中打印上海字典的所有值(一行一个)
        在终端中打印新疆字典的所有键和值(一行一个)
        在上海字典中查找值是61对应的键名称
'''
# for key in dict_hk:
#     print(key)
#
# for value in dict_sh.values():
#     print(value)
#
# for key,value in dict_xj.items():
#     print(key,value)
# 语法1：
# for key in dict_sh:
#     if dict_sh[key] == 61:
#         print(key)
# 语法2：
# for key,value in dict_sh.items():
#     if value == 61:
#         print(key)

"""
    字典推导式
        字典名 = {键的操作:值的操作 for 变量 in 可迭代对象 if 条件}
"""

"""
练习1：
将两个列表，合并为一个字典
		姓名列表["张无忌","赵敏","周芷若"]
		房间列表[101,102,103]
{101: '张无忌', 102: '赵敏', 103: '周芷若'}
"""
# 方法1：
# name = ["张无忌","赵敏","周芷若"]
# room = [101,102,103]
# dict_name = {}
# for number in range(len(name)):
#     dict_name[name[number]] = room[number]
# print(dict_name)
# 方法2：
# dict_name02 = {name[number]:room[number] for number in range(len(name))}
# print(dict_name02)


"""
练习2：
颠倒练习1字典键值
{'张无忌': 101, '赵敏': 102, '周芷若': 103}
"""
# dict_name02 = {value:key for key,value in dict_name.items()}
# print(dict_name02)
"""
    集合set 基础操作：
        作用1：去重复
"""
# 创建
# 添加
# 定位
# 遍历
# 删除

"""
练习：一家公司有如下岗位：
         "经理"："曹操","刘备","孙权"
         "技术" ："曹操","刘备","张飞","关羽"
    1. 定义数据结构,存储以上信息.
    2. 是经理也是技术的都有谁?
    3. 是经理不是技术的都有谁?
    4. 不是经理是技术的都有谁?
    5. 身兼一职的都有谁?
    6. 公司总共有多少人数?
"""

# # 1;
# dict_jl = {"经理":{"曹操","刘备","孙权"}}
# dict_js = {"技术":{"曹操","刘备","张飞","关羽"}}
# # 2;
# s1 = dict_jl['经理'] & dict_js['技术']
# print(s1)
# # 3;
# s2 = dict_jl['经理'] - dict_js['技术']
# print(s2)

# # 4;
# s3 = dict_js['技术'] - dict_jl['经理']
# print(s3)

# # 5;
# s4 = dict_js['技术'] ^ dict_jl['经理']
# print(s4)
#
# # 6;
# s5 = dict_js['技术'] | dict_jl['经理']
# print(s5)
