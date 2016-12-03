#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################
# File Name: csdn.py
# Blog http://blog.csdn.net/hurmishine
# Created Time: 2016-11-28 21:50:55
########################################################
import urllib2,re
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
def fun(page):
    print "page "+str(page)
    req = urllib2.Request(
    url = 'http://blog.csdn.net/peoplelist.html?channelid=0&page='+str(page),
    headers = headers
    )
    response = urllib2.urlopen(req)  
    html = response.read()
    #print html
    urls=re.findall('<dd>(.*?)</dd>', html, re.S)
    #print type(urls)
    urlstr=''.join(urls)
    #print urls
    f=open('all.txt','a')
    f.write(150*'*'+'\n')
    for url in urls:
        urlstr=''.join(url)
        link=re.findall('<a class="expert_name" href="(.*?)">(.*?)</a>', urlstr,re.S)
        #print link[0][1],link[0][0],
        f.write(link[0][1]+2*'\t'+link[0][0])
        address=re.findall('<em>(.*?)</em>', urlstr,re.S)
        f.write((52-len(link[0][0]))*' ')
        if len(address)>0:
            #print address[0],
            n=len(address[0])
            f.write(address[0]+(24-n)*' ')
        else:
            f.write(24*' ')
        num=re.findall('<div class="count_l fl"><b>(.*?)</b><span>文章数</span></div>', urlstr,re.S)
        n=len(num[0])
        f.write('\t'+num[0])
        cnt=re.findall('<div class="count_l fr"><b>(.*?)</b><span>阅读数</span></div>', urlstr,re.S)
        #print cnt
        f.write('\t'+cnt[0])
        job=re.findall('<span>(.*?)</span>', urlstr,re.S)
        if job[0] !='&nbsp;':
            #print job[0],
            f.write(2*'\t'+job[0])
        f.write('\n')
        #break
    f.close();
if __name__=='__main__':
    f=open('all.txt','a')
    f.write(150*'*'+'\n')
    f.write('专家姓名\t博客链接'+44*' '+'地址'+24*' '+'博客数\t'+'访问量'+2*'\t'+'职业\n');
    f.close();
    for i in range(1,111):
        fun(i)
