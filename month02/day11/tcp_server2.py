from socket import *

tcp_socket = socket()
tcp_socket.bind(('0.0.0.0',8888))
tcp_socket.listen(5)

while True:
    print('等待连接...')
    connfd, addr = tcp_socket.accept()
    print('连接了：', addr)

    data = connfd.recv(1024)
    print('收到：',data.decode())
    connfd.send(b'Thanks')
    connfd.close()
