"""
基于select的 IO网络并发模型
IO多路复用与非阻塞搭配
重点代码！
"""
from socket import *
from select import select

# 网络地址
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 创建监听套接字
sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

# 初始只有监听套接字，先关注他
rlist = [sockfd]  # 客户端连接
wlist = []
xlist = []

# 开始监控IO对象
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is sockfd:
            # 处理就绪的IO
            connfd, addr = r.accept()
            print('Connect from:', addr)
            connfd.setblocking(False)
            rlist.append(connfd)  # 将客户端连接套接字也监控起来
        else:
            # 某个客户端发消息 connfd 就绪
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue  # 不用break，因为可能会有多个客户端连接，要处理后续的connfd
            print(data)
            # r.send(b'OK')
            wlist.append(r)

    for w in ws:
        w.send(b'OK')
        wlist.remove(w)  # 写完要移除，不要一直写

    for x in xs:
        pass



# while True:
#     connfd, addr = sockfd.accept()
#     print('Connect from:', addr)
