#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python文件 sys.stdin 标准输入 sys.stdout 标准输出 sys.stderr标准错误
# sys.argv命令行传入参数
'''
 定义arg.py
 if __name__ == '__main__':
    print(len(sys.argv))
    for arg in sys.argv:
        print(arg)
终端输入执行命令 python arg.py 1 2 3 后，将返回
4 #表示sys.argv 接收四个参数
arg.py
1
2
3
'''
#如何创建一个utf-8或者其他编码格式的文件
import codecs
f = codecs.open('test.txt','w','utf-8')#会创建utf-8格式编码的test.txt文件
f.write(u'慕课')
f.flush()
f.close()
#将'慕课'写入到test.txt中

#linux应用层+linux内核
#每一个外设在内核中都有一个驱动程序，每一个外设在虚拟文件系统下会生成一个文件节点

#os模块操作文件，更接近于底层调用
import os
'''
os.open(filename,flag[,mode])#打开文件
flag:os.O_CREAT,os.O_RDONLY, os.O_WRONLY, os.O_RDWR
os.read(filename,buffersize) 读取文件
os.write(filename,string) 写入文件
os.lseek(fd,pos,how) 文件指针操作，类似于f.seek
os.close(fd) 关闭文件
os.access('imooc.txt',os.F_OK)#当前目录下是否存在imooc.txt文件
os.listdir('./')返回当前目录下所有文件的列表
os.remove('imooc.txt')删除文件
os.rename('imooc.txt','imooc1.txt')
os.mkdir('./test')当前目录创建目录test
os.makedirs('./test/test1/test2')创建多级目录
os.rmdir('test') test为空可以删除test目录
os.removedirs('test/test1/test2')删除多级目录
os.path.exists('./imooc.txt')是否存在文件
'''



