"""
练习1：大文件拆分
将一个文件拆分成2个部分，按照字节数平分
要求使用两个子进程完成这件事，要求上下两个部分
的拆分工作同时进程

思路：一个进程拷贝上半部分
一个进程拷贝下半部分
两个子进程同时执行
os.path.getsize() 获取文件大小
文件操作设置：seek()
"""

from multiprocessing import Process
import os

# 获取文件大小
size = os.path.getsize('caomei.jpg')
# 上半部分
def top():
    fr = open('caomei.jpg','rb')
    fw = open('top.jpg','wb')
    n = size // 2
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
# 下半部分
def bot():
    fr = open('caomei.jpg','rb')
    fw = open('bot.jpg','wb')
    fr.seek(size // 2,0)  # 偏移量放在中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


things = [top,bot]
jobs = []
for th in things:
    p = Process(target=th)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()  # 处理僵尸
