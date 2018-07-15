'''
import sys
sum = 0
while True:
	try:
		line = input() #相当于sys.stdin.readlines()
	except EOFError:
		break
	else:
		print(line)
		sum += int(line)
		print(sum)
print(sum)

import sys
sum = 0
for line in sys.stdin:
	print(type(sys.stdin))
	sum += int(line)
print(sum)

import sys
for line in sorted(sys.stdin): print(line,end='')

import sys
sum = 0
for line in sys.stdin:
	print(line,end='')
	sum += int(line)
print(sum)

import sys
print(sum(int(line) for line in sys.stdin))# 函数式编程

import sys
lines = sys.stdin.readlines()
lines.sort()
for line in lines: print(line,end='')
'''
import sys
def more(text,numlines=15):
	lines = text.splitlines()#splitlines()将字符串在换行处分割
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk:
			print(line)
		if lines and input('More?') not in ['Y','y']:break
import sys
more(sys.__doc__)