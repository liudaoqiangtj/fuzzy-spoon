
#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: liudaoqiang
@file: studycase
@time: 2018/5/30 8:04
'''

class Dynamo(object):
	def __init__(self, size):
		self.size = size

	def __getattribute__(self, key):
		# print('call getattribute')
		if key == 'color':
			return 'COLOR'
		else:
			raise AttributeError('getattribute')

	def __getattr__(self, key):
		# print('call getattr')
		# if key != 'color':
		#	return 'COLOR_color'
		# else:
		return AttributeError('getattr')
d = Dynamo(1)
#d.color
#Out[12]: 'COLOR'
#d.colorR
#Out[13]: AttributeError('getattr')
#d.size
#Out[14]: AttributeError('getattr')
#这可以说明，同时定义了__getattribute__和__getattr__时，无论属性是否存在时都会调用getattribute方法，虽然存在属性size但没有满足key=='color'
#会调用__getattr__返回AttributeError('getattr')
#而不存在时d.colorR则直接去调用__getattr__

'''
当只定义了__getattribute__方法
'''
class Dynamo(object):
	def __init__(self,size):
		self.size = size
	def __getattribute__(self, key):
		#print('call getattribute')
		if key == 'color':
			return 'COLOR'
		else:
			return 'getattribute'

	#def __getattr__(self, key):
		#print('call getattr')
		#if key == 'color':
		#	return 'COLOR_color'
		#else:
			#return AttributeError('getattr')

# d = Dynamo(1)
# d.size
# Out[35]: 'getattribute'
# d.color
# Out[36]: 'COLOR'
# d.colorR
# Out[37]: 'getattribute'
#只定义了__getattribute__方法，只有查看属性key=='color'时才会有return COLOR，即时已有属性size也会return getattribute
#查找不存在的属性colorR后返回return getattribute


'''
只定义了__getattr__方法
'''
class Dynamo(object):
	def __init__(self,size):
		self.size = size
	#def __getattribute__(self, key):
		#print('call getattribute')
	#	if key == 'color':
	#		return 'COLOR'
	#	else:
	#		return 'getattribute'

	def __getattr__(self, key):
		#print('call getattr')
		if key == 'color':
			return 'COLOR_color'
		else:
			return AttributeError('getattr')
# d.size
# Out[40]: 1
# d.color
# Out[41]: 'COLOR_color'
# d.colorR
# Out[42]: AttributeError('getattr')
#只定义了__getattr__方法与只定义了__getattribute__方法略有不同，前者可以返回已有属性size，
# 后者在查询size时会返回return 'getattribute'
