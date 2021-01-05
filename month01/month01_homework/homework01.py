"""
6. (选做)2048 游戏算法
# 全局变量
list_merge = [2,0,2,0]
(1). 定义函数,将零元素移动到末尾zero_to_end()
 备注：操作全局变量
    [2,0,2,0]  -->  [2,2,0,0]
    [2,0,0,2]  -->  [2,2,0,0]
    [2,4,0,2]  -->  [2,4,2,0]

    (2). 定义合并函数(向左移动的核心算法)　merge()
        思路：相邻相同数据合并
        [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
        [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
        [4,4,4,4]  -->  [8,8,0,0]
        [2,0,4,2]  -->  [2,4,2,0]
"""

# (1). 定义函数,将零元素移动到末尾zero_to_end()
# list_merge01 = [2,0,2,0] # 全局变量列表
# 定义函数：
def zero_to_end(list_merge):
    """
    将零元素移动到末尾
    :param list_merge: 调用全局变量list_merge01
    :return: 返回将零元素移动到末尾
    """
    for r in range(len(list_merge)-1):
        for c in range(r + 1,len(list_merge)):
            if list_merge[r] == 0:
                list_merge[r],list_merge[c] = list_merge[c],list_merge[r]
    return list_merge
# 调用：
# print(zero_to_end(list_merge01))
# ——————————————————————————————————————————————————————————————————————————————
# (2). 定义合并函数(向左移动的核心算法)　merge()
#     思路：相邻相同数据合并

def merge(list_merge):
    """
    相邻相同数据合并
    :param list_merge: 调用全局变量list_merge01
    :return: 将相邻相同数据合并
    """
    for number in range(len(list_merge)-1):
        if list_merge[number] == list_merge[number + 1]:
                list_merge[number] += list_merge[number + 1]
                list_merge[number + 1] = 0
    return list_merge

list_merge01 = [2,0,2,4]
while True:
    print(list_merge01)
    play = input('是否继续[c]:')
    if play =='c':
        zero_to_end(list_merge01)
        merge(list_merge01)
        zero_to_end(list_merge01)
    else:
        break
print(list_merge01)



