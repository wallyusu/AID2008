#  线程事件函数
from threading import Thread


def spider():
    print('正在请求 解析 处理数据中...')

for i in range(5):
    t_list = []
    t = Thread(target=spider)
    t_list.append(t)
    t.start()
    t.join()
