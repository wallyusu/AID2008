"""
udp客户端流程示例
重点代码！
"""
from socket import *

# 服务端地址
ADDR = ('127.0.0.1',8888)

# 创建upd套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 发送内容
while True:
    msg = input('>>>')
    # msg为空 则退出循环
    if not msg:
        break
    udp_socket.sendto(msg.encode(),ADDR)

# 接收反馈
    data,addr = udp_socket.recvfrom(1024)
    print('From server:',data.decode())



# 关闭
# udp_socket.close()