import pymysql.cursors

#数据库链接
connection = pymysql.connect(
host='119.23.206.70',
user='root',
password='07943688365',
db='pk10',
charset='utf8mb4'
)
try:
    #获取会话指针
    with connection.cursor() as cursor:
        #创建sql语句
        # sql = "select `shijian`,`qishu`,`haoma` from shuju where `id` is not null"
        sql = "select `shijian`,`qishu`,`haoma` from shuju where `qishu`= ' 619127'"
        #执行sql语句
        count = cursor.execute(sql)
        print(count)

        result = cursor.fetchmany(size=count)
        # print(result)
        for value in result:
            print(value)
finally:
    connection.close()
