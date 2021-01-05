"""
lock 线程锁
"""
from threading import Thread, Lock

a = b = 0  # 共享资源
lock = Lock()


def value():
    while True:
        with lock:
            if a != b:
                print('a = %d,b =%d' % (a, b))
        # with语句块结束后自动解锁


t = Thread(target=value)
t.start()

while True:
    lock.acquire()  # 上锁
    a += 1
    b += 1
    lock.release()  # 解锁
t.join()
