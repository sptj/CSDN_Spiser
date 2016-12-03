#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################
# File Name: csdn.py
# Blog http://blog.csdn.net/hurmishine
# Created Time: 2016-11-28 21:50:55
########################################################
import urllib2,re
headers = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
          }
def fun(page):
    print "page "+str(page)
    req = urllib2.Request(
    url = 'http://blog.csdn.net/peoplelist.html?channelid=0&page='+str(page),
    headers = headers
    )
    response = urllib2.urlopen(req)  
    html = response.read()
    #print html
    urls=re.findall('<dd><a class="expert_name" href="(.*?)">(.*?)</a>', html, re.S)
    f=open('csdnUrl.txt','a')
    f.write('*************************#page '+str(page)+'#************************\n')
    for url in urls:
        print url[1],url[0]
        f.write(url[1]+'\t'+url[0]+'\n')
    f.write('\n')
    f.close()

if __name__=='__main__':
    for i in range(1,111):
        fun(i)
