#! /usr/bin/env python
# -*- coding:utf-8 -*-

#函数名和变量没有什么区别，只不过函数名是指向函数的变量名
from math import sqrt

def add(x,y,f):
	return f(x)+f(y)
print(add(4,9,sqrt))
z = lambda x,y:x+y
import re
def format_name(s):
	st0 = re.sub(r'.*',s[0].upper(),s)
	st = re.sub(r'.*',s[1:].lower(),s)
	return st0+st
print(list(map(format_name,['adam','LISA','barT'])))

#判断奇偶数
list(filter(lambda x:x%2==1,[1,4,6,7,9,12]))
#剔除为空的字符 \t \n \r
list(filter(lambda s:s and len(s.strip()) > 0, ['test',None,' ','str','\t','\n']))
#过滤掉1~100中平方根是整数的数
# list(filter(lambda x:isinstance(sqrt(x),int),range(1,101))) 这个不行因为sqrt()返回的值是float
list(filter(lambda x: int(sqrt(x)) ** 2 == x, range(1, 101)))
#自定义排序函数
sorted([1,3,2])
#定义返回函数的函数，这其实是个闭包
def calc_prod(lst):
	def in_prod():
		def f(x,y):
			return x*y
		return(reduce,f,lst)
	return in_prod

f = calc_prod([1,2,3,4])
print(f())
#Closure外部函数返回内部函数的情况，内部函数引用外部函数变量，内部函数的参数是外部函数参数（是一个函数）的参数
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())#将打印出9，9，9
#闭包内部函数定义不要引用任何外部函数的循环变量
#正确写法
def count():
	print('count()')
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
				print(j*j)
			return g
		r = f(i)#f内部函数不要引用循环变量
		fs.append(r)
	print(fs)
	return fs
f1, f2, f3 = count()#此时f1,f2,f3返回的是
print(f1(),f2(),f3())#1,4,9

#无参数的装饰器函数
import time
def log(f):
	def fn(*args,**kwargs):
		print('call'+f.__name__()+ctime())
		t1 = time.clock()
		r = f(*args,**kwargs)
		t2 = time.clock()
		print('call time:%d' %(t2-t1))
		return r
	return fn
@log
def factorial(n):
	return reduce(lambda x,y:x+y,range(1, n))
print(factorial(6))