import pymysql

# 连接 MySQL 数据库
conn = pymysql.connect(
    host='localhost',  # 主机名
    port=3306,         # 端口号，MySQL默认为3306
    user='root',       # 用户名
    password='2870454770', # 密码
    database='dormitory',   # 数据库名称
)
cursor = conn.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SHOW TABLES;")
 
# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
for i in cursor:
    print(i)
 

 
# 关闭数据库连接
conn.close()
