#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
"class a:"、"class a():"和"class a(object):"三种写法是等价的：
object是Python的默认类，本身包含很多方法，比如list，str，dict等都是继承了object的方法；
继承了object的类属于新式类，没有继承的属于经典类，在Python2中有新式类和经典类的说法
Python3中只有新式类的说法，即所有的自定义类、基类都会继承object类：Python3中的所有类都是object的子类。
所以一些内置的方法会写在object中，调用的时候子类是否需要定义，比如常见的构造方法(__init__:)就属于内置方法
"""
# 定义类的时候可加括号，不加括号，括号里可写可不写object
class a(object):
    def __init__(self):
        print("不带括号的类a")

# 此时的a为字母a，赋值给b，指向同一个内存地址
b = a
print("b的内存地址", id(b))
print("a的内存地址", id(a))
"""
工厂可以用一个具有特定行为和功能的模子，生产出很多相似的具体的产品。
类可以理解为这个模子，而具体的产品则是类每次被调用时生成的实例化对象，程序处理的实际对象也就是这个实例化对象
"""
# a加括号，a()为类的调用，类每次被调用就会生成一个新的实例，下面的bb就是类a的一个实例化对象
bb = a()
print("bb的内存地址", id(bb))
print("a()的内存地址", id(a()))


# class aa():
#     def __init__(self):
#         print("带括号的类：aa()")
#
#
# bbb = aa
# print("bbb的内存地址", id(bbb))
# print("aa的内存地址", id(aa))
# bbbb = aa()
# print("bbbb的内存地址", id(bbbb))
# print("aa()的内存地址", id(aa()))
