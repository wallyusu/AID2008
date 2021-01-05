"""
练习：模拟一个售票系统程序
一共500张票 --> T1---T500
编写10个线程模拟10个售票窗口机器 记为W1-W10
10个窗口同时售票 直到所有票都卖出为止

票按照顺序出售
每个窗口卖出一张票后 w2---T346
卖出一张需要0.1s
"""

from threading import Thread
from time import sleep

ticket_list = []
for i in range(1, 501):
    ticket_list.append('T%d' % i)


def buy_ticket(i):
    while True:
        if len(ticket_list) == 0:
            print('w%s票已售完'%i)
            break
        t = ticket_list.pop(0)  # 提取列表内容并删除
        print('w%s---%s' % (i, t))
        sleep(0.1)


jobs = []
for i in range(1, 11):
    t = Thread(target=buy_ticket, args=(i,))
    jobs.append(t)
    t.start()

[c.join() for c in jobs]

