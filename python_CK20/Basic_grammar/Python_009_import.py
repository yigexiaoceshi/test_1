#!/usr/bin/python3
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
2、Python解释器对于模块位置的搜索顺序（不是绝对的按这个顺序找，而是按照sys.path打印出来的路径列表去找）：
    包含输入脚本的目录（如果未指定文件，则为当前目录）
    PythonPATH（目录名称列表，语法与shell变量相同PATH）
    安装的默认路径
3、如果自定义模块名和系统模块重名，则优先会调用自定义模块
"""
# 系统内置模块，无需另行安装
import os  # 导入的模块里的方法，类，函数，变量等未被使用则是置灰状态
import time

time.sleep(2)  # 强制等待2秒，该函数仅接收且必须接收一个参数
import sys

# 输出一个列表，列表里是当前导入的所有模块所在的路径，当前模块使用import导入的所有模块，都是在这个路径列表里找到的（路径精确到文件夹）
print(sys.path)  # 查找模块的路径，按照列表提供的路径依次找寻当前模块sys的路径
import json
import re
# import re,time,sys  #可这么导入，不建议

# 第三方开源模块：使用"pip install 模块名"进行安装
import yaml
import requests

# 自定义模块
import Python_009_import_test01
from Python_009_import_test01 import *

# from Python_009_import_test01 import search1,search2,search3,search4 #也可以这么写，不建议，太复杂
# 直接调用函数
print(search1())  # 无入参，无返回值，返回None
print(search2(2))  # 有入参，无返回值，返回None
print(search3())  # 无入参，有返回值
print(search4(4))  # 有入参，有返回值

# 直接调用类里的方法，写法"类名().方法名(参数1,参数2)"，类必须实例化
print(Number().add(1, 2))
print(Number().subtraction(3, 4))

# from pakeage.文件名 import 方法名
from Python_test.test001 import test001

print(test001())

# 直接调用模块里的变量
print(e)
print(f)

# 调用一个和系统重名的random，默认找到的是自定义的random，从random.path里可以看到，找目录的优先级
print(random())

"""
常用方法
"""
print(dir())  # 当前模块可调用的所有模块，方法，类，函数，变量等
print(dir(sys))  # sys模块可调用的所有模块，方法，类，函数，变量等

"""
小结：
1、提高代码的可维护性
2、提升了编码效率，使代码可读性更强
3、类名，方法名尽量避免与系统重复
"""
