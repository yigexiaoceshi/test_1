#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
一、使用yaml文件参数化：须大量练习，须大量练习，须大量练习
语法：添加装饰器
@pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./data.yaml))
def test_param(self,a,b):
    print(a+b)


二、yaml文件的编写格式：
1、字典：key: value，注意，冒号和value之间有个空格
例：
test: 127.0.0.1
dev: 127.0.0.2
相当于：{test:"127.0.0.1",dev:"127.0.0.2"}
2、列表：前面加横杠-表示
例：
-     #杠杠-表示下方是个列表
 - 10   #杠杠-表示后面是列表的第一个元素
 - 20
-
 - 30   #杠杠-表示后面是列表的第二个元素
 - 40
相当于：[[10,20],[30,40]]
3、列表嵌套字典1：
例：
-
 - key: value  #前面加-，表示这第一个元素还是个列表
 - key1: value1
-
 key2: value2   #前面不加-，表示当前元素是个字典
 key3: value3
相当于：[[{key:value,key1:value1}],[{key2:value2,key3:value3}]]
"""
import pytest
import yaml


# 使用列表、元组、集合、字典等序列化数据传参
class TestData1:
    @pytest.mark.parametrize("a,b", [(10, 20), (10, 5), (3, 9)])  # 字符串格式参数写法
    def test_data1(self, a, b):
        print(a + b)


class TestData2:  # tuple不可修改，后面可接tuple的内置函数，但不能增删改查
    @pytest.mark.parametrize(("a", "b"), [(10, 20), (10, 5), (3, 9)])  # 元组格式参数写法，后面可使用元组的方法(不可增删改查)
    def test_data2(self, a, b):
        print(a + b)


class TestData3:  # list参数可以修改，后面可以接list的内置函数进行增删改查
    @pytest.mark.parametrize(["a", "b"], [(10, 20), (10, 5), (3, 9)])  # 列表格式参数写法，后面可使用列表的方法(可增删改查)
    def test_data3(self, a, b):
        print(a + b)


class TestData4:
    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./test_006_parameterization_yaml.yaml")))
    def test_data4(self, a, b):
        print(a + b)


class TestData5:
    @pytest.mark.parametrize("a,b", yaml.safe_load(open("./test_006_parameterization_yaml.yaml")),
                             ids=["case1", "case2", "case3"])
    def test_data5(self, a, b):
        print(a + b)


# 数据驱动：
class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./test_006_env.yaml")))  # 文件为字典格式时，进入传入key赋值给参数
    def test_demo1(self, env):
        print(env)
        if "test" not in env:
            print("这是在测试环境")
            print("测试环境的IP地址是", env["test"])
        elif "dev" in env:
            print("这是在开发环境")
            print("开发环境的IP地址是", env["dev"])

    def test_yaml(self):
        print(yaml.safe_load(open("./test_006_env.yaml")))
