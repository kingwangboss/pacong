import pymysql.cursors

#数据库链接
connection = pymysql.connect(
host='localhost',
user='root',
password='kingwangboss',
db='baiduurl',
charset='utf8mb4'
)       
try:
    #获取会话指针
    with connection.cursor() as cursor:
        #创建sql语句
        sql = "select `urlname`,`urlhref` from urls where `id` is not null"
        #执行sql语句
        count = cursor.execute(sql)
        print(count)

        result = cursor.fetchmany(size=count)
        # print(result)
        for value in result:
            print(value)
finally:
    connection.close()
