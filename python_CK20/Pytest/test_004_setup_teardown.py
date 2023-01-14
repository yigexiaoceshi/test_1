#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
测试装置介绍：
1、setup_module/teardown_module：模块(.py文件)前后各执行一次 - (定义在类外面)
2、setup_class/teardown_class：类前后执行一次 - (定义在类里面)
3、setup_method/teardown_method：每个方法(类内定义)调用前后各执行一次 - (定义在类里面)
4、setup/teardown：和setup_method/teardown_method一样
5、setup_function/teardown_function：每个函数(类外定义)调用前后各执行一次 - (定义在类外面)
6、每种类型不是一定成对出现，根据项目需求选择使用
"""


def setup_module():
    print("模块级别：setup_module")


def teardown_module():
    print("模块级别：teardown_module")


def setup_function():
    print("函数级别：setup_function")


def teardown_function():
    print("函数级别：teardown_function")


# 定义一个类
class TestDemo:
    def setup_class(self):
        print("类级别：setup_class")

    def teardown_class(self):
        print("类级别：teardown_class")

    # def setup_method(self):   #和 def setup(self): 效果相同
    def setup(self):
        print("方法级别：setup_method")

    # def teardown_method(self):   #和 def teardown(self): 效果相同
    def teardown(self):
        print("方法级别：teardown_method")

    # 定义一个方法：
    def test_demo1(self):
        print("我是TestDemo类的test_demo1方法")

    # 定义一个方法：
    def test_demo2(self):
        print("我是TestDemo类的test_demo2方法")


# 定义两个函数：
def test_func1():
    print("这是一个函数test_func1")


def test_func2():
    print("这是一个函数test_func2")
