#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests

# get请求示例：
a = requests.get("http://www.baidu.com")
print(a)
print(a.status_code)
print(a.headers)
print(a.encoding)
print(a.text)  # 打印返回值，很多中文乱码显示
a.encoding = 'utf-8'  # 切换编码格式
print(a.text)  # 输出正常，乱码解决

# post请求示例：
b = requests.post("http://httpbin.org/post", data={"key": "value"})
print(b.text)
print(b.json())
