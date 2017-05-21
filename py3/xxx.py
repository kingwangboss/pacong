import re
str = '<td>2017-05-21 09:07:50</td>'

info = re.findall(r'\d+',str)
print(info)