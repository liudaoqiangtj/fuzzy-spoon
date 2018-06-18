#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: liudaoqiang
@file: studycase
@time: 2018/6/15 8:12
'''
import urllib
class HtmlDownloader(object):
	def download(self,url):
		if url is None:
			return None
		response = urllib.urlopen(url)
		if response.getcode() != 200:
			return None
		return response.read()
