# -*- coding:utf-8 -*-
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://dc5678.com/index.php?c=content&a=list&catid=2"

resp = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(resp,"html.parser")

nowQishu = soup.findAll("em")[0].getText()
nextQishu = soup.findAll("em")[6].getText()

num = soup.findAll("span",title=re.compile("^.+"))

nowNumArr = list()

for n in num:
    print(n)
for span in num:
    nowNumArr.append(span["title"])
nowNum = " ".join(nowNumArr)
print(nowNum)

# print("当前开奖号码：" + nowNum)
# print("当前开奖期数：" + nowQishu)
# print("下一期开奖期数：" + nextQishu)