#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
fixture的特点及优势：
1、命令灵活，对于setup和teardown，可以不起这两个名字，fixture结合yield使用
2、数据共享，在conftest.py配置里写方法可以实现数据共享，不需要import导入，可以自动导入（自动发现机制，公共的类、方法、变量等）
3、scope的层次及神奇的yield组合相当于各种setup和teardown
"""
import pytest

"""fixture使用场景1：
每条测试用例的前置条件不一致，使用fixture，默认的scope(范围)是方法级别(function)
function：函数方法级别，每个函数或方法前后都会执行一次yield，相当于setup_function和teardown_function
class：类级别，每个类执行前后都会调用一次yield，相当于setup_class和teardown_class
module：模块级别，每个模块执行前后都会调用一次yield，相当于setup_module和teardown_module
package：package包级别，每个包执行前后调用一次yield
session：每个项目执行前后各调用一次yield，项目内所有的test_*.py，所有的Test类，所有的test_*或*_test模块都共享这个方法
步骤：
1、导入pytest
2、在登录的函数上方添加装饰器：@pytest.fixture()
3、在需要使用测试方法的的用例前传入该方法名称，在执行该用例的时候就会先执行传入的方法，不传入就不会执行
注意：即使公共方法写在公共模块conftest.py，如果要实现方法名作为参数传递给其他方法，还是要加装饰器的，如果公共方法有返回值而调用方需要用到的话，还是需要传入，不然会被忽略
注意：在方法里调用fixture函数，可理解为只是为了拿到fixture函数的返回结果，比如传入方法，返回的方法也可以理解为一个变量，返回值作为一个常量
"""


def start_app():
    print("启动APP操作")


@pytest.fixture()  # 添加该装饰器，该方法就可以作为参数传入到其他方法
def login():
    print("登录操作")


def test_search():  # 需求：无须登录
    print("搜索功能")


# 下面的注释掉，因为conftest.py里注释掉了start_app()方法，因为fixture添加了autouse=True影响了其他用例
# def test_cart(login,start_app):   #需求，须登录
#     print("添加购物车功能")
def test_order(login):  # 需求，须登录
    # 提前调用登录方法
    # login()  #也可以放入setup，但是有些用例不需要login()，此时用到fixture
    print("下单功能")


"""fixture的使用场景2
1、使用conftest.py进行数据共享，包括公共类，公共方法和函数，公共变量，公共数据等都可以写入conftest.py
2、conftest.py放在不同的位置，共享的作用范围不同
3、系统执行到某个函数时，先到当前模块中查找，找不到时，就会到conftest.py模块里查找
注意：
1、conftest.py文件名字不能更换，基于Python的自动发现机制
2、一般放在项目下，可以实现更大范围(全局)的数据共享
"""


def test_cart1(start_app1, login1):  # 注意：调动多个方法时，注意顺序，程序按照顺序执行的
    print("添加购物车1")


def test_order1(login1):  # login1()写在公共模块，并添加了装饰器：@pytest.fixture()
    print("下单功能1")


@pytest.mark.parametrize("a,b", [[1, 2], [3, 4], [5, 6]])
def test_params(a, b, login, start_app):  # 方法参数按照顺序，传入的方法和当前参数顺序任意，传入的方法之间按照顺序
    print("当前方法需要传参数的用例")
