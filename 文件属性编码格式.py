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




