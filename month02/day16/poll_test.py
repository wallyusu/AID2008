"""
poll IO多路复用方法
"""
from socket import *
from select import *

# 制作一些IO对象
file = open('my.log', 'a+')

socket_tcp = socket()
socket_tcp.bind(('0.0.0.0', 8888))
socket_tcp.listen(5)

socket_udp = socket(AF_INET, SOCK_DGRAM)

# 查找字典 需要与register的IO保持一致
map = {socket_tcp.fileno(): socket_tcp,
       socket_udp.fileno(): socket_udp,
       file.fileno(): file}

# 准备poll方法
p = poll()  # 生成poll对象
p.register(socket_tcp, POLLIN | POLLERR)
p.register(socket_udp, POLLOUT)
p.register(file, POLLOUT)

print("开始监控IO")
events = p.poll()

# events --> [(fileno,event),()]
# 必须获取到IO对象才能调用方法处理IO
print(events)
