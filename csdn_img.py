#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################
# File Name: csdn.py
# Blog http://blog.csdn.net/hurmishine
# Created Time: 2016-11-28 21:50:55
########################################################
import urllib,urllib2,re
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


def fun(page):
    print "page "+str(page+1)
    req = urllib2.Request(
    url = 'http://blog.csdn.net/peoplelist.html?channelid=0&page='+str(page),
    headers = headers
    )
    response = urllib2.urlopen(req)  
    html = response.read()
    #print html
    #<img src="http://avatar.csdn.net/E/8/5/2_duruiqi_fx.jpg" alt="img" class="expert_head">
    urls=re.findall('<img src="(.*?)" alt="img" class="expert_head"', html, re.S)
    for url in urls:
        print url
        print url[31:]
        urllib.urlretrieve(url,'CSDN_expert//%s.jpg' % url[31:])
if __name__=='__main__':
    for i in range(110,111):
        fun(i)
