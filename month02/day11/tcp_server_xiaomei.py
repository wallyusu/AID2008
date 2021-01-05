from socket import *
import re
chat = []
# 提取文件中的内容，放在列表中[(key,ansewer),()]
def answer():
    # 打开对话文件
    file = open('xiaomei.txt','r')
    for line in file:
        tup = re.findall(r'(\w+)\s+(.*)',line)
        chat.extend(tup)  # 将列表合并到chat列表
    file.close()

def main():
    answer() # 生成列表

tcp_socket = socket()
tcp_socket.bind(('0.0.0.0',8888))
tcp_socket.listen(5)

while True:
    print('小美等待接收...')
    connfd,addr = tcp_socket.accept()
    print('小美已经连接到:',addr)

    data = connfd.recv(1024)
    print('收到:',data.decode())
    connfd.send('')
    connfd.close()