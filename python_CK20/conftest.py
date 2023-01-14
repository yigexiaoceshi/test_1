#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
from typing import List
import pytest
from pytest_pratice.pythoncode.Calculator import Calculator


# 使用yield模拟teardown


@pytest.fixture()  # 添加参数作用范围设置scope="class"，yield在整个类里前后只执行一次，默认function级别每个方法前后执行一次
def get_calc():
    print("开始计算")
    calc = Calculator()  # 相当于setup
    yield calc  # 相当于return
    print("计算结束")  # 相当于teardown


# 添加这个参数，就相当于是全局方法，只要用到当前方法里的变量都可以直接使用，不需要再传入方法名
# @pytest.fixture(autouse=True)  #默认是False，如果有返回值的话不能接收，每条用例都不要返回值的时候用
# def start_app():
#     print("启动APP")

@pytest.fixture()
def start_app1():
    print("启动APP1")


@pytest.fixture()
def login():
    print("登录操作")


@pytest.fixture()
def login1():
    print("登录：成功1")


"""
比如yaml文件里或者ids想进行中文命名打印出来的是乱码，可用如下改写自带的hook的某个方法来更改编码格式解决：
External Libraries/site-packages/_pytest/hookspec.py，搜索方法：pytest_collection_modifyitems
将：
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
复制到当前需要更改编码格式的py文件任意位置，添加以下内容即可
"""


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:  # 遍历所有测试用例，item就是测试用例
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 按照当前时间自动生成日志目录名和日志文件名：
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # python找根目录：优先找pytest.ini所在路径，如果找不到会找conftest.py所在路径，都找不到就会报错
    rootdir = request.config.rootdir  # 获取当前项目的根目录
    print(f"rootdir当前项目的根目录为：{rootdir}")  # 打印当前项目的根目录
    log_name = rootdir + '/Pytest/output/log/' + now + '.logs'  # 可以拼接在日志地址上

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)
    # .set_log_path(return_path(log_name))
