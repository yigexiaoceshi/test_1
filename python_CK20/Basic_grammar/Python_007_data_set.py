#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
集合的定义：
1、无序
2、不重复
3、可使用 set() 或者 {} 创建集合
4、当{}里无任何元素时，优先默认是字典格式，所以空集合使用set()表示
5、集合里的每个值的数据类型必须是不可变的(可作为字典的key,可hash)，所以字典，元组，集合不可嵌套在集合里作为一个元素，而元组可以
"""
# 集合的定义
set_a = {1, 2, "你好", True, "%%", (1, 2)}  # 使用{}创建集合，单个字符串传入set()会自动去重，使用{}定义集合则不会
print(set_a)
print(type(set_a))

set_b = set()  # 使用set()创建集合
print(set_b)  # 空集合
print(len(set_b))  # 长度为0，空集合
print(type(set_b))
# set(表达式)创建集合,set里仅支持传入一个表达式
set_aa = set(range(1, 4))
print(set_aa)
# set([1,2,3])，分解列表到集合里时，仅支持传入一个参数（一个列表，一个元组，一个字典，一个集合等），单个元素可以多个
set_bb = set([4, 5, 6])  # 获取列表中所有的值创建集合
print("set_bb集合：", set_bb)
set_BBBB = set((44, 55, 66))  # 获取元组中所有的值创建集合
print(set_BBBB)
set_CCCC = set({1, 2, 3})  # 获取集合中所有元素创建集合
print(set_CCCC)
set_DDDD = set({1: 2, 3: 4})  # 获取字典中所有的key创建集合
print(set_DDDD)
# 表达式创建集合
set_aaa = {aaa for aaa in range(1, 11)}
print("set_aaa集合：", set_aaa)

set_bbb = {bbb for bbb in "aabbcdefg123"}  # 去重了
print("集合set_bbb：", set_bbb)
# 集合的内置函数
set_c = {1, 2, 3}
set_d = {1, 4, 5}
print(set_c.union(set_d))  # 求并集
print(set_c.intersection(set_d))  # 求交集
print(set_c.difference(set_d))  # 求差集，存在set_c不存在set_d
set_c.add(6)  # 添加元素
print("set_c集合：", set_c)
set_d.update("a", "b", "c")  # 没有指定替换元素，会直接添加，相当于 .add
print("set_d集合：", set_d)
# 单个字符串传入set()创建集合，会自动去重
e = "sfsfdsfsf  fsfsf"
print(set(e))  # 去重之后的集合
