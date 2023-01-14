#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、pycharm或者使用命令"pip install pytest"安装好pytest，不需要导入pytest
2、命令行：使用pytest直接执行，不需要带文件名，会自动识别当前目录及其子目录下所有test_开头的方法并执行，如果使用"python 文件名"则需在程序内添加执行入口
注：使用pip和pip3安装的包，路径不一样，先确定pip的指向（待研究）
"""


# 定义一个函数
def inc(x):
    return x + 1


# 定义一个函数，一条通过测试用例1：
def test_answer1():
    assert inc(3) == 4


# 定义一个函数，一条不通过测试用例2：
def test_answer2():
    assert inc(3) == 5


# 定义一个类
class TestDemo:
    # 类内定义一个方法：
    def test_demo1(self):
        pass

    # 类内定义一个方法：
    def test_demo2(self):
        pass
