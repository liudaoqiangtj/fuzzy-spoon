#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: liudaoqiang
@file: studycase
@time: 2018/6/14 7:11
'''
import urllib2,cookielib,sys
sys.path.append(r'F:\anaconda\lib\site-packages')
print(sys.path)
# import bs4
url = "http://www.baidu.com/"
res1 = urllib2.urlopen(url)
print(res1.getcode())
print(len(res1.read()))

request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
res2 = urllib2.urlopen(request)
print(res2.getcode())
print(len(res2.read()))

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
res3 = urllib2.urlopen(url)
print(res3.getcode())
print(res3.read())