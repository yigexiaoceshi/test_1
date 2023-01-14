#!/usr/bin/python3
# -*- coding:utf-8 -*-
import json

"""
Json定义：轻量级的数据交换格式
1、友好，容易读写（比xml，protobuf，yaml要好）
2、对机器友好，易于解析和生成
3、由列表和字典组成：一般为字典格式，字典里嵌套字典或者列表
使用场景：
1、生成：将对象生成为字符串，存入文件，数据库，在网络传输等
2、解析，解析来自文件，数据库，网络传输的字符串或Python对象
3、跨语言的数据交换：比如Python和C/C++/Java/JavaScripts等都支持JSON
"""
# 定义一个字典格式的JSON
json_test1 = {
    "name": ["lili", "xiao9"],
    "age": 17,
    "gender": "female"
}
print(json_test1)
print(type(json_test1))
# 定义一个列表格式的JSON
json_test2 = [
    {
        "name": "laoli",
        "age": 17,
        "sex": "man"
    }
]
print(json_test2)
print(type(json_test2))

# 常用方法1：json.dump(python_obj)，把数据类型转换成字符串
json_str1 = json.dumps(json_test1)
print(json_str1)
print(type(json_str1))  # str，字符串型
json_str2 = json.dumps(json_test2)
print(type(json_str2))  # str，字符串型

# 常用方法2：json.loads(json_string)，把字符串转换成JSON
print(type(json.loads(json_str1)))
print(type(json.loads(json_str2)))

# 常用方法3：json.dupm()，把数据类型转换成字符串并储存在文件中

# 常用方法4：json.load(file_stream)，把文件打开，把里面的字符转换成数据类型
