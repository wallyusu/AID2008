"""
python实现快速排序
"""


def quick_sort(li, first, last):
    # 递归出口
    if first >= last:
        return
    split_pos = sort(li, first, last)

    # 递归思想
    quick_sort(li, first, split_pos - 1)
    quick_sort(li, split_pos + 1, last)


def sort(li, first, last):
    """
    :param li: 源列表（从头到尾操作的列表）
    :param first: 基准值的下标索引
    :param last: 最后一个元素的下标索引
    :return: 基准值的正确位置
    """
    mid = li[first]
    lcur = first + 1
    rcur = last
    sign = False
    while not sign:
        # 左游标右移
        while lcur <= rcur and li[lcur] <= mid:
            lcur += 1
        # 右游标左移
        while lcur <= rcur and li[rcur] >= mid:
            rcur -= 1
        # 判断是交换哪个位置
        if lcur <= rcur:
            sign = True
            li[lcur], li[rcur] = li[rcur], li[lcur]
        else:
            li[first], li[rcur] = li[rcur], li[first]
    return rcur


if __name__ == '__main__':
    li = [6, 5, 3, 1, 8, 7, 2, 4]
    quick_sort(li, 0, len(li) - 1)
    print(li)
