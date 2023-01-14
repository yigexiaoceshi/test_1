#!/usr/bin/python3
# -*- """"""coding:utf-8 -*-
"""
文件打开：open(file,mode='r',buffering=1,encoding=None,errors=None,newline=none,closefd=True,opener=None)
file：文件的路径和名称
mode：文件权限，只读r，写入w，追加a，默认的文件访问模式为只读(r)的文本模式(t)
buffering：寄存区缓存
    0：不寄存；
    1：访问文件时会寄存行；
    >1：寄存区的缓冲大小；
    负值：寄存区的缓冲大小则为系统默认
"""
# txt文件操作：图片格式文件需要使用rb权限，读取二进制；正常的文本可使用rt（默认只读的文本格式）
file = open("Python_011_file_f_w_x.txt")  # open("Python_011_file_f_w_x.txt","rt")不写文件权限时，默认为只读的文本模式
print(file.readable())  # 返回True，表明读取成功，文件是可读的
# print(file.readlines()) #一次性读取所有行
print(file.readline())  # 依次读取一行
print(file.readline())  # 依次读取一行
print(file.readline())  # 依次读取一行
# 注意：上面这种写法，文件打开一次，赋值给file，执行三次readline()相当于是依次取同一个文件里的第一、二、三行；
# 而下面这种写法意思是每次都单独打开一个新文件，分别从三个文件里取第一行
print(open("Python_011_file_f_w_x.txt").readline())
print(open("Python_011_file_f_w_x.txt").readline())
print(open("Python_011_file_f_w_x.txt").readline())
# 文件打开后要执行关闭操作，关闭而且要及时，及时释放空间
file.close()

# with语句介绍：打开文件，执行完with语句块里的语句后（读写操作），自动关闭文件
with open("Python_011_file_f_w_x.txt") as file1:
    # print(file1.readline())
    # print(file1.readline())
    # print(file1.readline())
    while True:
        line = file1.readline()
        if line:  # 如果该行有数据
            print(line)  # 每次print会带一个回车，每行的末尾也有个\n，相当于两次回车
        else:  # 如果没有值，可根据业务场景选择break或者continue
            break
