#--coding:utf-8--
import re
f=open("all.txt","r")
f1=open('aa.txt','a')
while True:
    line=f.readline()
    if line:
    	#print (line)
    	#p = re.compile(r'http:\\/\\/blog.csdn.net\\/\w+\\/article\\/details\\/\d+')
    	p = re.compile(r'"url":".*?"')
    	link=p.findall(line)
    	#print(link)
    	s=("").join(link)
    	link=s[7:-1]
    	print (link)
    	title=re.compile(r'"title":".*?"')
    	t= title.findall(line)
    	s=("").join(t)
    	print (s[9:-1])
    	s=s[9:-1]
    	f1.write(link+'\n'+s+'\n')
    	print(repr(s))
    else:
    	break
print ("GG")
f.close()
f1.close()
