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

#无参数参数的装饰器函数
import time
def log(f):
	def fn(*args,**kwargs):
		t1 = time.clock()
		r = f(*args,**kwargs)
		t2 = time.clock()
		print('call %s call time:%d' %(f.__name__(),t2-t1))
		return r
	return fn
@log
def factorial(n):
	return reduce(lambda x,y:x+y,range(1, n))
print(factorial(6))

#装饰器 封装性，不改变原有代码新增功能，
#缺点：装饰器返回的函数已经不是原有的函数，所以依赖原有函数名的代码会失效，而且装饰器还改变了原有函数的__doc__属性
#如果要让调用者看不出一个函数经过装饰器的”改造“，就需要把原函数的一些属性复制到新函数中，functools
import functools
def log(f):
	@functools.wraps(f)
	def wrapper(*args,**kwargs):
		print('call ...')
		return f(*args,**kwargs)
	return wrapper
@log
def f2(x):
	pass
print(f2.__name__)#将会打印f2

#如果没有用functools来复制
import functools
def log(f):
	#@functools.wraps(f)
	def wrapper(*args,**kwargs):
		print('call ...')
		return f(*args,**kwargs)
	return wrapper
@log
def f2(x):
	pass
print(f2.__name__)#将会打印wrapper,依赖f2函数名的代码会失效，而且wrapper不会有f2的属性

#带参数的装饰器函数
#实现带参数的装饰器函数就需要三层嵌套的函数
import time,functools
def performance(unit):
	def perf_decorator(f):
		@functools.wraps(f)
		def wrapper(*args,**kwargs):
			t1 = time.time()
			r = f(*args,**kwargs)
			t2 = time.time()
			t = (t2 - t1)*1000 if unit=='ms' else (t2-t1)
			print('call %s() in %f %s' %(f.__name__,t,unit))
			return r
		return wrapper
	return perf_decorator

@performance('ms')
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(10))
#返回结果
#call factorial() in 0.000000 ms
# 3628800

#偏函数
import functools
int2 = funtools.partial(int,base=2)
int2('1000000')
#返回64