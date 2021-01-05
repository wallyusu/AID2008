list_merge = [2, 0, 2, 0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

import random
def merge():
    """
        合并
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    # [4,4,4,4]
    for i in range(len(list_merge) - 1):  # 取前三个  i
        if list_merge[i] == list_merge[i + 1]:  # 与下一个比 i + 1
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]  # 删除下一个(因为不是当前,所以不存在漏删)
            list_merge.append(random.choice([0,0,2,0]))  # 因为删除一个,补充一个,所以不存在越界


map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]


def move_left():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        list_merge = line
        merge()

def move_right():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        # 从右向左获取数据形成新列表
        list_merge = line[::-1]
        # 处理数据
        merge()
        # 将处理后的数据再从右向左还给map
        line[::-1] = list_merge

def transport(map):
    # global list_merge
    for i in range(1, len(map)):
        for j in range(i, len(map)):
            map[j][i - 1], map[i - 1][j] = map[i - 1][j], map[j][i - 1]

def move_up():
    transport(map)
    move_left()
    merge()
    transport(map)

def move_down():
    transport(map)
    move_right()
    merge()
    transport(map)

def set_type():
    for num in map:
        print(num)

def main():
    while True:
        set_type()
        direction = input('---------------------')
        if direction == 'w':
            move_up()
        elif direction == 's':
            move_down()
        elif direction == 'a':
            move_left()
        elif direction == 'd':
            move_right()


print(main())