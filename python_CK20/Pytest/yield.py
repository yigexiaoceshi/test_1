#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""带
yield的函数被定义为一个生成器(generator)
"""


def yieldtest():
    for i in range(1, 11):  # 带yield的函数，在for循环体中，每次循环都会自动调用一个next()函数
        print(f"第{i}次循环开始，值为：{i}")
        yield i  # 相当于return，并记住上次循环的位置，下次循环从yield后面的语句开始执行
        print(f"第{i}次循环结束")


"""
第一次循环走到yield就跳出当前循环，进入第二个循环
第二个循环从yield后面的语句开始执行，再次走到yield跳出
所以，例子中的for循环从1到10一共循环10次，但是yield执行了11次，返回第十次循环的值跳出循环后，最后还调用了一次循环结束的print
"""

a = yieldtest()
for x in a:
    print(f"x的值为：{x}")
# 也可以使用next()函数打印出生成器每个迭代生成并返回的值
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
"""
命令行可以添加"--setup-show"来查看具体的调用执行过程，如想看到为什么yield会被调用两次，执行以下命令：
当前目录下可以执行：pytest yield.py::TestCalc::test_add --setup-show -vs
"""
