f=open('aa.txt')
f2=open('index.html','a')
cnt=0
while True:
	line=f.readline()
	cnt=cnt+1
	if line:
		line=('').join(line)
		line=line.decode('unicode-escape').encode('utf-8')
		if cnt%2==1:
				f2.write('<a href="'+line+'"'+' target="_blank">')
		else:
				f2.write(str(cnt-1)+"\t"+line+'</a><br><br>\n')
	else:
		break
f.close()
f2.close()
print 'ok'
