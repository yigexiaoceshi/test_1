# -*- coding:utf-8 -*-
"""
一、项目的目录结构
    1、package 包
    2、module 模块
    3、function 方法
二、模块定义：包含Python定义和语句的文件，以（.py）结尾，可作为脚本运行
三、文件引用
"""

"""
模块导入：
1、import 模块名
2、from 模块名 import 方法/变量/类
3、from 模块名 import *
4、from 目录名.模块名 import 方法/变量/类
注：
1、同一个模块写多次，只被导入一次；import写在代码的顶端
2、Python解释器对于模块位置的搜索顺序（不是绝对的按这个顺序找，而是按照sys.path打印出来的路径列表去找）
    包含输入脚本的目录（如果未指定文件，则为当前目录）
    PythonPATH（目录名称列表，语法与shell变量相同PATH）
    安装的默认路径
"""

"""模块分类：1、系统内置模块：Python安装自带的，比如：sys，os，time，json等"""
import sys

print(sys.path)  # 输出一个列表，列表里是当前导入的所有模块所在的路径，当前模块使用import导入的所有模块，都是在这个路径列表里找到的（路径精确到文件夹）
import json
import os  # 在后面的代码没有引用，是置灰状态，建议分开导入（可以以逗号隔开一次性导入）
import time
import re

time.sleep(1)  # 方法sleep() 必须且只能接收一个参数

"""2、第三方开源模块：使用pip install安装的，第三方开源的模块"""
import yaml
import requests

"""3、自定义模块：自己写的模块，对某段逻辑或者某些函数进行封装后供其他函数调用"""
"""同一个模块下多个类/方法/函数/变量"""
# from search001 import search    #导入这个方法
# from search001 import search1   #导入这个方法
# from search001 import Search2   #导入这个类
# from search001 import search,search1,Search2    #同一个模块的多个方法/类/变量可以用逗号隔开，写在一起
from search001 import *  # 如果一个模块里有多个方法/类/变量/函数需要导入，可以用*代替，导入所有的类/方法/函数/变量

search()
"""不同目录下模块的导入"""
from Python_test.test001 import test001
from Python_test.test001 import hello

print(hello)  # 此处的hello是导入的模块中的一个变量，如果加上双引号或者单引号就成了字符串
test001()
# import Python_test.test001    #可以仅导入模块名，但是调用方法的时候要指明（目录.模块.方法/类/函数)
# Python_test.test001.test001() #因为2个py文件里可能有相同的类名和方法名
# 问：如果同时导入2个文件里的所有方法，2个文件里有相同的类名或方法名时会怎样？

"""
常用方法：
1、dir() ： 找出当前模块定义的对象
2、dir(sys) ： 找出参数模块定义的对象
"""
AAA = "我是当前模块定义的变量"


def BBB():
    pass


print(dir())  # 当前模块定义了的对象，以列表方式输出一个当前模块已经定义或者引用的类，方法，函数，变量的集合
print(dir(sys))

"""注：如果自定义的模块和系统自带模块同名，优先导入的是自定义模块，所以命名的时候一定要避免和系统自带的模块同名"""

"""
模块化的总结：
1、提高代码的可维护性
2、提升编码效率
3、函数名可重复（起名避免与系统模块名重复）
"""
