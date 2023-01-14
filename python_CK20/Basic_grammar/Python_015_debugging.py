#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
调试（debug）：将编制的程序投入实际运行前，运用手工或者编译程序等方法进行测试，修正"语法错误和逻辑错误"的过程
1、语法错误：编写的Python语法不正确，程序编译失败
2、逻辑错误：代码本身能正常执行，但是执行完成的结果不符合预期结果
调试（debug）分类：
1、语法错误：类型错误，语法错误，缩进错误，索引错误，键错误
2、逻辑错误：业务逻辑错误，并不会报错
调试（debug）方法：
1、对应位置使用print或者logging打印日志信息
2、启动断点模式debug调试
"""
import logging

# 语法错误示例
# name = 'wang'
# age = 20
# print('name is ' + name + ",age is " + str(age)) #如果直接拼接会报错，整数不能和字符串拼接，所以必须转为字符串

# 逻辑错误示例
# 需求：a == 1时，flag = True
a = 1
b = 2
logging.basicConfig(level=logging.INFO)  # 调用方法设置日志级别
if a == 1:
    flag = False  # 和需求不符，因为逻辑错误就产生了bug，但是程序能正常运行
    # print(f"a == 1时，flag为{flag}")
    logging.info(f"a == 1:flag = {flag}")
else:
    flag = True
    # print(f"else,flag为：{flag}")
    logging.info(f"a == 1:flag = {flag}")
print(flag)

# c = 1
# d = 2
# if c = 1:   #语法错误
#     cd = False
# else:
#     cd = True

# e = [1,2,3]
# print(e[4])  #语法错误，下标越界，超出列表长度

"""
栈的概念：先入先出，后入后出
"""
