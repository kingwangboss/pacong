# -*- coding:utf-8 -*-
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql.cursors

resp = urlopen("https://dc5678.com/index.php?c=content&a=list&catid=9&day=2017-05-31").read().decode("utf-8")
soup = BeautifulSoup(resp,"html.parser")
i = 0
str = ""
listspan = soup.findAll("span",title=re.compile("^.+"))
listtb = soup.findAll("tbody")

kaijiang = list()
shijian = list()
qishu = list()
for title in listspan:
    # print(title["title"]),
    if i > 9:
        # print(str)
        kaijiang.append(str)
        str = title["title"]
        i = 1
    else:
        i+=1
        if str :
            str = str + ' ' + title["title"]
        else:
            str = title["title"]
# print(listtd)
tab = listtb[0]
for tr in tab.findAll('tr'):  
    for td in tr.findAll('td')[1:2]:  
        # print(td.getText())
        qishu.append(td.getText().strip())
for tr in tab.findAll('tr'):  
    for td in tr.findAll('td')[0:1]:  
        # print(td.getText())
        shijian.append(td.getText())
# for tb in listtr:
    # print(tr)
# print(kaijiang[0])
# print(shijian[0])
# print(qishu[0])

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
        sql = 'INSERT INTO shuju (shijian, qishu, haoma) VALUES (%s, %s, %s)';
        #执行sql语句
        for (kaijiang, shijian, qishu) in zip(kaijiang,shijian,qishu):
            count = cursor.execute(sql,(shijian,qishu,kaijiang))
            print(count)
            connection.commit()
finally:
    connection.close()