# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n//2 + 1):
#         if n % i == 0:
#             return False
#     return True
#
# # num以内的质数之和
# def prime_sum(num:int):
#     for i in range(num + 1):
#         if isprime(i):
#             yield i
#
# sum = 0
# for item in prime_sum(100000):
#     sum += item
# print(sum)

'''
字节串示例
1.是否所有的字符串都能转换成字节串  Yes
2.是否所有的字节串都能转换成字符串  No
'''
# name = 'Emma'
# print(type(name))
# # ascii字符定义字节串
# name01 = b'Emma'
# print(type(name01))
# name02 = '张无忌'.encode()
# print(type(name02))
# # 将字节串转化成字符串
# print(name02.encode())
"""
    打开文件
"""
# 打开文件
# file = open('file.txt','w') # w不存在文件会自动创建 文件存在 原有内容会被清空
# file = open('file.txt','r') # r文件必须存在
# file = open('file.txt','a') # a追加方式 原有内容不会清空
# file = open('caomei.jpg','rb')
# 对于大文件 建议循环读取,而不是一次性读取
# while True:
#     data = file.read(5)
#     if not data:# if data == '':
#         break
#     print(data,end='')
# 每次读取一行的内容
# data = file.readline(50)
# print(data)
# data = file.readline(50)
# print(data)
# 读取多行
# data = file.readlines(20)
# print(data)
# for循环取每一行 读方式文件自带迭代属性
# for line in file:
#     print(line)
# 读写文件
# data = file.read() # 不加参数表示读取所有内容
# print(data)
# 关闭文件
# file.close()

"""
练习1：    基于单词本完成
编写一个函数,传入一个单词,返回单词对应的解释

提示：每行一个单词
     
"""
# def word_expain(n):
#     file = open('dict.txt','r')
#     for word in file:
#         # 提取单词和解释
#         tmp = word.split(' ',1) # split对单词和解释做切割,切一次
#         if n in tmp[0]:
#             return tmp[1].strip() # strip()去除解释前的所有空格键
#
#
# print(word_expain('abbey'))
# 方法2：
# def word_expain(n):
#     file = open('dict.txt','r')
#     for word in file:
#         # 提取单词和解释
#         tmp = word.split(' ',1) # split对单词和解释做切割,切一次
#         if tmp[0] > word:
#             break
#         if n in tmp[0]:
#             return tmp[1].strip() # strip()去除解释前的所有空格键
#             file.close()
#
#
# print(word_expain('abbey'))

"""
    文件写入操作
"""
# # 写方式打开文件
# # file = open('file.txt','w')
# file = open('file.txt','a') # 追加
# # 写入内容
# n = file.write('祝福祖国节日快乐.\n') # 追加的字符不会换行，需要手动\n换行
# print(f'写入了{n}个字符')
# # 关闭
# file.close()

"""
    练习2:    文件拷贝
    编写一个copy函数,传入一个具体的文件,将传入的文件以当前日期为名字，拷贝当程序所在的文件夹下
    假设文件比较大,不许一次性读取
"""
# import time
# def copy(filename):
#     file = open(filename,'rb')
#     new_file = '%s-%s-%s.jpg' %time.localtime()[:3]
#     file01 = open(new_file,'wb')
#     while True:
#         data = file.read()
#         if not data:
#             break
#         file01.write(data)
#     file.close()
#     file01.close()
#
# copy('caomei.jpg')

"""
    with打开文件
"""
# with open('file.txt','w') as f:
#     nb = f.write('hello kitty')
#     print(nb)


# with open('file.txt','r') as f:
#     data = f.read(4)
#     print(f.tell())
#     n = f.tell()

"""
    缓冲实验演示
"""
# f = open('file.txt','w')

# while True:
#     data = input('>>')
#     if not data:
#         break
#     f.write(data)
#
# f.close()

# while True:
#     data = input('>>')
#     if not data:
#         break
#     f.write(data)
#     f.flush() # 刷新缓冲
#
# f.close()

# f = open('file.txt', 'w', buffering=1)
# while True:
#     data = input('>>')
#     if not data:
#         break
#     f.write(data + '\n')
#
# f.close()
# 指定缓冲区大小   必须要二进制方式打开
# f = open('file.txt', 'wb', buffering=15)
# while True:
#     data = input('>>')
#     if not data:
#         break
#     f.write(data.encode())
#
# f.close()

"""
    文件偏移量（文件指针）
"""
# f = open('file.txt','w+')
# f.write('Hello World')
# f.flush() # 文件有内容
#
# print('文件偏移： ',f.tell())
# # 操控文件偏移量
# f.seek(2,0) # 当第二个数（即指针定位）不是0.是1或2的时候，需要以二进制方式打开文件才可以操作
# data = f.read()
# print(data)
# f.close()

"""
练习3：
写一个程序，向一个文件 my.log中不断写入内容
    1.2020-10-10 12:12:12
提示：sleep(2)
    使用什么方式打开
    序号如何衔接 -> 有多少行
"""
# import time
# file = open('my.log','a+',buffering=1)
# num = 1
# file.seek(0,0)
# for line in file:
#     num += 1
# while True:
#     note = time.ctime()
#     file.write(f'{num}. {note}\n')
#     num += 1
#     time.sleep(2)


"""
    作业：
    1.重点函数自己熟练 open read write
    2.文件拷贝代码自己会写
    3.现在有两个文本文件（自己指定）,编写一个程序
    将两个文件合并为一个新的文件
"""
# def merger_documents(filename):
#     file = open(filename,'r')
#     details = file.read(1024)
#     with open('homework_total','a+',buffering=1) as f:
#         f.write(details+'\n')
#     file.close()

# merger_documents('homework_text01.py')
# merger_documents('homework02.py')
# merger_documents('file.txt')


def copy(filename,fw):
    """
    :param filename: 要拷贝的文件
    :param fw:
    :return:
    """

"""
OS模块    文件处理小函数
"""
import os
# 查看文件的大小
# print(os.path.getsize('file.txt'))
# 获取目录下的内容
# print(os.listdir('/home/tarena/桌面'))
# 判断一个文件是否存在 True False
# print(os.path.exists('caomei.jpg'))
# 判断一个文件是否为普通文件 True False
# print(os.path.isfile('caomei.jpg'))
# 删除文件
# os.remove('file.txt')

"""
练习1： 编写一个函数，传入一个文件夹，删除该文件夹中小

于100kb的普通文件。
"""