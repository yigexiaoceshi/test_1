# -*- coding:utf-8 -*-
"""
元组：
1、通过小括号：()
2、元组（tuple)，列表[list]，range 都是序列数据类型
3、元组不可变，但是可以通过解包、索引来访问
"""
# 元组的定义
tuple_a = (1, 2, 3)
print(tuple_a)

tuple_b = 1, 2, 3  # 可以不加小括号
print(type(tuple_b), tuple_b)
"""
1、元素不可变
2、但是列表作为元组的一个元素，列表里的元素是可变的，因为元组里的列表其实对应的是一个指针地址(内存地址)，这个指针地址不可变，列表里的元素可变
"""
# 改变嵌套在元组内的列表里的元素，不等同于改变元组
tuple_c = (1, 2, 3)
# tuple_c[1] = "a"
list_a = [1, 2, 3]
tuple_d = ("a", "b", "c", list_a)
print(id(tuple_d[3]))  # 列表元素修改之前，通过id()获取当前元组的第四个元素的指针地址（内存地址）
print(tuple_d)
list_a[1] = "A"
print(tuple_d)
print(id(tuple_d[3]))  # 列表元素修改之后，通过id()获取当前元组的第四个元素的指针地址（内存地址）

"""
元组的内置函数
"""
tuple_e = (1, 2, 2, 2, 3)
print(tuple_e.count(2))  # 元组中某元素出现次数，注意 2 和 "2"的不同
print(tuple_e.index(2))  # 元组中某元素的下标，即索引，有多个元素取第一个
