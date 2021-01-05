"""
* 创建流程

将需要新进程执行的事件封装为函数

通过模块的Process类创建进程对象，关联函数

可以通过进程对象设置进程信息及属性

通过进程对象调用start启动进程

通过进程对象调用join回收进程资源
"""

import multiprocessing as mp
from time import sleep

# 进程的执行函数
def fun():
    print('开始执行')
    sleep(3)
    print('一个任务假装执行了3秒结束')

# 创建进程对象
p = mp.Process(target=fun)

# 启动进程 这时进程产生，进程执行fun函数
p.start()

print('我也要干点事情')
sleep(3)
print('我这件事做了2秒')
# 阻塞等待回收进程 将资源归还给操作系统 资源释放
p.join()
