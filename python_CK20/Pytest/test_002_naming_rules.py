#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
Python推荐规范：
1、目录名(包名)：lower_with_under
2、模块名(.py文件)：lower_with_under
3、类(class)：CapWords（驼峰命名法，仅首字母大写）
4、方法(类里面定义的def)/函数(类外面定义的def)：lower_with_under
5、全局常量(Global/Class Constants)：CAPS_WITH_UNDER  #常量意思是不能改变的量，事实上Python中的常量仍然是个变量，习惯上的写法一般不去改变它的值
6、全局变量(Global/Class Variables)：lower_with_under

Python里Pytest测试用例编写规则：
1、目录名(包名)：暂时不做要求
2、模块名(.py文件)：test_ 开头，或者 _test 结尾
3、类(class)：Test 开头         #注意：测试类中不可添加构造函数"__init__"，添加之后就不是一个测试类，里头所有的"test_"方法都无法识别
4、方法/函数(def)：test_ 开头
"""

"""
1、使用pytest框架执行测试用例，解释器可以使用"python test.py"(需在test.py里添加执行入口)，也可以使用pytest解释器
2、设置默认解释器为pytest:Tools/Python Integrated Tools:Testing的Default test runner设置为pytest，apply应用OK确定即可
3、配置好了默认解释器为pytest后，会自动识别当前文件所有符合pytest框架命名的类、方法/函数等，绿色箭头标记
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
