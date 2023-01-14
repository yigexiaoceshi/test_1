#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
pytest常用插件：
pip install allure-pytest：安装了才可以添加各种装饰器
pip install pytest-ordering：控制用例的执行顺序（重点），一般尽量保持测试用例的独立性，特定业务场景会要求按顺序执行
pip install pytest-xdist：分布式并发执行测试用例（重点），测试用例的量比较大时，可分配给多个CPU同时执行，更高效
pip install pytest-dependency：控制用例之间的依赖关系
pip install pytest-rerunfailures：失败重跑，可通过参数设置重跑次数
pip install pytest-assume：多重校验，assert如果失败则会跳出并停止执行，使用该插件可以实现不管断言结果都全部执行
pip install pytest-random-order：用例随机执行
pip install pytest-html：测试报告（了解即可，一般使用allure）
"""
import logging
import time

"""pytest-ordering:
场景：一般对于集成测试，经常用例间会有上下文的依赖关系，默认的用例执行顺序是自上而下按照顺序执行
解决方法1：尽量通过setup和teardown或者fixture来解决
解决方法2：使用装饰器"pytest.mark.run(order=2)"，数字越小执行优先级越高
注意：多个插件装饰器(多于2个时)，有可能会发生冲突
"""
import pytest
from time import sleep


def double(a):
    return a * 2


# 注：当pycharm默认解释器配置了pytest后，默认只收集test_开头的方法/函数，及Test开头的类，其他的语句块不会执行，如要执行得添加参数(-s)
print(double("你好"))


# @pytest.mark.int
@pytest.mark.run(order=3)  # 添加装饰器，设置执行优先级为3，先执行1，再执行2，再执行3
def test_double_int():  # 整数比较
    assert 4.0 == double(2)


# @pytest.mark.float
@pytest.mark.run(order=1)  # 添加装饰器，设置执行优先级为1，先执行1，再执行2，再执行3
def test_double_float():  # 浮点数比较
    assert 0.4 == double(0.2)


# @pytest.mark.str
@pytest.mark.run(order=2)  # 添加装饰器，设置执行优先级为2，先执行1，再执行2，再执行3
def test_double_str():  # 字符串比较
    assert "abcabc" == double("abc")


"""pytest-xdist，用例较多时，执行效果比较明显，多进程并发执行，同时支持allure"""


def test_a():
    sleep(1)
    logging.info(f"测试日志相关功能:{time.time()}")  # pytest.ini里已经配置，并在当前目录自动生成log目录和log文件


def test_b():
    sleep(2)


def test_c():
    sleep(3)


# 当前目录下执行：pytest test_015_live_plug_in.py --collect-only，收集当前一共有多少条测试用例
# 直接执行：pytest test_015_live_plug_in.py，差不多执行时间为6.04秒
# 使用分布式执行，执行：pytest test_015_live_plug_in.py -n 4，使用4个CPU核心同时执行者6条用例，时间约为3.64秒

"""
分布式执行测试用例的基本原则：
1、测试用例之间建议是可独立执行的，不要有依赖关系，容易导致批量失败，会互相牵制
2、用例执行没有顺序，随机顺序都保证能正常执行最好，容易导致批量失败
3、每个用例都能重复执行，运行结果不会影响其他用例，容易导致批量失败
"""
