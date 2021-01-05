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
练习1： 编写一个函数，传入一个文件夹，删除该文件夹中小于100kb的普通文件。
"""
# import os
# def remove_file(dir):
#     for file in os.listdir(dir):
#         filename = dir + '/' + file
#         if os.path.getsize(filename) < 1024*100 and os.path.isfile(filename) == True:
#             os.remove(filename)
#
# if __name__ == '__main__':
#     remove_file('text')
import re
# s = 'Alex:1544,bummy:1954'
# pattern = r'(?P<name>\w+):(?P<age>\d+)'

# result = re.match(pattern,s)
# print(result.group('name'))

# result = re.finditer(pattern,s)
# for i in result:
#     print(i.span())
#     print(i.group())

# result = re.search(pattern,s)
# print(result.groupdict())
"""
功能扩展
"""
s = """Hello
上海
"""
# result = re.findall(r'\w+',s,flags=re.A)
# print(result)

# result = re.findall(r'[a-z]+',s,flags=re.I)
# print(result)

# result = re.findall(r'.+',s,flags=re.S)
# print(result)

"""
现在有两个文本文件（自己指定），
编写一个程序将两个文件合并为一个新的文件
"""

# 分拷贝文件
def copy(filename,fw):
    """
    filename: 要拷贝的文件
    fw: 文件对象，向fw中去写
    """
    fr = open(filename,'rb')
    # 文件复制
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()

def union_files(filename,filelist):
    """
    :param filename: 要合成的文件
    filelist : 要拼接的文件列表
    """
    fw = open(filename,'wb')
    # 拼接两个文件
    for file in filelist:
        copy(file,fw) # 拷贝文件
    fw.close()

if __name__ == '__main__':
    filelist = [
    '../day01/1.txt',
    '../day02/2.txt',
    '../day03/3.txt'
    ]

    union_files('./笔记.txt',filelist)

"""
正则表达式 re  示例
"""
import re

# 目标字符串
s = "Alex:1996,Sunny:1997"
pattern = r"(\w+):(\d+)"

# 有子组的时候函数只返回子组对应的内容，而不是正则匹配到的内容
# result = re.findall(pattern,s)
# print(result)

# 使用正则表达式匹配到的内容切割字符串s
# result = re.split("\W+",s,2)
# print(result)


# 使用 ## 替换正则表达式匹配到的内容，返回替换后的字符串
result = re.sub("\W+",'##',s,2)
print(result)

"""
正则表达式 re  示例 2
"""

import re

# 目标字符串
s = "Alex:1996,Sunny:1997"
pattern = r"(?P<name>\w+):(\d+)"

# 匹配目标字符串，只匹配第一处
result = re.search(pattern,s)
# 获取捕获组字典 {组名:对应内容}
print(result.groupdict())


# # 匹配目标字符串的开始位置
# result = re.match(pattern,s)
# # 通过group传参可以获取指定子组的对应内容
# print(result.group('name'))

# # 匹配到的内容形成一个可迭代的对象
# result = re.finditer(pattern,s)
#
# # 每次迭代取出一处匹配内容
# for i in result:
#     # match对象
#     print("匹配内容对应位置:",i.span()) # s[0:9]即对应内容
#     print("匹配到的内容:",i.group())




