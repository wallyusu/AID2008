'''
    练习：input输入一个学生的姓名，将该学生的成绩改为100分
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
#     name01 = input('请输入学生姓名,将其改为100分： ')
#     sql = f'update cls set score=100 where name="{name01}";'
#     cur.execute(sql)
#     db.commit() # 事务提交
# except:
#     db.rollback() # 事务回滚

# 方法2
# try:
#     name = input('请输入学生姓名： ')
#     sql = 'update cls set score=%s where name=%s;'
#     cur.execute(sql,[97,name])
#     db.commit() # 事务提交
# except Exception as e:
#     print(e)
#     db.rollback() # 事务回滚

# 方法3 批量插入数据
# l = [('Peter',16,'m',69),
#      ('Allen',18,'m',79),
#      ('joe',19,'m',90)
#      ]
# try:
#     sql = 'insert into cls (name,age,sex,score) values (%s,%s,%s,%s);'
#     cur.executemany(sql,l)
#     db.commit() # 事务提交
# except Exception as e:
#     print(e)
#     db.rollback() # 事务回滚

# 关闭游标和数据库连接
cur.close()
db.close()