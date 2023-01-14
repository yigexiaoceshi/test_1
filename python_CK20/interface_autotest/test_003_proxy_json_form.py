#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、设定代理格式
2、通过proxies参数传递代理设置（通过该参数监听请求与响应信息）
3、开启代理工具监听请求
4、一般的使用场景：使用代理和不使用代理的两次请求的对比，用来更直观的排查请求错误，相当于编写代码的debug
"""
import requests


class TestProxy():
    def setup_class(self):
        # 设置代理，需启动Charles，定义一个代理配置信息，key值为协议类型，value为代理服务器地址
        self.proxy = {"http": "http://127.0.0.1:8888", "https": "http:127.0.0.1:8888"}

    def test_json(self):
        data = {"hogwarts": "school"}
        # json请求，参数使用json=data传入请求体信息，参数verify=False表示不验证证书是否信任，'Content-Type':'application/json'
        r = requests.post("https://httpbin.testing-studio.com/post", json=data, proxies=self.proxy, verify=False)
        print(r.json())

    def test_form(self):
        data = {"hogwarts": "school"}
        # form请求，参数使用data=data传入请求体信息，'Content-Type':'application/x-www-form-urlencoded'
        r = requests.post("https://httpbin.testing-studio.com/post", data=data, proxies=self.proxy, verify=False)
        print(r.text)
