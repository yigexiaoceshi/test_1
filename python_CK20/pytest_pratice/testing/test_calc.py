#!/usr/bin/python3
# -*- coding:utf-8 -*-

class TestCalc:
    def test_add(self, get_calc):
        # calc = Calculator()
        result = get_calc.add(1, 2)
        assert result == 3

    def test_div(self, get_calc):
        # calc = Calculator()
        result = get_calc.div(6, 3)
        assert result == 2


"""
命令行可以添加"--setup-show"来查看具体的调用执行过程，如想看到为什么yield会被调用两次，执行以下命令：
pytest test_calc.py::TestCalc::test_add --setup-show
"""
