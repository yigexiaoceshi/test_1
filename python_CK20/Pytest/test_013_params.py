#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List

import pytest
import yaml


# 定义一个方法读取yaml文件里的数据：
def get_datas():
    with open("./datas/calc.yml") as f:
        file = yaml.safe_load(f)
        datas_int = file.get("add").get("int").get("datas")
        print(datas_int)  # 返回一个列表嵌套列表
        datas_int_ids = file.get("add").get("int").get("ids")
        print(datas_int_ids)  # 返回一个列表
        datas_float_ids = file.get("add").get("float").get("ids")
        print(datas_float_ids)  # 返回一个列表
        datas_float = file.get("add").get("float").get("datas")
        print(datas_float)  # 返回一个列表嵌套列表

        return (datas_int, datas_int_ids, datas_float, datas_float_ids)


def test_datas():
    print(get_datas())


class TestCalc:
    # 参数化方式1，录播有
    @pytest.mark.parametrize("a,b,expect", get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect, get_calc):
        # calc = Calculator()
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[0], ids=get_datas()[1])
    def test_div(self, get_calc, a, b, expect):
        # calc = Calculator()
        result = get_calc.div(a, b)
        assert result == expect
