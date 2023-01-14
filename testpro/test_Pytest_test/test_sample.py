# -*- coding:utf-8 -*-
"""
pytest命名规则
1、py文件：test_ 开头，或者 _test 结尾
2、类：Test 开头
3、方法/函数：test_ 开头
4、Python包没有命名要求
5、测试类中不可添加构造函数：__init__，否则pytestcd 无法识别
"""


# content of sample_test.py

def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5
