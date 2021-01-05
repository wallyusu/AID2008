from multiprocessing import Queue,Process


q = Queue()

def func1():
    name = 'Baby'
    passwd = '123456'
    q.put(name)
    q.put(passwd)

def func2():
    name = q.get()
    passwd = q.get()
    print('用户名：',name)
    print('密码: ',passwd)


p1 = Process(target=func1)
p2 = Process(target=func2)
p1.start()
p2.start()
p1.join()
p2.join()