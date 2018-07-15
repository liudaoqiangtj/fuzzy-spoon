
# io.StringIO 和io.BytesIO
# io.StringIO 将文件操作映射到str字符串
# io.BytesIO 将文件操作映射到内存字节缓冲区
# sys.stdout.write() =>print
# sys.stdin.readlines() => input()

import sys
from io import StringIO
buff = StringIO()
sys.stdout = buff #将stdout标准输出流重定向到buff对象, buff.getvalue() 取代print()

# print(stuff,file=filename) #可以把stuff重定向到filename
# os.popen和subprocess.Popen 管道开放重定向

import os
pipe = os.popen('python hello-in.py','w') # 'w'指对stdin进行写操作
pipe.write('Gumby\n')
pipe.close()

#subprocess.Popen 可以访问程序的输入和输出，将一个程序的输出发送到另一程序的输入；也可以用os.popen来实现一个程序的输出作为另一个程序的输入
import os
p1 = os.popen('python writer.py','r') # 'r'表示对stdout进行读操作
p2 = os.popen('python reader.py','w') # 'w'表示对stdin进行写操作

