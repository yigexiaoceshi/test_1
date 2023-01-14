# -*- coding:utf-8 -*-
"""
文件打开：open(file,mode='r',buffering=1,encoding=None,errors=None,newline=none,closefd=True,opener=None)
file：文件的路径和名称
mode：文件权限，只读r，写入w，追加a，默认的文件访问模式为只读r的文本模式t
buffering：寄存区缓存
    0：不寄存；
    1：访问文件时会寄存行；
    >1：寄存区的缓冲大小；
    负值：寄存区的缓冲大小则为系统默认
"""
file = open('data.txt')
print(file)
print(file.read())  # 读取文件中所有内容（缺点：文件内容较多，文件较大时，大于内存时，无法使用该方法）
print(file.readable())  # 判断文件是否可读，返回True是可读
# print(file.readline())  #每次读取文件1行，返回一个字符串对象，保存当前行的内存
print(file.readline())  # 每次读取文件1行，返回一个字符串对象，保存当前行的内存
print(file.readlines())  # 读取文件所有行，返回一个列表
file.close()  # 文件打开，操作完成之后，一般都会关闭，释放被占资源

# with 语句块，可以将文件打开之后，操作完毕，自动关闭这个文件，操作语句必须在with语句块里
# 如果文件是个图片：with open("/Download/liyong/1.jpg","rb") as picture: 指定二进制模式
# 正常的文本，可以使用rt，也就是它的默认读取模式
with open('data.txt') as file1:
    while True:
        line = file1.readline()
        if line:  # 如果当前行不为空
            print(line)  # 每执行一次print就自动执行一次自动换行
        else:
            break

"""
Json格式转化
"""
