#闭包Closure:内部函数中对enclosing作用域的变量进行引用
# 封装,复用
#外部函数返回内部函数，内部函数调用外部函数的“原有”参数并返回外部函数的“当前”参数
#coding:utf-8
def setpassline(passline):
	def cmp(val):
		if val >= passline:
			print('pass')
		else:
			print('failed')
	return cmp




def dec(func):
	print('call dec')
	def in_dec(*args):
		if len(args) == 0:
			return 0
		for val in args:
			if not isinstance(val,int):
				return 0
		return func(*args)
	return in_dec
#外部函数dec返回内部函数in_dec，内部函数in_dec引用外部函数参数，返回func(*args)

@dec
def my_sum(*args):
	return sum(args)

#调用装饰器dec(my_sum)等价于my_sun = dec(my_sum )
print(my_sum(1,2))