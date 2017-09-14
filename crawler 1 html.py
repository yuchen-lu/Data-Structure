# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
-------crawler find number in html using BS
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
score=list()
count=0




# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_26582.html'
html=urllib.request.urlopen(url,context=ctx).read()

#print(html)

yolo= BeautifulSoup(html,'html.parser')

tags = yolo('span')
print(tags)
for tag in tags:
    score.append(tag.contents[0])
    count=count+1
  #  score.append(tag.span)
    
   # count=count+1
    
#print(sum(int(score)))
#print(count)


finalsum=list(map(int,score))




print('Count',count)
print('Sum', sum(finalsum))