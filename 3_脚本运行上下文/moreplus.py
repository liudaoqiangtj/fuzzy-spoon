#! /usr/bin/env python
import sys
def getreply():
	if sys.stdin.isatty(): #如果sys.stdin 是控制台
		return input('?')
	else:
		if sys.platform[:3] == "win":
			import msvcrt
			msvcrt.putch(b'?')
			key = msvcrt.getche() #使用windows控制台工具
			msvcrt.putch(b'\n') #getch()方法不能回应键
			return key
		else:
			assert False,'platform not supported'
			#linux?:open('/dev/tty').readline()[:-1]

def more(text, numlines=10):
	lines = text.splitlines()
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk: print(line)
		if lines and getreply() not in [b'y',b'Y']:break

if __name__ == '__main__': #运行时执行，导入时不执行
	if len(sys.argv) == 1:
		more(sys.stdin.read())  #在stdin页没有输入数据
	else:
		more(open(sys.argv[1]).read()) #其他文件名参数