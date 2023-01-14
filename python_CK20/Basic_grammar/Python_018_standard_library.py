#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
常见标准库
操作系统相关：os
时间日期相关：time，datatime
科学计算相关：math
网络请求相关：urllib
sys，JSON等等
"""
# OS模块：主要对文件和目录进行操作
# 常用方法：
# os.mdkir()：创建目录
# os.removedirs()：删除目录或文件
# os.getcwd()：获取当前目录
# os.path.exists(dir or file)：判断文件或目录是否存在
import os

# print(os.getcwd())   #获取当前目录
# os.mkdir("testdir")  #在当前目录创建文件夹"testdir"，再次执行会报错，提示文件已存在
# print(os.listdir("./"))  #列出当前目录或指定目录所有的文件和文件夹，返回一个列表
# os.removedirs("testdir")  #删除目录或文件，同理再次执行会报错，提示文件不存在
# if not os.path.exists("b"): #判断当前目录是否存在目录b
#     os.mkdir("b")  #不存在则创建
# if not os.path.exists("b/test.txt"): #如果目录b下没有test.txt
#     file = open("b/test.txt","w")  #则创建并打开test.txt，文件权限为w
#     file.write("你好，我是test.txt文件")  #往文件test.txt里写入字符串

import time

print(time.asctime())  # 国外时间格式
print(time.time())  # 时间戳，以纪元(1970年1月1日0时0分0秒)为单位以来的时间(以秒为单位)，称为Unix时间,float格式
time.sleep(2)  # 强制等待2秒
print(time.localtime())  # 时间戳转换成时间元组
# time.strftime("需转换的格式",元组对象) #将当前时间戳转换成带格式的时间
print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime()))
# 获取两天前的时间
now_timesmap = time.time()
two_day_before = now_timesmap - 60 * 60 * 24 * 2
print(two_day_before)
two_day_beford_tuple = time.localtime(two_day_before)
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", two_day_beford_tuple))

# import urllib2  #Python2导入
import urllib.request  # python3导入

# response = urllib.urlopen("http://www.baidu.com")
response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)
print(response.read())
print(response.headers)
# urllib更多方法参考官网

import math

"""
math.ceil(x)：返回大于或等于参数x的最小整数，int型
math.floor(x)：返回小于或等于参数x的最大整数，int型
math.sqrt(x)：返回x的平方根，返回浮点型float
等等
"""
print(math.ceil(6.6))
print(math.floor(4.9))
print(math.sqrt(16))
print(math.sqrt(4 * 4))
print(math.sqrt(7 + 3 * (2 + 1)))
