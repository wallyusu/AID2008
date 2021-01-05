# def f(n):
#     if n == 0:
#         return
#     print(n)
#     f(n-1)
#
# f(3)

"""
递归实现n的阶乘
5的阶乘：5*4*3*2*1
"""


# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n-1)
#
#
# print(f(5))
#
# """
# 递归实现 n + (n-1) + (n-2)... +1 的过程
# """
# def s(n):
#     if n == 1:
#         return 1
#     return n + s(n-1)
#
# print(s(5))
# # python设定最大递归深度：998
# print(s(998))

def jump(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return jump(n - 1) + jump(n - 2)

print(jump(10))