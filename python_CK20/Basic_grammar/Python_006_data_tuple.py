#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
元组：
1、通过小括号：()
2、元组（tuple)，列表[list]，range()，str 都是序列化数据类型
3、元组不可变，但是可以通过解包、索引来访问
4、如果元组中只有一个元素，须在元素后面加逗号","来消除歧义，如：(1,),("aaa",),([1,2,3],),((1,2,3),)等
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
tuple_c = (1, 2, 3)
# tuple_c[1] = "a"  #元素不可变
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
print(tuple_e.index(2))  # 元组中某元素的下标，即索引，有多个相同元素取第一个
# 使用元组生成器
tuple_f = (f * 2 for f in range(4))
print(tuple_f)  # 返回生成器对象
print(tuple(tuple_f))  # 返回元组

"""
嵌套：
1、元组内可嵌套列表：([1,2,3],["aaa","你好",True])
2、元组内可嵌套元组：((4,5,6),("yy",False,"dsfsfsd"))
3、元组内可嵌套集合:({1,2,3},{"sfd",3,"dsfs"})
4、元组内可嵌套字典:({"key1":"value1"},{"key2":"value2"})
"""
