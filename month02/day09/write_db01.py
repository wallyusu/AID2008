'''
    数据库写操作示例
    1.不支持事务的引擎 execute 会直接执行语句
    2.支持事务的引擎（InnoDB),执行写操作会默认开启事务
'''
import pymysql

# 生成数据库连接对象,连接数据库
db_dict = {'host':'localhost',
           'port':3306,
           'user':'root',
           'password':'123456',
           'database':'stu',
           'charset':'utf8'
           }

db = pymysql.connect(**db_dict)

# 生成游标  游标：操作数据库数据,获取操作结果的对象
cur = db.cursor()

# 写操作示例 insert delete update
# try:
#     sql = 'update cls set score=100 where id=1;'
#     cur.execute(sql)
#     db.commit() # 事务提交
# except:
#     db.rollback() # 事务回滚

# 读取数据库内容 select
sql = 'select name,age,score from cls where score > 80;'
cur.execute(sql) # cur类似一个容器

# for row in cur:
#     print(row) # 得到的都是元组形式
# 查询第一个结果
# one = cur.fetchone()
# print(one)
# 查询多个结果
# many = cur.fetchmany(3)
# print(many)
# 查询所有结果
# all = cur.fetchall()
# print(all)

# 关闭游标和数据库连接
cur.close()
db.close()