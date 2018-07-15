
# 打开关闭文件
myfile = open(filename,'w') #通用形式
try:
	...process myfile...
finally:
	myfile.close()

with open(filename) as myfile: #上下文管理器形式（线程锁），自动myfile.close()
	... process myfile ...

# 上下文管理器是个什么玩意？线程锁
# 文件对象包含迭代器，

for line in open('data.txt'): #文件对象是临时对象打开，自动关闭
	print(line,end='') #不使用文件内容中的换行符，print 会自动带换行符\n

# +模式与seek方法联合使用来实现随机的读取、写入权限
open('data.bin','wb').write(b'Spam\n') #像二进制文件对象写入必须为二进制数据
open('data.bin','wb').write('spam\n') #会报错TypeError: must be bytes or buffer, not str

#文本文件的默认是Unicode默认编码，ascii编码表个128个字符,ascii是古老的编码，还不区分字符集和编码，可以看做合二为一的东西，ascii码表示一个字符需要一个字节
#unicode严格来说是字符集，可以有多种编码，unicode默认编码用4字节表示一个编码，可以提供65536字符，基本上包含了世界上的所有语言
#字符集（char set）是字符的集合，收录了一定数量的字符，每个字符都有对应的ID值，叫码点（code point）,实际存储的时候，
#不一定是直接存储字符串的的码点，要进行转换，这个转换规则就是编码。
#utf8-8是unicode的一种变长字符编码（重点在变长），用1到6个字节编码unicode字符；ascii码其实是utf-8的子集。
#计算机硬盘默认存储的是utf-8以节省内存空间，计算机 内存存储的是Unicode字符集的码点，因此读写的时候回出现编码转换。
#chr character=>a unicode string