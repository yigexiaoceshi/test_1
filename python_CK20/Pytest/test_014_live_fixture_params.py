#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List

import pytest
import yaml
from pytest_pratice.pythoncode.Calculator import *
from pytest_pratice.testing.test_calc import *

"""第一步
打开测试数据文件，通过yaml.safe_load("打开的文件")并提取测试数据，初步确定格式，返回一个列表或元组格式
注意：编写yaml文件格式的时候，ids的元素个数必须是要和测试用例的个数(或者叫多少组)保持一致的
******
******核心重点：学会怎么根据测试用例需要的数据去写yaml文件，并且如何去组装成我们所需要的数据格式应用到测试用例中
******
"""


def get_datas():
    with open("./datas/calc.yml") as f:  # 使用with_as打开文件读取完数据之后会自动关闭文件，所以一般不用open
        file = yaml.safe_load(f)
        # datas.get("key")和datas("key")区别，如果key不存在，则第一种不会报错，第二种会报错
        datas_int = file.get("add").get("int").get("datas")
        print(datas_int)  # 返回一个列表嵌套列表
        datas_int_ids = file.get("add").get("int").get("ids")
        print(datas_int_ids)  # 返回一个列表
        datas_float_ids = file.get("add").get("float").get("ids")
        print(datas_float_ids)  # 返回一个列表
        datas_float = file.get("add").get("float").get("datas")
        print(datas_float)  # 返回一个列表嵌套列表
        """不可按照下面这种方式来写，因为一个文件被load一次之后，相当于是open状态没有关闭，第二次再去load就是空的，返回None,
        #指针已经指到了文件末尾，相当于从最后一行开始读取，也可以通过修改指针位置的方式来多次load，在load一次之后，
        执行f.seek(0)将指针移到文件首行，可以再次load，但是写法较复杂不推荐，多次load也会浪费资源"""
        # datas_int = yaml.safe_load(f).get("add").get("int").get("datas")
        # datas_int_ids = yaml.safe_load(f).get("add").get("int").get("ids")
        # datas_float = yaml.safe_load(f).get("add").get("float").get("datas")
        # datas_float_ids = yaml.safe_load(f).get("add").get("float").get("ids")

        return (datas_int, datas_int_ids, datas_float, datas_float_ids)


"""第二步
按照方法中需要传入的数据格式，从第一步返回的列表或元组中使用request.param方法return想要的格式"""


@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])  # 一次性全部加载进来，一组一组的使用
def get_datas_byfixture(request):
    print(f"request.param = {request.param}")
    # 按照用例的条数接收并返回测试数据，是固定的写法
    return request.param


# 验证提取到的return数据格式，进一步确认是否想要的数据
# 此时确定调用方法需要用到的2个传参，以及返回结果分别在每个return到的数组里，索引依次为[0],[1],[2]
# 所以调用方法时，参数不再需要传递，而是直接从第二部return到的数组里直接以索引的方式读取并使用
def test_get_datas_byfixture(get_datas_byfixture):
    print(get_datas_byfixture)


class TestCalc:
    #
    def test_add(self, get_calc, get_datas_byfixture):  # 括号里的2个fixture顺序随意`
        result = get_calc.add(get_datas_byfixture[0], get_datas_byfixture[1])
        assert result == get_datas_byfixture[2]


"""
小结：
录播里使用@pytest.mark.parametrize("a,b,expect",[[1,2,3],[4,5,6],ids=["A","B","C"])的方式，
还是读取数据，并赋值给传参进行使用
使用fixture则不需要传参，而是把每一组传参以列表的形式返回，直接使用索引的方式读取使用
"""


# 加深理解，例子1：
@pytest.fixture(params=[1, 2, 3])
def get_parame():
    print("fixture parame")


def test_fixture_parame(get_parame):  # 依次传入三组用例，一组一个数字
    print("aaa")


@pytest.fixture(params=[[1, 2, 3], [4, 5, 9], [11, 22, 33]], ids=["用例1", "用例2", "用例3"])  # 提供三组测试用例，每个元素都是一组
def get_param(request):
    return request.param  # 可理解为将目标数据按照每个元素一组用例的方式依次给到调用函数使用，使用索引
    # print(f"request.param的值是 = {request.param}")


def test_fixture_param(get_param):
    print(f"get_param的值是：{get_param}")
    x = get_param[0]
    y = get_param[1]
    z = get_param[2]
    print(f"a = {x},b = {y},c = {z}")  # 一共三组测试用例，全部加载进来，一组一组依次使用
    if get_param[0] + get_param[1] == get_param[2]:
        print("测试通过")
    else:
        print("测试不通过")
