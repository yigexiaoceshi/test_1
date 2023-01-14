#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys

list_b = {((1, 2, 3), 2, 3): {1: 1, 2: 2, 3: 3}, (4, 5, 6): {4: 4, 5: 5, 6: 6}, (7, 8, 9): {7: 7, 8: 8, 9: 9}}  # 写法正确

print(type(list_b))
print(list_b)

# 第一组key/value里的key是个包含了可变数据类型list的tuple，所以报错
# list_c = {([1,2,3],2,3):{1:1,2:2,3:3},(4,5,6):{4:4,5:5,6:6},(7,8,9):{7:7,8:8,9:9}}
# print(type(list_c))
# print(list_c)


companies = [[{"id": 1, "name": "company1", "prince": "200W"}], [{"id": 2, "name": "company2", "price": "500W"}]]
test = [[{"by": "id"}], [{"locator": "name"}], [{"action": "click"}]]
