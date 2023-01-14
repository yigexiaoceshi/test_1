#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
导入包出问题时，可先通过打印sys.path查看当前py文件所有的方法、类所在的路径，如果需要导入的包的路径不存在
则需要添加进path，就不需要再导入，否则需要从sys.path的已有的项目路径下开始导入
"""


# 定义一个无入参，无返回值函数
def search1():
    print("这是一个搜索函数，无入参，无返回值")


# 定义一个有入参，入返回值函数
def search2(a):
    print("这是一个搜索函数，有入参，无返回值")


# 定义一个无入参，有返回值函数
def search3():
    print("这是一个搜索函数，无入参，有返回值")
    return "这是函数3的返回值"


# 定义一个有入参，有返回值函数
def search4(b):
    print("这是一个搜索函数，有入参，有返回值")
    return "这是函数4的返回值"


# 定义一个类，类里面定义2个方法
class Number():
    def add(self, a, b):
        print("这是一个相加的方法，返回2个参数之和")
        return a + b

    def subtraction(self, c, d):
        print("这是一个相减的方法，返回2个参数之差")
        return c - d


# 定义一个变量
e = "eee"
f = {f: f * f for f in range(6)}


# 定义一个和系统模块重名的方法
def random():
    print("这是一个自定义的random")
