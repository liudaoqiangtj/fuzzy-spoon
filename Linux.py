'''
linux 主分区+扩展分区最多四个分区，扩展分区可以划分逻辑分区，逻辑分区号只能从5开始，可以有多个逻辑分区。
原因是MBR格式只能有4条主分区记录，为了分出更多的区只能将一个主分区当成扩展分区，在其中分出更多的逻辑分区。

/ 根分区 swap 分区
swap分区（交换分区，功能类似于windows系统的虚拟内存，内存4G内swap分区是内存的两倍，内存大于4G，swap分区设置成跟内存一样大，
当Linux内存用尽时会用swap分区补充。虚拟内存是计算机内存管理的一种技术，它使得应用程序认为它拥有连续的可用的内存。windows中
即使 物理内存没有用完也会去用到虚拟内存，而Linux只有当物理内存用完才会用动用虚拟内存（swap分区）。
swap是linux直接调用的，不需要挂载点（盘符）

/boot (启动分区，200MB)

硬盘接口SATA IDE SICS，Linux中如果只有一个SATA盘，一个分区，那么分区就是sda1；如果有多个分区那就是sda1/sda2/sda3 ;
如果有两个SATA接口的硬盘，那么就是识别为sda,sdb，它们的分区一般是sda1/sda2/sda3,sdb1/sdb2/sdb3
sda1 表示第一块硬盘的第一个分区

将文件系统和硬盘分区关联的过程叫做挂载，就是建立一个挂载点（盘符），是用户访问硬盘空间的入口。Linux用目录作为盘符，windows用大写字母作为盘符。

硬件设备文件名
/dev/hd[a-d] IDE硬盘
/dev/sd[a-p] SCSI/SATA/USB硬盘
/dev/cdrom或/dev/hdc 光驱
/dev/fd[0-1] 软盘
/dev/lp[0-2]打印机(25针)
/dev/usb/lp[0-15] 打印机（USB）
/dev/mouse 鼠标

windows下 分区，格式化，分配盘符就可以使用；Linux格式化就是把文件系统写入列表，将磁盘分区分成等大小的块并建立i节点.

Linux常用目录作用
etc 配置文件目录，boot启动目录，lib 系统库，bin、sbin和usr/bin、usr/sbin都是用来保存系统命令的，bin、sbin下保存的命令普通用户可以执行，
usr下的bin/sbin保存的命令是root可以使用的命令，home普通用户的家目录,超级用户root,mnt 系统挂载目录，
proc和sys目录不能直接操作，这两个目录保存的是内存的挂载点。

ln -s [原文件(绝对路径)] [目标文件] 生成文件软链接，ln [原文件(不一定绝对路径)] [目标文件]；分区的文件索引表，
硬链接是对应分区上同一i节点（inode），相当于是访问一块存储空间的两个个接入点，就像是教室的前门和后面一样，都是访问一个教室空间。
删除原文件，通过硬链接还可以访问文件。
软连接类似于Windows快捷方式，软链接拥有自己的I节点和block块，软链接文件与原文件有不同的文件索引表，软链接和原文件会访问不同的
存储块，只不过软链接文件存储块存储的是原文件的存储位置。软链接的执行权限都是rwxrwxrwx,修改原文件或软链接文件另一个都会改变，
删除原文件，软链接不能使用

cp [选项] [源文件或目录] [目标目录]，选项 -r 复制目录，-p 连带文件属性复制，-d 若源文件是链接文件，则复制链接属性，
-a 相当于 -pdr就是(-all)
mv [源文件或目录] [目标目录] 剪切或改名

文件搜索命令 locate 文件名
updatedb更新数据库
locate命令所在配置文件 /etc/updatedb.conf
PRUNE_BIND_MOUNTS = "yes" 开启搜索限制；PRUNEFS = 搜索时，不搜索的文件系统；PRUNENAMES = 不搜索的文件类型；
PRUNEPATHS = 不搜索的文件路径

命令搜索命令 whereis which ；其他命令类似命令 whoami whatis
whereis 只能搜索系统命令，选项： -b 可执行命令， -m查看帮助文档
which 搜索命令还能显示别名；
echo $PATH ,whereis 和which搜索命令依赖PATH所列出的路径。

文件搜索命令 find [搜索范围] [搜索条件]，find命令缺点是比较耗费系统资源；
举个栗子 find / -name install.log在根目录下搜索install.log
linux通配符：*匹配任意内容；？匹配任意一个字符；[]匹配括号内的字符
find /root -iname install.log # -iname 不区分大小写
find /root -user root 搜索所有者root的文件
find /root -nouser 没有所有者的垃圾文件；注意根目录下的proc和sys中包含内核产生的文件可能没有所有者，但不是垃圾文件；外来设备文件
有可能没有所有者，但也不是垃圾文件

find /var/log/ -mtime +10 #查找10天前修改的文件；
-10 10天内修改的文件
10 10天当天修改的文件
+10 10天前修改的文件
atime 文件访问时间；ctime 改变文件属性； mtime 修改文件内容

find . -size 25k #查找当前目录下大小是25k的文件
-25k #小于25k
+25k #大于25k
注意不能用大写的K，同样的搜索兆字节大写的文件只能用大写的"M"，而不能用小写的“m”.

find /root inum 262147  #搜索/root目录下i节点262147的文件
find /etc -size +20k -a -size -50k #搜索/etc目录下大于20k小于50k的文件，-a and 逻辑与，-o or 逻辑或
find /etc -size +20k -a -size -50k -exec ls -lh {} \;#查找/etc/目录下，大于20k且小于50k的文件，并显示详细信息，
返回结果：-rw-r--r--. 1 root root 31K 1月   3 00:29 /etc/sysconfig/network-scripts/network-functions-ipv6

-exec 命令 {} \; 是标准格式，再举个栗子：
find /root -inum 262421 -exec rm -rf {} \; 在/root目录下找到i节点262421文件并删除

grep [选项] 字符串 文件名 #在文件中当中匹配符合条件的字符串：
-i 忽略大小写 -v 排除指定字符串

find 查找文件名用通配符匹配，grep 在文件中搜索字符串用正则表达式匹配

帮助命令man ,帮助命令是分等级的。举个栗子，man 5 passwd 查看等级5的passwd帮助；man -f passwd（相当于whatis passwd），
查看passwd有什么等级的帮助;如果命令有多个等级的帮助，不添加等级号会默认提供最小等级的帮助。
man -k passwd 不仅会返回passwd命令有什么等级的帮助也会返回含有passwd关键字的其他命令的帮助信息，还有帮助文件中含有passwd关键字的信息。
命令 --help 选项帮助
help 命令，只能是shell内部命令，只要whereis 命令，找不到执行文件就说明是内部命令，比如whereis ls
返回ls: /usr/bin/ls /usr/share/man/man1p/ls.1p.gz /usr/share/man/man1/ls.1.gz，有执行文件ls: /usr/bin/ls，不是内部命令
info 命令：- 回车：进入子帮助页面（带有*号标记），- u 进入上层页面， - n 进入下一个帮助小节，- p 进入上一个帮助小节， - q 退出

zip 压缩文件名 源文件；zip -r 压缩文件名 压缩目录；unzip 压缩文件
gzip 源文件 #源文件会消失，压缩为.gz；gzip -c 源文件 > 压缩文件 #会保留源文件
gzip -r 目录 #压缩目录下所有的子文件，但是不能压缩目录
gzip -d 压缩文件 #解压缩文件; gunzip 压缩文件 #解压缩文件;gunzip -r 压缩目录 #解压缩目录
bzip2 源文件 #压缩为.bz2,不保留源文件；bzip2 -k 源文件 #压缩之后保留源文件；bzip2命令不能压缩目录
bzip2 -d 压缩文件 #解压缩文件，bunzip2 压缩文件 # 解压缩文件
tar -cvf 打包文件名 源文件，选项-c:打包，-v显示过程，-f指定打包后的文件名，举个栗子，tar -cvf longla.tar longla
tar -xvf 打包文件名，解打包，tar -xvf longla
.tar.gz、.tar.bz2 是先打包为.tar格式，再压缩为.gz格式
tar -zcvf 压缩包名.tar.gz 源文件，-z 压缩为.tar.gz格式
tar -zxvf 压缩包名.tar.gz ，-x 解压缩.tar.gz格式
tar -jcvf 压缩包名.tar.bz2, -z压缩为.tar.bz2格式
tar -jxvf 压缩包名.tar.bz2 ,-x解压缩.tar.bz2
tar -jxvf jp.tar.bz2 -C /tmp/ 指定解压缩到tmp目录下
tar -zcvf /tmp/test.tar.gz jp anaconda-ks.cfg 压缩多个文件到tmp目录下
tar -ztvf test.tar.gz 查看但不解压文件

shutdown [选项] 时间，-c取消前一个关机命令，-h关机，-r重启
shutdown -r 05:30 & 计算机后台在05:30执行；shutdown -r now
halt，poweroff,init 0 关机
reboot,init6 重启
系统运行级别，0关机，1单用户，2不完全多用户，不含NFS服务，3完全多用户，4未分配，5图形界面，6重启
init 5启动图形界面，runlevel 查看系统运行级别
linux中，大写X指代图形界面
cat /etc/inittab中最后一行id:3:initdefault表示开机后默认的运行级别，默认是完全多用户
logout退出登录

挂载，分配盘符，是不是新设备只有挂载后才能打开设备内容？
mount #查询系统中已经挂载的设备；mount -a #依据配置文件 /etc/fstab的内容，自动挂载
mount [-t 文件系统] [-o 特殊选项] 设备文件名 挂载点；-t 文件系统：加入文件系统类型来指定挂载的类型，可以ext3/ext4/
iso9660(光盘专用)，-o 特殊选项：可以指定挂载的额外选项
mount -o remount,noexec /home/ ，将/home/分区权限修改为没有不可执行，不要修改分区的执行权限！
mkdir -p /mnt/cdrom/ 创建挂载点（挂载点要求是空目录）
mount -t iso9660 /dev/sr0/ /mnt/cdrom/ #将光盘/dev/sr0挂载到 /mnt/cdrom
挂载的默认权限是rw,但是被压制的光盘不支持写入，所以挂载后的权限是只读的
umount /mnt/cdrom/ 光盘用完之后要卸载,不能在/mnt/cdrom/目录下执行卸载命令
fdisk -l #查看U盘设备文件名
U盘一般是顺着硬盘的设备名，硬盘为sda1,U盘是sdb1。
Linux使用Windows的数据是通过网络传输方法，而不是将windows的NTFS系统挂载到linux盘符下，因为windows下的NTFS系统挂载到Linux
下是只读的。

查看用户登录命令
w 查看系统已经登录的用户
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1                      五01    4days  0.09s  0.09s -bash
root     pts/0    192.168.136.1    20:11    7:47m  0.46s  0.46s -bash
root     pts/1    192.168.136.1    07:31    7.00s  0.17s  0.12s w
USER:登录的用户名；TTY:登录终端；FROM:从哪个IP登录；LOGIN@:登录时间；IDLE:闲置时间；
JCPU:指的是和该终端连接的所有进程占用的时间，这个时间里并不包括过去的后台作业时间，但却包括当前正在运行的后台作业所占用的时间；
PCPU：是指当前进程所占用的时间；
WHAT：当前正在运行的命令
who 用户名，命令输出：
-用户名
-登录终端
-登录时间（登录时间来源IP地址）
last 查看所有所有用户的登录时间和重启时间，last命令默认是读取/var/log/wtmp 文件数据

shell 概述，界面系统级程序，命令解释器
接收命令，翻译成二进制，发送给内核，内核调用硬件
C Shell ，Bourne Shell，这两种语法不兼容
Bourne 家族主要包括sh/ksh/Bash/psh/zsh;linux中的标准shell是Bash,Linux支持的所有shell都可以在/etc/shells下看到
C家族主要包括：csh/tcsh
echo $SHELL 返回 /bin/Bash
父界面shell，子界面shell，父shell中可以调用子shell

echo -e [内容] #允许在内容加入一些反斜杠\字符
echo -e "h\te\tl\tl\to" #返回h	e	l	l	o，中间会插入制表符
echo -e "\x68\t\x65\t\x6c\t\x6c\t\x6f\t" #返回h	e	l	l	o
linux不支持英文的感叹号 !作为echo输出
echo -e "\e[1;31m嫁人就要加凤姐！\e[0m" # 有颜色的输出

脚本执行
赋予执行权限
chmod 755 hello.sh
./hello.sh
通过Bash调用脚本执行
bash hello.sh

别名与快捷键
alias 查看系统已经生效的别名
alias ls='ls --color=never';alias mv='mv -i'(-i系统询问确认)
vi ~/.bashrc 要让别名永久生效，写入环境变量配置文件，
unalias 别名  删除别名
别名优先级高于系统内部命令，外部命令。
Ctrl-U 从光标所在位置删除到行首；Ctrl-C强制终止当前命令；Ctrl-L 清屏；Ctrl-A 光标移动到命令行首；
Ctrl-E 光标移动到命令行尾；Ctrl-Z 把命令放入后台（尽量不要放入后台）；Ctrl-R 把历史命令搜索

历史命令
history [选项] [历史命令保存文件]，选项 -c:清空历史命令，-w:把缓存的历史命令写入历史命令保存文件~/.bash_histoy
!n 重复执行历史第n条命令；!!n 重复执行上次命令；!字符串 重复执行最后一次字符串开头的命令

输出重定向
设备 设备文件名 文件描述符 类型
键盘 /dev/stdin 0      标准输入
显示器 /dev/stdout 1    标准输出
显示器 /dev/stderr 2 标准错误输出
命令 > 文件 覆盖输出；命令 >> （可以有空格）文件，追加输出
命令 2>文件 覆盖保存错误信息到文件，命令 2>> 文件，追加保存错误输出到文件，错误输出大于号两侧没有空格、
ifconfigg >> test2.log 2>&1，ifconfigg &>> test2.log 这两条命令作用相同，都是把正确命令和错误命令追加写入到test2.log中
ls &>/dev/null 相当于空， 覆盖写入到空
命令 >> 文件1 2>>文件2 ，把正确的输出追加到文件1中，错误的输出文件2中

逻辑运算符
命令1；命令2 命令1,2顺序执行
命令1&&命令2，命令1 执行正确才执行命令2
命令1 || 命令2 ，命令1正确执行，命令2不执行；命令1执行不正确，命令2才会执行
date ; tar -zcvf etc.tar.gz /etc ; date 打包压缩时间
命令 && echo yes || echo no #命令正确执行输出yes,执行错误输出no

管道符
命令1 | 命令2 ，命令1的正确输出作为命令2的操作对象
netstat -an | grep ESTABLISHED | wc -l  #查看服务器连接人数

通配符 用来匹配文件名，目录名
rm -rf test* 删除所有test开头的文件
单引号中的所有特殊字符都没有特殊意义 echo 'ls' #ls，aa=1,echo 'aa' #aa,echo '$aa' #$aa
双引号中的特殊符号没有特殊含义，但是"$","`","\"是例外，"拥有调用变量的值","引用命令"，"转义符"的特殊含义，
    aa=1;echo "$aa" #1
`命令` 反引号和$(命令)作用一样，用来引用系统命令
    aa=`ls`;echo "$aa" #输出ls命令的结果，aa=`ls`与aa=$(ls)的作用相同，都是获取ls的结果然后赋值给aa
$用来调用变量的值
\ 反斜线，跟在\之后的特殊符号将失去特殊含义，变为普通字符。


'''