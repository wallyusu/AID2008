'''
    插入二进制图片
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

# 数据操作(插入一张图片到数据库)
# with open('timg.jpg','rb') as f:
#     data = f.read()
#
# sql = 'update cls set image=%s where id=1;'
# cur.execute(sql,[data])
# db.commit()

# 提取二进制文件
# sql = 'select image from cls where id=1;'
# cur.execute(sql)
# data=cur.fetchone()
# with open('王祖贤.jpg','wb') as a:
#     a.write(data[0])

# 关闭游标和数据库连接
cur.close()
db.close()