"""
练习1：    使用进程池完成
拷贝一个指定的目录 （文件夹中全是普通文件，没有子文件夹）

思路： 1. 什么事情作为进程池事件 （拷贝文件）
      2. 拷贝文件函数 找共性封装 特性传参

      os.listdir()
      os.mkdir('XXX")
"""

from multiprocessing import Pool
from time import sleep,ctime
import random
import os

import os  # 调出os库


# 文件的复制
# def mycopy(file1, file2):  # 定义一个mycopy函数用于复制文件
#
#     f1 = open(file1, "rb")  # 以读取模式打开file1
#     f2 = open(file2, "wb")  # 以清空写模式打开file2
#
#     content = f1.readline()  # 将第一行数据赋给content
#     while len(content) > 0:  # 如果读取到的数据长度不为0则循环执行
#         f2.write(content)  # 在file2里写下content
#         content = f1.readline()  # 再读一行赋给content
#
#     f1.close()  # 关闭file1
#     f2.close()
#
#
# # 自定义目录复制函数
# def copydd(dir1, dir2):  # 定义复制文件夹函数coppydd
#     # 获取被复制目录中的所有文件信息
#     dlist = os.listdir(dir1)  # 以列表模式赋给dlist
#     # 创建新目录
#     os.mkdir(dir2)  # 创建新文件夹dir2
#     # 遍历所有文件并执行文件复制
#     for f in dlist:  # 让f在dlist中遍历
#         # 为遍历的文件添加目录路径
#         file1 = os.path.join(dir1, f)  # 将f遍历出的文件名给file1（dir1+f即路径+文件名）
#         file2 = os.path.join(dir2, f)  # 同样也给file2
#         # 判断是否是文件
#         if os.path.isfile(file1):  # 判断是否为文件的方式为os库中的函数 os.path.isfile(文件名)
#             mycopy(file1, file2)  # 调用自定义的mycopy函数复制文件
#         if os.path.isdir(
#                 file1):  # 如果是文件夹的话   那就调用自身(自身就是复制文件夹嘛)e而处理的不是dir1，dir2，是file1，file2，因为此时文件夹同文件一起被f遍历，此处判断的就是f遍历出的是文件还是文件夹
#             coppydd(file1, file2)  # 调用自身   递归思想


# 测试
# copydd("./aa", "./bb")  # 当前文件夹中的aa文件夹复制到bb文件夹   没有会自动创建


# 创建进程池
# pool = Pool(4)
#
# # 向进程池队列添加事件
# pool.apply_async(func=copydd,args=('./test','./test2'))
#
# # 关闭进程池 不能添加新的事件
# pool.close()
#
# # 阻塞回收进程池
# pool.join()

# 方法2
# 拷贝每一个文件 --》 进程池要做的事情
def copy(filename,old_folder,new_folder):
    fr = open(old_folder+"/"+filename,'rb')
    fw = open(new_folder+"/"+filename,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()



# 创建进程池 参数为要拷贝的目录
def main(old_folder):
    # 创建新文件夹
    new_folder = old_folder + "-备份"
    os.mkdir(new_folder)

    pool = Pool(4)
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy,
                         args=(file,old_folder,new_folder))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main("/home/tarena/FTP")