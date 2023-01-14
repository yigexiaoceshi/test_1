#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、定制请求头信息，在参数headers={key:value}
2、已经知道cookie的情况下，如何携带cookie发起请求
    a、放在请求头里，通过headers={"Cookie":"value"}的方式，得到"Cookie":"value"
    b、放在请求参数里，通过cookies={key1:value1,key2:value2}，得到"Cookie":"key1=value1;key2=value2"
"""
import requests


# cookie的传递，放在请求头里
def test_cookie1():
    url = 'https://httpbin.testing-studio.com/cookies'
    headers = {
        "Cookie": "Hogwarts_school",  # 首字母大写，没有s:Cookie
        "User-Agent": "python-requests/2.26.0_test"  # 定制请求头信息
    }
    r = requests.get(url, headers=headers)
    print(r.request.headers)


# cookie的传递，requests的内置参数cookies
def test_cookie2():
    url = 'https://httpbin.testing-studio.com/cookies'
    headers = {
        "User-Agent": "Hello_Python3"
    }
    cookies = dict(cookies_1='working1', cookies_2='working2')  # cookie可以多个
    r = requests.get(url, headers=headers, cookies=cookies)  # 作为参数传递，参数名"cookies"
    print(r.request.headers)
