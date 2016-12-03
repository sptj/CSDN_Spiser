# CSDNSpiser

由于我是CSDN用户，发现最近在评选年度博客之星，官方给出了一些博客专家的信息
[http://blog.csdn.net/experts.html](http://blog.csdn.net/experts.html)
给出姓名和地址和职业，还有文章数和访问量，浏览了一会儿发现是异步加载的数据，真实的网址是[http://blog.csdn.net/peoplelist.html?channelid=0&page=1](http://blog.csdn.net/peoplelist.html?channelid=0&page=1)第一个数据是专家类型，第二个是页数（从1开始，0和1一样）就爬一下吧。


1. 1.0 爬取了所有博客专家的姓名和博客链接
2. img 爬取了所有博客专家的头像
3. 2.0 爬取了所有博客专家的所有信息，但我不是很会正则表达式，BeautifulSoup,更不用说了框架了，写得很菜
