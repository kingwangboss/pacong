# -*- coding:utf-8 -*-
import re
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

url = "https://dc5678.com/index.php?c=content&a=list&catid=2"
req = Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
resp = urlopen(req).read().decode("utf-8")
soup = BeautifulSoup(resp,"html.parser")

nowQishu = soup.findAll("em")[0].getText()
nextQishu = soup.findAll("em")[6].getText()

num = soup.findAll("span",title=re.compile("^.+"))

nowNumArr = list()

for span in num:
    nowNumArr.append(span["title"])
numList = ['01','02','03','04','05','06','07','08','09','10',]
nowNumArr.pop(0)
for x in nowNumArr:
    numList.remove(x)
nowNumArr.insert(0,numList[0])
nowNum = " ".join(nowNumArr)
print(nowNum)


print("当前开奖号码：" + nowNum)
print("当前开奖期数：" + nowQishu)
print("下一期开奖期数：" + nextQishu)