"""
练习2：    创建两个线程同时执行
一个线程负责打印  1--52     52个数字
另一个线程打印  A--Z  26个字母
要求打印结果为12A 34B...5152Z
"""

from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()


def number_all():
    for i in range(1, 53, 2):
        lock1.acquire()
        print(i,end=',')
        print(i + 1,end=',')
        lock2.release()


def pirnt_chr():
    for c in range(ord('A'), ord('Z') + 1):
        lock2.acquire()
        print(chr(c))
        lock1.release()


t1 = Thread(target=number_all)
t2 = Thread(target=pirnt_chr)
lock2.acquire()

t1.start()
t2.start()
t1.join()
t2.join()
