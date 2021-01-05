'''
含有参数的进程函数示例
'''
from multiprocessing import Process
from time import sleep
from signal import *
import os

# 含有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")

# 忽略子进程退出
signal(SIGCHLD,SIG_IGN)

# 创建进程 按位置传参 arg = ()
# p = Process(target=worker,args=(2,'Levis'))

# 按关键字传参 kwargs={}
p = Process(target=worker,kwargs={'name':'Levis','sec':2})
# 该子进程会随父进程而退出 start前设置
# p.daemon = True
p.start()
# p.join(3)  # 最多等待3秒(超时时间)

# print('Name:',p.name)  # 进程名
# print('PID:',p.pid)
# print('is alive',p.is_alive())
print(os.getppid(),'--',os.getpid())


