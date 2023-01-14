#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
参数化：将模型中的定量信息变量化，使之成为任意调整的参数，对于变量化参数赋予不同数值，就可得到不同大小和形状的零件模型
"""
import pytest

# 单个参数的参数化
# list_a = ["appium","selenium","pytest"]  #列表有序，按照索引顺序取值
# # list_a = ("appium","selenium","pytest")  #元组有序，按照索引顺序取值
# # list_a = {"appium","selenium","pytest"}  #集合是无序的，参数化的时候取值随机
# # list_a = {"key1:appium","key2:selenium","key3:pytest"}  #字典无序，随机取键值对作为参数
# @pytest.mark.parametrize("name",list_a,)
# def test_aaa(name):
#     print(name)
#     print("测试单个参数的参数化")
#     assert name in list_a

# 多个参数的参数化，示例1
"""注意：参数在参数化的时候必须要和方法传入的参数名称和顺序一致"""
# list_b = [["appium","selenium","pytest"],]  #列表嵌套列表有序，按照索引顺序取值，单个元素加逗号,消除歧义
# list_b = [("appium","selenium","pytest"),]  #列表嵌套元组有序，按照索引顺序取值，单个元素加逗号,消除歧义
# list_b = [{"appium","selenium","pytest"},]  #列表嵌套集合是无序的，参数化的时候取值随机，单个元素加逗号,消除歧义
# list_b = [{"key1:appium","key2:selenium","key3:pytest"},]  #列表嵌套字典无序，随机取键值对作为参数，单个元素加逗号,消除歧义
# list_b = ((1,2,33),)  #元组里仅嵌套一个元组时，需要加个","来消除歧义
# list_b = ([1,2,3],[4,5,6],[7,8,9])  #元组里仅嵌套一个列表时，需要加个","来消除歧义
# list_b = ({1,2,3},{4,5,6},{7,8,9})  #元组里仅嵌套一个集合时，需要加个","来消除歧义
# list_b = ({"a1:b1","a2:b2","a3:b3"},{"c1:d1","c2:d2","c3:d3"},{"e1:f1","e2:f2","e3:f3"}) #元组里仅嵌套一个字典时，需要加个","来消除歧义
# list_b = {(1,2,3),(4,5,6),(7,8,9)}   #集合仅能嵌套元组，因为集合的每个值是不可变的，所以列表、集合、字典均不能作为集合的元素
# list_b = {(1,2,3):[1,2,3],(4,5,6):[4,5,6],(7,8,9):[7,8,9]}  #字典嵌套，因key值是不可变的，仅元素均为不可变数据类型的元组可做key，列表可做value
# list_b = {(1,2,3):(1,2,3),(4,5,6):(4,5,6),(7,8,9):(7,8,9)}  #字典嵌套，因key值是不可变的，仅元素均为不可变数据类型的元组可做key，元组可做value
# list_b = {(1,2,3):{1,2,3},(4,5,6):{4,5,6},(7,8,9):{7,8,9}}  #字典嵌套，因key值是不可变的，仅元素均为不可变数据类型的元组可做key，集合可做value
list_b = {(1, 2, 3): {1: 1, 2: 2, 3: 3}, (4, 5, 6): {4: 4, 5: 5, 6: 6},
          (7, 8, 9): {7: 7, 8: 8, 9: 9}}  # 字典嵌套，因key值是不可变的，仅元素均为不可变数据类型的元组可做key，字典可做value


# list_b = {((1,2,3),2,3):{1:1,2:2,3:3},(4,5,6):{4:4,5:5,6:6},(7,8,9):{7:7,8:8,9:9}}  #字典嵌套，因key值是不可变的，仅元素均为不可变数据类型的元组可做key，字典可做value
# list_b = {([1,2,3],2,3):{1:1,2:2,3:3},(4,5,6):{4:4,5:5,6:6},(7,8,9):{7:7,8:8,9:9}}  #第一个元组内包含可变数据类型列表，所以报错

# 需要参数化的参数也可以放入list里：@pytest.mark.parametrize(["name1","name2","name3"],list_b)，列表后面敲个实心点"."，可以使用list相关函数，可增删改查
# 需要参数化的参数也可以放入tuple里：@pytest.mark.parametrize(("name1","name2","name3"),list_b)，元组后面敲个实心点"."，可以使用tuple相关函数，无增删改查
# 需要参数化的参数可以是一个字符串，里面多个参数分别以逗号隔开
@pytest.mark.parametrize("name1,name2,name3", list_b)  # 当list_b为字典时，仅会传入key依次赋值给参数，而不会传入value
def test_bbb(name1, name2, name3):
    print(name1, name2, name3)
    print("测试多个参数的参数化")
    assert True


# 多个参数的参数化，示例2
# list_c = [(1+2,3),(9+4,7),(8+1,9)] #如果是这个列表传参，则assert test_input == expected就可以了，不需要使用eval()函数
list_c = (("1+2", 3), ("9+4", 7), ("8+1", 9))


# 用例重命名：case的默认名称是参数值，使用"ids=["用例1","用例2","用例3"]重命名用例名称，须和参数个数一致，且必须放在列表里
@pytest.mark.parametrize("test_input,expected", list_c, ids=["case1", "case2", "case3"])
def test_ccc(test_input, expected):
    print("test_input的值是：", test_input, "expected的值是：", expected)
    # 因为参数test_input是个字符串表达式，无法进行是否相等计算，eval()函数则是将字符串表达式转化为直接的表达式
    assert eval(test_input) == expected


# 笛卡尔积：如何使用ids=["a","b","c"]对用例名称重命名？？？？？？？？？？？？？
list_e = ["AA", "BB", "CC"]
list_f = ["XX", "YY", "ZZ"]


@pytest.mark.parametrize("func_test", list_e)
@pytest.mark.parametrize("code_test", list_f)
def test_dkrj(func_test, code_test):
    print("func_test的值是：", func_test, "code_test的值是：", code_test)
    print(f"func_test的值是：{func_test},code_test的值是：{code_test}")
    assert True
