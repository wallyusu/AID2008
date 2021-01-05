"""
作业：1.进程函数使用熟练，自定义进程类
2.求100000以内质数之和，写成一个函数写一个装饰器求一个这个函数运行时间
  将100000分成4等分，分别使用4个进程求每一份的质数之和，四个进程同时执行记录时间
  将100000分成10等分，分别使用10个进程求每一份的质数之和，10个进程同时执行记录时间
"""
from multiprocessing import Process
from time import time

# l = []
# def sum_pn(num):
#     a = 0
#     for i in range(2,num):
#         for c in range(2,i):
#             if i % c == 0:
#                 break
#             # l.append(i)
#             a += i
#             break
#     return a
#
#
# print(sum_pn(10))
#
# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n//2 + 1):
#         if n % i == 0:
#             return False
#     return True

# num以内的质数之和
# def prime_sum(num:int):
#     for i in range(num + 1):
#         if isprime(i):
#             yield i
#
# sum = 0
# for item in prime_sum(100000):
#     sum += item
# print(sum)

class My_sum(Process):
    def __init__(self):
        # 调用父类init保留父类属性
        super().__init__()

    def fun1(self):
        l = []
        start_time = time()
        for i in range(2, 10001):
            for c in range(2, i):
                if i % c == 0:
                    break
            else:
                l.append(i)

        print(sum(l))
        end_time = time()
        print("运行了%.2f" %(end_time - start_time))

    def fun2(self):
        for i in range(20001,110001,10000):
            self.sum_pn(i)
    #
    # def fun3(self):
    #     self.sum_pn(30001)
    #
    # def fun4(self):
    #     self.sum_pn(40001)
    #
    # def fun5(self):
    #     self.sum_pn(50001)
    #
    # def fun6(self):
    #     self.sum_pn(60001)
    #
    # def fun7(self):
    #     self.sum_pn(70001)
    #
    # def fun8(self):
    #     self.sum_pn(80001)
    #
    # def fun9(self):
    #     self.sum_pn(90001)
    #
    # def fun10(self):
    #     self.sum_pn(100001)

    def sum_pn(self,num):
        l = []
        start_time = time()
        for i in range((num-10000), num):
            for c in range(2, i):
                if i % c == 0:
                    break
            else:
                l.append(i)
        print(sum(l))
        end_time = time()
        print("运行了%.2f" %(end_time - start_time))

    # 进程做的事情
    def run(self):
        self.fun1()
        self.fun2()
        # self.fun3()
        # self.fun4()
        # self.fun5()
        # self.fun6()
        # self.fun7()
        # self.fun8()
        # self.fun9()
        # self.fun10()

p = My_sum()
p.start() # 运行run'作为一个进程
p.join()




