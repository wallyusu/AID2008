"""
    作业：1.熟练正则表达式元字符
         2.给予log.txt文档
         编写一个函数传入一个端口的名称，返回这个端口对应的address值
         address is
"""
import re
# 提取每一段文字 --> 生成器
def get_info():
    file = open('log.txt','r') # 读方式打开
    while True:
        # 每次while循环info就获取一段内容
        info = ''
        for line in file:
            if line == '\n':
                break
            info += line # 累加一段的内容
        # print(info)
        # print('------------------------------------')
        # info 为空说明到了文件结尾
        if not info:
            file.close()
            return
        else:
            yield info