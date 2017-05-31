# -*- coding:utf-8 -*-
import re
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

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
print('最新开奖号码:' + kaijiang[0])
print('最新开奖时间:' + shijian[0])
print('最新开奖期数:' + qishu[0])