#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
try except语句的执行流程如下：
1、首先执行try中的代码块，如果执行过程中出现异常，系统会自动生成一个异常类型，并将该异常提交给Python解释器，这个过程叫捕获异常
2、当Python解释器收到异常时，会寻找能处理该异常对象的except块，找到合适的except块则把异常丢给它处理，这个过程叫处理异常，如果Python解释器找不到，则程序终止运行，Python解释器会退出
3、不管代码是否在try块中，只要出现异常系统都会捕获，如果出现异常的代码块没有在try中，则Python解释器不会去寻找能处理该异常的except块，或者说没有处理该异常的except块时，Python解释器无法处理程序将停止运行，反之，如果发生异常的代码块由try捕获并由except处理，则程序可以继续执行
4、异常常见的相关信息：
yichang.orgs：返回异常的错误编码和描述字符串，如果是列表、元组等，则可以使用索引
yichang.type：返回异常信息的类型
yichang.str(e)：返回异常信息，但不包括异常信息的类型
yichang.repr(e)：返回较全面的异常信息，包括异常信息的类型
5、常见异常：
    除0异常：1/0
    名称异常
    索引异常：索引不存在
    键异常：比如字典取value时，传入了一个不存在的key
    值异常：比如数据类型异常
    属性异常：
    等等
"""
# 示例1：
try:
    a = int(input("请输入除数："))
    b = int(input("请输入被除数："))
    c = a / b  # 此处如果发生异常，会执行处理该异常的一个except，不会再返回try模块，所以之后即使还有异常也不会被捕获到
    print("您输入的两个数相除的结果是：", c)
    d = 1 / 0
except(ValueError, ArithmeticError):  # 指定异常的类型，及处理方法
    print("程序发生了数字格式异常，算术异常之一")
except:  # 不知道异常的具体类型，但做出处理
    print("未知异常")
else:  # 执行完try模块，没有发现任何异常，也就是说没有执行任何一个except，就会执行else代码块
    print("没有异常")
finally:  # 不管是否发生异常，不管是否走进except，都会执行finally
    print("程序继续运行")
