#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
数据类型可变性理解：可变不可变是针对同一个内存地址来讲，值是否可以修改，修改了变量的值，内存地址不变则称为可变数据类型，反之亦反
1、不可变数据类型：如果该数据对应变量的值发生改变后，该数据对应的内存地址也发生了改变
2、可变数据类型：如果该数据对应变量的值发生改变后，该数据对应的内存地址不会发生改变

小结：
可变：列表list、集合set、字典dict
不可变：整型int、字符串string、元组tuple
"""

"""整型  int   """
int_a = 1
print("int_a为", int_a)
print(id(int_a), type(int_a))
int_a = 2
print("int_a为", int_a)
print(id(int_a), type(int_a))
# 变量值发生改变后，内存地址发生了改变，所以整型(int)为：不可变数据类型

"""字符串  'string'  """
str_b = "Hello Python"
print("str_b为", str_b)
print(id(str_b), type(str_b))
str_b = "Hello Python3"
print("str_b为", str_b)
print(id(str_b), type(str_b))
# 变量值发生改变后，内存地址发生了改变，所以字符串型(string)为：不可变数据类型

"""列表[list]"""
list_c = [1, 2, 3]
print("list_c为", list_c)
print(id(list_c), type(list_c))
list_c[0] = 4
print("list_c为", list_c)
print(id(list_c), type(list_c))
# 列表第一个元素的值发生了改变，内存地址未发生改变，所以列表为：可变数据类型

"""元组（tuple）"""
list_d = ["a", "b", "c"]
tuple_d = (1, 2, ["a", "b", list_d])
print("tuple_d为", tuple_d)
print(id(tuple_d), type(tuple_d))
list_d[2] = "CCCCC"
print("tuple_d为", tuple_d)
print(id(tuple_d), type(tuple_d))
# 元组内第三个元素为列表，当一个列表内的元素发生改变时，该列表的内存地址是不发生改变的，所以可以认为这个列表无论里面的元素值怎么变化，这个列表
# 都没有发生变化，所以元组的值未发生变化，元组为：不可变数据类型

"""集合  {"set1","set2"}  """
set_e = {1, 2, True, "Hello Python"}
print(set_e)
print(id(set_e), type(set_e))
set_e.add(666)
print(set_e)
print(id(set_e), type(set_e))
# 集合内新增了一个元素，对应的内存地址未发生改变，所以集合{"set_1","set_2"}为：可变数据类型

"""字典"""
list_f = ["XX", "YY", "ZZ"]
tuple_f = ("x", "y", "z")
dict_f = {1: 2, "AA": "BB", tuple_f: list_f}
print(dict_f)
print(id(dict_f), type(dict_f))
list_f[2] = "ZZZZZZZZZ"
print(dict_f)
print(id(dict_f), type(dict_f))
# 字典内value值发生了改变后，内存地址未发生改变，所以字典{key1:value1,key2:value2}为：可变数据类型
