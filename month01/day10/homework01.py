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


class Game2048:

    def __init__(self,left,right,up,down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def use_game(self):
        if self.left == 'a':
            return zero_to_end(list_merge)


import random
def print_list_number():
    new_list = [0,0,2,4,0,0]
    list_merge = [[random.choice(new_list) for r in range(4)] for c in range(4)]
    return list_merge


def zero_to_end(list_merge):
    for x in range(len(list_merge)):
        for r in range(len(list_merge[x])-1):
            for c in range(r + 1,len(list_merge[x])):
                if list_merge[x][r] == 0:
                    list_merge[x][r],list_merge[x][c] = list_merge[x][c],list_merge[x][r]
    return list_merge

zero_to_end(print_list_number())


a = 1
while True:
    Game2048(a, d, w, s)
    b = input('↑')
    c = input('↓')
    d = input('←')
    e = input('→')
    f = input('e')
    if b == w:
        print(zero_to_end(print_list_number()))
    elif c == s:
        pass
    elif d == a:
        pass
    elif e == d:
        pass
    elif f == e:
        break






