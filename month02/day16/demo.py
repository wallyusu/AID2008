from socket import *
from time import sleep,ctime


sock = socket()
addr = ('0.0.0.0',8000)
sock.bind(addr)
sock.listen(5)

log = open('my.log','a')

sock.setblocking(False)

while True:
    try:
        data,addr = sock.accept()
        print('Connect from:',addr)
    except timeout as c:
        print('开始写日志')
        sleep(2)
        msg = '%s:%s\n'%(ctime(),e)
        log.write(msg)
        log.flush()
    except BlockingIOError as e:
        print('非阻塞日志')
        sleep(2)


    else:
        f = sock.recv(128).decode()
        print(f)


