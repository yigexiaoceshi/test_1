#!/usr/bin/python3
# -*- coding:utf-8 -*-
from genson import SchemaBuilder

# 实例化SchemaBuilder
builder = SchemaBuilder()
# 添加符合的JSON数据
builder.add_object({"a": 1, "b": "aaaa", "c": "", "d": None})
builder.add_object({"a": 1, "b": "bbb", "c": 1})
# 生成JSONschema
print(builder.to_schema())
print(builder.to_json(indent=2))
