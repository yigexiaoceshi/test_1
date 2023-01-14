#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
认证体系;
1、基本认证（Basic access authentication)：http basic，是允许http用户代理在请求时，提供用户名和密码的一种认证方式
    Authorization:Basic QRWERSFFSFFfsdfsdfsfu230jfsofjs==
2、
"""
import requests
from requests.auth import HTTPBasicAuth


def test_author():
    res = requests.get("https://httpbin.testing-studio.com/basic-auth/banana/123",
                       auth=HTTPBasicAuth("banana", "123"))
    print(res.text)
