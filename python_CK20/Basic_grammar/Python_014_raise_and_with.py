#!/usr/bin/python3
# -*- coding:utf -*-
"""
pytest.raise()
1、可以捕获特定的异常
2、获取捕获的异常细节(包括异常类型，异常信息)，可以考虑加入打印日志
3、发生异常，后面的代码将不会运行
"""
import pytest

# 示例1：
# def main():
#     try:
#         # 使用try...except来捕捉异常
#         # 此时即使程序出现异常，也不会先传递给main函数，而是先寻找能够处理该异常的except
#         mtd(3)
#     except Exception as e:  #exception为常见异常的父类
#         print("程序出现异常：",e)
#     # 不使用try...except捕捉异常，下面这次调用就会传播出来导致程序终止
#     mtd(3)
#
# def mtd(a):
#     if a > 0:
#         raise ValueError("a的值大于0，不符合要求")
#
# main()
"""
程序运行详解：
1、运行方法main，进入try模块，try模块里第一次调用mtd()函数，传入参数a=3
2、此时，3>0，引发程序自发抛出的异常ValueError，因为在try里抛出，所以程序找到except进行处理
3、执行print，输出"程序出现异常：a的值大于0，不符合要求"，程序继续执行
4、main方法继续往下走，第二次调用mtd()函数，传入参数a=3
5、此时，3>0，再次引发程序自发抛出的异常ValurError，此时并不在try里抛出，Python解释器无法处理该异常，程序终止
6、main()方法始终未被调用
7、注：即使try里有多个异常，只要其中一个异常被捕获进入except，执行了except之后不会再返回try里继续执行，程序终止
"""
# 示例2：
# def test_raise():
#     with pytest.raises(ValueError,match="must be 0 or None"):
#         raise ValueError("value must be 0 or None")
#
# def test_raise1():
#     with pytest.raises((ZeroDivisionError,ValueError),match="除数为0"):  #预期匹配到的一个或多个异常以及文字，文字一般可以去掉，用的不多
#         raise ZeroDivisionError("除数为0")  #文字不匹配时，添加多个异常预期会报错（正则匹配match报错）
#
# def test_raise2():
#     #pytest.raises()：捕获异常
#     with pytest.raises(ValueError) as exc_info: #用as给捕获到的异常起个别名，方便在except块中调用异常类型
#         raise ValueError("value must be 42")
#     assert exc_info.type is ValueError
#     assert exc_info.value.args[0] == "value must be 42"

# with-as用法：
"""示例1：程序无错误"""
# class Sample(object):
#     def __enter__(self):
#         print("In __enter__()")
#         return "Foo"
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("In __exit__()")
#
# def get_sample():
#     return Sample()
#
# with get_sample() as sample:
#     print("sample",sample)
#
# print(Sample) #这个表示类本身：<class '__main__.Sample'>
# print(Sample()) #这个表示类的一个实例对象：<__main__.Sample object at 0x7fee40302fd0>
"""
程序运行详解：
1、定义了一个类Sample，类里面2个方法，定义了一个函数get_sample
2、执行with语句，调用函数get_sample()，返回Sample()，即Sample类的一个匿名实例化对象，该对象赋值给别名的sample
3、注意：2中如果没有as别名，则函数get_sample返回的实例化对象Sample()会被忽略
4、执行Sample类里的第一个方法，打印"In __enter__()"，以及返回值Foo赋值给别名sample
5、因为执行__enter__()方法没有报错，所以继续执行__exit__()方法，打印"In __exit__()"赋值给sample
6、所以最终代码执行结果为：
In __enter__()
sample Foo
In __exit__()
<class '__main__.Sample'>
<__main__.Sample object at 0x7fee40302fd0>
"""

"""示例2：程序有错"""
# class Demo:
#     def __enter__(self):
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exc_type",exc_type)
#         print("exc_val",exc_val)
#         print("exc_tb",exc_tb)
#     def do_somethiing(self):
#         bar = 1/0
#         return bar + 10
# with Demo() as demo:
#     demo.do_somethiing()
"""
程序运行详解：
1、执行with语句，执行Demo()类，并将返回值赋值给demo
2、首先执行__enter__()，方法将Demo类自身实例化并返回给demo
3、执行demo.do_something()，bar = 1/0抛出异常，return bar + 10语句不再执行，程序无法处理该异常，报错
4、即使报错，仍然会执行方法__exit__()，执行三个print
"""

"""
自定义异常:
class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
"""


class MyException(Exception):  # 继承
    def __init__(self, msg):  # 后续深究，先了解用法
        print(f"这是自定义一个异常:{msg}")


def test_1(a):
    if a > 0:
        raise MyException
    else:
        pass


test_1(1)
