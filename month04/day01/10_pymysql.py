"""
pymysql回顾
库：noveldb
表：nobel_tab
"""

import pymysql

# 1. 连接对象 游标对象
db = pymysql.connect('localhost', 'root', '123456', 'noveldb', charset='utf8')
cur = db.cursor()
# 2. 执行sql命令
ins = 'insert into novel_tab values(%s,%s,%s,%s)'
cur.execute(ins, ['战神', 'zh.com', '黑龙', '真厉害'])
# 3. 提交到数据库执行
db.commit()
# 4. 关闭游标 断开数据库的连接
cur.close()
db.close()
