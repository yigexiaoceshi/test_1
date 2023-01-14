#!/usr/bin/python3
# -*- coding:utf-8 -*-
from filecmp import cmp

# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# list2 = list1[8::-1]
# print(list2)
#
# for i in range(5, -1, -1):
#     print(i)
a = "abcdefg你好"
b = a.replace("你好", "新的你好")
print(a)
print(b)

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict1.pop("aa", "c")
print(dict1)
