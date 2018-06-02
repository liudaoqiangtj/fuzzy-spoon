#! /usr/bin/env python
# -*- coding:utf-8 -*-

try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO

#使用__future__
#from __future__ import division #但是它必须放在第一行

#用kwargs声明实例属性
class Person(object):
	def __init__(self, name, *args, **kwargs):
		self.name = name
		for k, v in kwargs.items():
			setattr(self, k, v)

p = Person('xiaoming', job='student')
# p.__dict__
# 返回{'job': 'student', 'name': 'xiaoming'}

#添加类属性count,统计创建实例的个数
class Person(object):

	count = 0
	print(count)
	#只会在类定义的时执行一次，创建实例的时候不会去执行；但是在类或实例的方法中可以修改count，
	#比如在这个__init__函数中，递增Person.count = Person.count + 1
	def __init__(self,name):
		Person.count = Person.count + 1
		self.name = name
p = Person('xm')
pp = Person('xx')
# p.count 返回1
# Person.count 返回1
#创建实例时，先调用__new__方法，然后__init__方法
#有个问题，类属性是什么时候初始化的


class Person(object):
	count = 0
	print(count)#只会在类定义的时执行一次，创建实例的时候不会去执行
	def __init__(self,name):
		Person.count = Person.count + 1
		self.name = name
	@classmethod
	def clsmethod(cls):
		print('classmethod')
# p = Person('xm')
#p.count返回1
# pp = Person('xx')
# pp.count返回2

#外部将无法访问__count属性
class Person(object):
	__count = 0
	print(__count)
	def __init__(self,name):
		Person.__count = Person.__count + 1
		self.name = name
#p = Person('xw')
#p.__count 将无法访问

#在实例方法中访问不能被外部访问的类私有属性
class Person(object):
	def __init__(self,score,name):
		self.name = name
		self.__score = score
	def get_grade(self):
		if self.__score > 90:
			return 'A'
		elif self.__score > 80 and self.__score <= 90:
			return 'B'
		else:
			return 'C'

#在class中定义的实例方法其实也是属性，它实际上是一个函数对象，因为可以动态的添加到类实例上，用到types.MethodType()
import types
class Person(object):
	def __init__(self,score,name):
		self.name = name
		self.__score = score
def fn_get_grade(self):
	if self.score >= 80:#要这样定义的函数才可以动态添加到类方法中
		return 'A'
	elif self.score < 80:
		return 'B'
	return 'C'
#p1 = Person('Bob',90)
#p1.get_grade = types.MethodType(fn_get_grade,p1,Person)
#print p1.get_grade()返回A
#p2 = Person('Alice',90)
#p2.get_grade() 将返回AttributeError: 'Person' object has no attribute 'get_grade'，因为没用给p2动态增加实例属性

#python中定义类方法
class Person(object):
	count = 0
	@classmethod
	def how_many(cls):
		return cls.count
	def __init__(self,name):
		self.name = name
		Person.count = Person.count + 1
# Person.count
# Out[248]: 0
# Person.how_many()
# Out[249]: 0
# p1 = Person('xw')#实例会得到类的方法和属性
# p1.count
# Out[251]: 1
# p1.how_many()
# Out[252]: 1

#类的继承
class Person(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
class Student(Person):
	def __init__(self, name, gender, score):
		super(Student, self).__init__(name, gender)
		self.score = score
# 函数super(Student,self)将返回父类，即Person，然后调用__init__()方法，在子类中初始化父类方法。


#类中实现Magic Method,特殊方法
#有些特殊方法是针对一个实例的，有写是对两个实例的
class Person(object):
	def __init__(self,name,gender):
		self.name = name
		self.gender = gender
class Student(Person):
	def __init__(self,name,gender,score):
		super(Student,self).__init__(name,gender)
		self.score = score
	def __str__(self):
		return '(Student: %s,%s,%d)' %(self.name,self.gender,self.score)
	__repr__ = __str__

	def __cmp__(self,other):
		if self.name < other.name:
			return -1
		elif self.name > other.name:
			return 1
		else:
			return 0
class Fib(object):
	def __init__(self,num):
		a, b, L = 0, 1, []
		for n in range(num):
			L.append(a)
			a,b = b,a+b
		self.numbers = L
	def __str__(self):
		return self.numbers
	def __len__(self):
		return len(self.numbers)

#实现有理数size运算
class Rational(object):
	def __init__(self,p,q):
		self.p = p
		self.q = q
	def __add__(self, other):
		return Rational(self.p*other.q+self.q*other.p,self.q*other.q)
	def __str__(self):
		return '%s/%s' %(self.p,self.q)#这里反斜线不是除法运算符，只是一个字符，所以print(Rational(1,3))会返回1/3，但不是
		#1’除法运算符‘3，不能直接用float(Rational(1/3)),所以需要实现float方法
	__repr__ = __str__
	def __mul__(self,other):
		return Rational(self.p*other.p,self.q*other.q)
	def __sub__(self,other):
		return Rational(self.p*other.q-self.q*other.p,self.q*other.q)
	def __div__(self,other):
		return Rational(self.p*other.q,self.q*other.p)
	def __int__(self):# int类型装换
		return self.p // self.q
	def __float__(self):
		return float(self.p) /self.q
# r1 = Rational(1,3)
# print(r1) 返回 1/3
# float(r1) 返回0.3333333333333333

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.__score = score
	@property
	def score(self):
		return self.__score
	@score.setter#score.setter是property装饰score之后的副产品
	def score(self,score):
		if score < 0 or score > 1000:
			raise ValueError('Invalid Score')
		self.__score = score
	@property
	def grade(self):
		if self.__score < 60:
			return 'C'
		elif self.__score < 80:
			return 'B'
		else:
			return 'A'
# s = Student('xw',88)
# s.score 返回 88
# s.score() 不支持这样访问
# s.score(91) 不支持这样设置，支持s.score = 91
# s.score 返回91


#类的实例可以变成可调用对象，需要实现 __call__方法
class Person(object):
	def __init__(self,name,gender):
		self.name = name
		self.gender = gender
	def __call__(self, friend):
		print('My name is %s, My friend is %s' %(self.name,self.friend))
# p = Person('xw','female')
# p('Bob') 返回 My name is xw, My friend is Bob

#将类的对象变成可调用的
class Fib(object):
	def __init__(self):
		pass
	def __call__(self,number):
		a,b,l = 0,1,[]
		for _ in range(number):
			l.append(a)
			a,b = b,a+b
		self.numbers = l
	def __str__(self):
		return str(self.numbers)
	def __len__(self):
		return len(self.numbers)
f = Fib()
# f(10) 什么也没有返回，因为在__call__方法里没有定义return
#print(f) 返回[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#print(len(f)) 返回10