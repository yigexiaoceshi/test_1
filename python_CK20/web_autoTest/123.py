#!/usr/bin/python3
# -*- coding:utf-8 -*-
a = 1
b = [1, 2]

for i in b:
    print(i)
    print(type(i))
    if a != i:
        a = i
    else:
        pass
print(a)
