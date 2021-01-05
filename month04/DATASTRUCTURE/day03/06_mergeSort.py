"""
归并排序
"""
def merge_sort(li):
    if len(li) == 1:
        return li
    # [6,5,3,8]
    mid = len(li) // 2
    left = li[:mid]  # li[:2] = [6,5]
    right = li[mid:]  # li[2:] = [3,8]
    # 递归思想
    left_li = merge_sort(left)
    right_li = merge_sort(right)

    # 合并：调用递归之后的语句，从内到外（回归）执行
    return merge(left_li,right_li)

def merge(left_li,right_li):
    """合并代码"""
    # [3,5] [2,6]
    result = []
    while left_li and right_li:
        if left_li[0] <= right_li[0]:
            result.append(left_li.pop(0))
        else:
            result.append(right_li.pop(0))

    # 循环结束：一定有一个列表为空
    if left_li:
        result.extend(left_li)
    else:
        result.extend(right_li)
    return result

if __name__ == '__main__':
    li = [6,5,3,1,8,7,2,4]
    print(merge_sort(li))
    # print(merge([3,5],[2,6]))