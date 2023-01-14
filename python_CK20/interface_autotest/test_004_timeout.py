#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests

import requests


class TestProxy():
    def setup_class(self):
        # 设置代理，需启动Charles，并配置好代理
        self.proxy = {"http": "http://127.0.0.1:8888", "https": "https://127.0.0.1:8888"}

    def test_json_one(self):
        data = {"hogwarts": "school"}
        r = requests.post("https://httpbin.testing-studio.com/post", json=data)
        print(r.json())

    def test_json_two(self):
        data = {"hogwarts": "school"}
        # 设置timeout=3参数，单位是秒，超过该时间没有得到服务器相应，会自动抛错
        # 可在Charles当前请求上右键选择Breakpoints(断点)，此时不加timeout会一直阻塞，加了断点阻塞3秒之后会跳过该用例继续执行
        r = requests.post("https://httpbin.testing-studio.com/post", json=data, proxies=self.proxy, verify=False,
                          timeout=3)
        print(r.json())

    def test_json_three(self):
        data = {"hogwarts": "school"}
        r = requests.post("https://httpbin.testing-studio.com/post", json=data)
        print(r.json())
