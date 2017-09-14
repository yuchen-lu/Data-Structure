# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:57:44 2017

@author: luyuche1
"""

#---location, count, iteration number, for loop range


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


count=0
#checkfirst=1

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
yolo = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = yolo('a')


for i in range(7):
    for tag in tags:
        name=tag.contents[0]
        count=count+1
        #print(count)
        if count==18:#&(checkfirst==1):
            goin=tag.get('href', None)
            #print(goin)
            html=urllib.request.urlopen(goin)
            yolo = BeautifulSoup(html, 'html.parser')
            tags=yolo('a')
            #print(tags)
            #checkfirst=1
            count=0
            break
       
        
print(name)








