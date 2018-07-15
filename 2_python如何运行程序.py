'''
python是解释器+支持的库，是一个软件包。python解释器可由C语言实现，也可由Java类实现。
python编译时：源代码生成字节码（pyc文件)(python字节码不是机器的二进制代码)，转发到“虚拟机”（Python Virtual Machine,PVM）。
通过字节码会提高python的执行速度。

python 模块搜索优先级：主目录（文件所在目录）,PYTHONPATH目录（从左至右搜索），标准链接库目录，任何.pth文件的内容；可以将.pth文件放在安装目录的
顶层（C:\Python27）或者在标准库所在位置的sitepackage子目录中（C:\Python27\Lib\sitepackages）来扩展模块搜索路径。

sys.exc_info函数会返回一个元组，含有最近异常的类型
import traceback,sys
def grail(x):
	raise TypeError('already got one')
try:
	grail('arthur')
except:
	exc_info = sys.exc_info()
	print(exc_info[0])
	print(exc_info[1])
	traceback.print_tb(exc_info[2])

os.sep python运行平台锁采用的目录分隔符号，window下是“\\” 两个反斜线，unix是斜线"/"；os.pathsep 提供了目录列表中分隔目录的字符，
POSIX系统中是“:”，windows系统是“;”，os.path.split(os.sep) 分解平台的目录，不依赖于平台。
os.path.split ，os.path.join，这两个命令都是可移植的。
windows平台下
os.path.join(r'C:\temp','output.txt') #返回'C:\\temp\\output.txt' 合并目录和文件
os.path.split(r'C:\temp\data.txt') #返回('C:\\temp', 'data.txt') 分割目录和文件
name = r'C:\temp\data.txt'
os.path.dirname(name) #返回'C:\\temp' 是os.path.split的目录
os.path.basename(name) #返回 'data.txt' 是os.path.split的文件
os.path.splitext(r'C:\PP4thEd\Examples\PP4E\Pydemos.pyc')#返回('C:\\PP4thEd\\Examples\\PP4E\\Pydemos', '.pyc')
os.path.splitext 剥离了文件的扩展名（最后一个.后面的内容）

pn = r'C:\PP4thEd\Examples\PP4E\PyDemos.pyc'
dirname = os.path.dirname(pn)
basename = os.path.basename(pn)
os.path.join(dirname,basename)#返回'C:\\PP4thEd\\Examples\\PP4E\\PyDemos.pyc'
os.path.splitext(pn) #返回('C:\\PP4thEd\\Examples\\PP4E\\PyDemos', '.pyc')

os.sep.join(pn.split(os.sep)) #返回'C:\\PP4thEd\\Examples\\PP4E\\PyDemos.pyc' 用到str.join方法
os.path.join(*pn.split(os.sep)) #返回'C:PP4thEd\\Examples\\PP4E\\PyDemos.pyc'，os.path.join要传入多参数（因此用了*)

pn = 'C:\\temp\public/files/index.html' #混合了Unix和Windows分隔符，用normpath根当前平台分割
#返回'C:\\temp\\public\\files\\index.html'
os.path.abspath(r'PP4E\dev') ，#目录的绝对路径
os.path.abspath(r'C:\temp\spam.txt') #文件的绝对路径

os模块允许在python执行shell命令；os.getcwd获取脚本启动目录

py脚本运行时，Python会把脚本所在路径添加到模块搜索路径sys.path的最前面，从而脚本能看到所在目录的所有文件，因为python搜索路径
最先从文件所在目录开始搜索。

#命令行参数 sys.argv 在命令行键入的启动参数，将其作为脚本的输入，以列表形式返回
def getopts(argv):
	opts = {}
	while argv:
		if argv[0][0] == '-':
			opts[argv[0]] = argv[1]
			argv = argv[2:]
		else:
			argv = argv[1:]
	return opts
if __name__ == '__main__':
	from sys import argv
	myargvs = getopts(argv)
	if '-i' in myargvs:
		print(myargvs['-i'])
print(myargvs)
存为testargv.py
在testargv.py所在cwd,输入命令行参数：python testargv.py -i data.txt -o results.txt将返回
data.txt
{'-i': 'data.txt', '-o': 'results.txt'}

os.environ 是shell中命名的变量，程序运行时并传给脚本。
#! /usr/bin/env python 文件运行时，操作系统会将文件内容发送至首行#！后面的解释器上，env的作用就是操作系统会根据
你的环境变量定位Python解释器。
os.system('python echoenv.py') #执行脚本进程。
子进程始终从它的父进程那里继承环境变量设置，子进程由如下方式启动，Unix下的os.spawnv，os.fork/exec，或者所有平台下的
os.popen,os.system,subprocess。

标准流 sys.stdin,sys.stdout,sysstderr
标准流是预先打开的文件对象，在python启动时自动连接到程序，print和input函数实际上只是标准输出/输入流的接口
#teststreams.py
def interact():
	print('Hello stream')
	while True:
		try:
			reply = input('Enter a number')
		except EOFError
			break
		else:
			num = int(reply)
			print("%d squared is %d" %(num,num**2))
	print('bye')
if __name__ == '__main__':
	import sys
	interact()
shell语法 "> filename" 输出重定向到文件，"< filename" 输入重定向到文件输入
python teststreams.py < input.txt > output.txt,其中input.txt内容是 6\n8
用管道（pipe）链接程序，shell "|" 管道操作
windows下文件结束符为组合键Ctrl-Z,在Unix下是Ctrl-D.
adder.py 1 将输入的数字相加
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

adder.py 2 将输入的数字相加
import sys
sum = 0
for line in sys.stdin: sum += int(line)
print(sum)

adder.py 3  将输入的数字相加
import sys
sum = 0
for line in sys.stdin: sum += int(line)
print(sum)

adder.py 4 将输入的数字相加
import sys
print(sum(int(line) for line in sys.stdin))# 函数式编程

sorter.py 1 将输入的数字排序
import sys
for line in sorted(sys.stdin): print(line,end='')

sorter.py2 将输入的数字排序
import sys
lines = sys.stdin.readlines()
lines.sort()
for line in lines: print(line,end='')

more.py 分页程序
#分割字符串或文本文件并交互式地进行分页
def more(text,numlines=15):
	lines = text.splitlines()#splitlines()将字符串在换行处分割
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk:
			print(line)
		if lines and input('More?') not in ['Y','y']:break
if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		more(sys.stdin.read())
	else:
		more(open(sys.argv[1]).read())

实现stdin接收输入并利用控制台作为用户交互
执行C:\Users\daoqi>python teststreams.py < input.txt | python more.py，DOS输出
Hello stream world
Enter a number>8 squared is 64
Enter a number>6 squared is 36
Enter a number>Bye
more.py 调用input函数从stdin读取用户的交互输入，另一方面它从stdin中读取输入文本,这意味着stdin要同时接收控制台交互输入
和输入文本；当stdin被重定向到管道时就不能继续从控制台读取用户交互输入，此时它只能从管道符获取输入。所以虽然程序可以幸运执行，但是他是有问题的。
使用特殊的接口从键盘而非标准输入，直接读取用户输入。在windows下，python标准库msvcrt模块提供了该功能。
moreplus.py脚本不带参数调用时它对标准输入流进行分页，并且利用底层平台相关的工具实现用户交互。
moreplus.py
import sys
def getreply()"
	#读取交互式用户的回复键，即使stdin重定向到某个文件或者管道
	if sys.stdin.isatty(): #如果stdin是控制台
		return input('?')  #从stdin读取回复行数据
	else:
		if sys.platform[:3] == 'win': #如果stdin重定向,不能用于询问用户
			import msvcrt
			msvcrt.putch(b'?')
			key = msvcrt.getche()
			msvcrt.putch(b'\n')
			return key
		else:
			assert False,'platform not supported'
			#linux?:open('/dev/tty').readline()[:-1]
def more(text,numlines=15):
	#page multiline string to stdout
	lines = text.splitlines()
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk:print(line)
		if lines and getreply() not in [b'y',b'Y']:break
if __name__ == '__main__':
	if len(sys.argv) == 1:
		more(sys.stdin.read())
	else:
		more(open(sys.argv[1]).read())

'''