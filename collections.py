#! /usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
User = namedtuple('User',['name','age','height','edu'])#namedtuple将创建一个类，第一个参数是类名，第二个参数是列表表示属性
user_tuple = ('Bobby',28,175)
user = User(*user_tuple,'master')#User类实例化对象user
print(user.name,user.age,user.height,user.edu) #返回Bobby 28 175 master
user_dict = {
	'name':'bobby',
	'age':29,
	'height':175
}
user = User(**user_dict,edu='master')
user_info_dict = user._asdict()
print(user.name,user.age,user.height,user.edu)#返回Bobby 28 175 master
#分别用*user_tuple和**user_dict作为参数来实例化对象，这对应于*args,**kwargs
#namedtuple类的_asdict()方法返回一个dict，并且按键排序
#user_info_dict内容是
# OrderedDict([('name', 'bobby'),
#              ('age', 29),
#              ('height', 175),
#              ('edu', 'master')])
name,age,*other = user
#namedtuple继承了tuple类，tuple支持分组拆包；namedtuple创建的类的实例化对象支持分组拆包’一般类的对象不可以拆包的，
#但是namedtupled实例化的对象是可以的


from collections import defaultdict
#统计出现的次数
user_dict = {}
users = ['bobby1','bobby2','bobby3','bobby1','bobby2','bobby2']
for user in users:
	if user not in user_dict.keys():#user_dict.keys()可以用字典名替换
		user_dict[user] = 1
	else:
		user_dict[user] += 1
print(user_dict)#返回{'bobby1': 2, 'bobby2': 3, 'bobby3': 1}
#替换代码一
user_dict = {}
users = ['bobby1','bobby2','bobby3','bobby1','bobby2','bobby2']
for user in users:
	user_dict.setdefault(user,0)#设置字典键默认值
	""" D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
	#setdefault如果不存在默认值则设置 D[k]=d,如果k 是D的键，则获取D.get(k,d)
	user_dict[user] += 1
print(user_dict)#返回{'bobby1': 2, 'bobby2': 3, 'bobby3': 1}
#替换代码二，好处是代码量低，不容易出错，会自动创建默认值
default_dict = defaultdict(int)#传入可调用对象,如果键不存在，则赋给键一个默认值，int默认值是0，list默认会创建空数组
users = ['bobby1','bobby2','bobby3','bobby1','bobby2','bobby2']
for user in users:
	default_dict[user] += 1
print(default_dict)#返回{'bobby1': 2, 'bobby2': 3, 'bobby3': 1}
#defaultdict以默认方式初始化键值对
def gen_default():
	return {
		'name':'',
		'nums':0
	}
default_dict = defaultdict(gen_default)#函数是可调用对象，__missings__函数
print(default_dict)#默认创建{'group1': {'name': '', 'nums': 0}} 字典


from collections import deque
#deque相对于list的优势是线程安全，有GIL线程安全锁
# deque(iterable)#传入可迭代对象，tuple,list,dict对象
user_list = deque(['bobby1',29,175])#print(user_list)返回deque(['bobby1', 29, 175])
user_tuple = deque(('bobby1',29,175))#print(user_tuple)返回deque(['bobby1', 29, 175])
user_dict = deque({'bobby1':25,'bobby2':28})#print(user_dict)返回deque(['bobby1', 'bobby2'])，即字典键值的双端队列
#deque的浅copy


from collections import Counter
users = ['bobby1','bobby2','bobby3','bobby1','bobby2','bobby2']
user_counter = Counter(users)
#user_counter是Counter({'bobby1': 2, 'bobby2': 3, 'bobby3': 1})，统计列表中元素出现的次数
#Counter常用方法update,most_common()


from collections import OrderedDict
user_dict = OrderedDict()
user_dict['b'] = 'bobby2'
user_dict['a'] = 'bobby1'
user_dict['c'] = 'bobby3'
print(user_dict)
#会按照输入顺序打印出来结果
#OrderedDict([('b', 'bobby2'), ('a', 'bobby1'), ('c', 'bobby3')])
#python3中dict默认是有序的



