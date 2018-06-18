#! /usr/bin/env python
# -*- coding: utf-8 -*-




'''
URL容器管理器：管理待抓取URL集合和已抓取的URL集合
实现方式：
内存，Python内存，待抓取URL集合：set(),已抓取URL集合：set()
关系数据库，MySQL,urls(url, is_crawled)
缓存数据库，redis,待抓取URL集合：set，已抓取URL：set

网页下载器：将互联网上URL对应的网页下载到本地的工具
urllib2 Python官方基础模块
requests库 第三方模块

import urllib2
url = 'http://www.baidu.com'
response = urllib2.urlopen(url)
print(response.getcode()) #
cont = response.read()

import urllib2
url = 'http://www.baidu.com'
#创建Request对象
request = urllib2.request(url)
#添加数据
request.add_data('a','1')
#添加http的header
request.add_header('User-Agent','Mozilla/5.0')
#发送请求获取结果
response = urllib2.urlopen(request)

import urllib2,cookielib
#创建cookie容器
cj = cookielib.CookieJar()
#创建1个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# 给urllib2安装opener
urllib2.install_opener(opener)
#使用带有cookie的urllib2的访问网页
response = urllib2.urlopen("http://www.baidu.com/")

网页解析器
正则表达式模糊匹配
BeautiSoup 第三方插件
lxml 第三方插件
html.parser 自带
DOM 树，文档对象模型，Document Object Model


登录，验证码，Ajax, 服务器防爬虫，多线程，分布式

'''