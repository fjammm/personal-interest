import requests as req
from bs4 import BeautifulSoup as bup
import pandas as pd
import re
basic_web='https://www.qidian.com/book/coverrec'
u=req.get(url=basic_web)
#print(u)验证是否访问成功
soup=bup(u.text,'lxml')
infor=soup.find_all('a')
lis=[]
for i in infor:
    lis.append(i.text.replace(" ","").replace("\n",""))
n=0
for i in lis:
    if '往期三江' in i:
        n+=1
        break
    else:
        n+=1
for i in lis[n+1::2]:
    if '起点中文网' in i:
        break
    else:
        print(i)
    with open('fengtui.txt','a') as tar:
        tar.write(i+'\n')
c=input("以上是目前起点中文三江封推的书籍目录,请参考.")
