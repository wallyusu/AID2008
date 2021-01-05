"""
服务端循环示例2
重点！
"""
from socket import *

# 创建tcp套接字（不写参数默认也是tcp)
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定改地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听(为连接做准备,参数为等待监听的队列数)
tcp_socket.listen(5)

# 等待客户端连接(阻塞等待处理客户端请求)
while True:
    print('等待连接...')
    connfd,addr = tcp_socket.accept()
    print('连接了：',addr)

# 收发消息
    while True:
        data = connfd.recv(1024)
        # 收到了## 表示客户端已经退出
        # 客户端断开连接，此时recv返回空字节串（不会造成服务端管道破裂的情况）
        # if not data:
        #     break
        print('接收到：', data.decode())
        connfd.send(b'Thanks')
    connfd.close()


tcp_socket.close()