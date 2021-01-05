'''
练习： 创建一个数据库 dict
      创建一个数据表 words
      id    word    mean
      将dict.txt单词本中单词插入到该数据表
'''
import pymysql
import re

# 生成数据库连接对象,连接数据库
# db_dict = {'host':'localhost',
#            'port':3306,
#            'user':'root',
#            'password':'123456',
#            'database':'stu',
#            'charset':'utf8'
#            }
#
# db = pymysql.connect(**db_dict)

# 生成游标  游标：操作数据库数据,获取操作结果的对象
# cur = db.cursor()

# 写操作示例 insert delete update
# try:
#     file = open('dict.txt', 'r')
#     for word in file:
#         # 提取单词和解释
#         tmp = word.split(' ',1) # split对单词和解释做切割,切一次
#
#         sql = 'insert into dict.words (word,mean) values (%s,%s);'
#         cur.execute(sql,[tmp[0],tmp[1].strip()]) # strip()去除解释前的所有空格键
#     file.close()
#     db.commit() # 事务提交
# except Exception as e:
#     print(e)
#     db.rollback() # 事务回滚

# 方法2：
# 使用executemany ---> [(word,mean),(),...]
# l = [] # 存储单词
# for line in file:
#     tup = re.findall(r"(\w+)\s+(.*)",line)
#     l.append(tup[0])
# try:
#     sql = "insert into words (word,mean) values (%s,%s);"
#     cur.executemany(sql,l)
#     db.commit()
# except:
#     db.rollback()


# 关闭游标和数据库连接
# cur.close()
# db.close()

"""
作业：1. 数据管理部分进行 函数 语句 知识点的整理
     2. 练习没有做出来的 做一下
"""