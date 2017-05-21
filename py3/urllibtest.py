# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import pymysql.cursors

resp = urlopen("https://baike.baidu.com/").read().decode("utf-8")
soup = bs(resp,"html.parser")
listUrls = soup.findAll("a",href=re.compile("^/fenlei/"))
# print(listUrls)
for url in listUrls:
    print(url.get_text(),"<---->","https://baike.baidu.com"+url["href"])

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
            sql = "insert into `urls` (`urlname`,`urlhref`) values(%s,%s)"
            #执行sql语句
            cursor.execute(sql,(url.get_text(),"https://baike.baidu.com"+url["href"]))
            #提交
            connection.commit()
    finally:
        connection.close()
