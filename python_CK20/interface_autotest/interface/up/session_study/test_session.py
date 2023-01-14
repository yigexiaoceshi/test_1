#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests


def test_get_use_detail():
    # 先进性登录
    login_url = "http://127.0.0.1:5000/login"
    json = {
        "phone": "13888888888",
        "password": "123456"
    }
    r = requests.post(url=login_url, json=json)
    print(r.json())
    user_cookies = r.cookies.get("y-token")
    print("用户的cookies是：", user_cookies)
    # 再获取用户信息，并未实现session的传递，提示用户未登录
    get_detail_url = "http://127.0.0.1:5000/user/detail"
    r = requests.get(url=get_detail_url)
    print(r.cookies.get("y-token"))
    print(r.json())


def test_get_detail():
    session = requests.session()
    # 课程提供的可用的服务：http://47.92.149.0:9000
    login_url = "http://127.0.0.1:5000/login"
    login_data = {
        "phone": "13888888888",
        "password": "123456"
    }
    r = session.post(url=login_url, json=login_data)
    print(r.cookies.get("y-token"))
    get_user_detail_url = "http://127.0.0.1:5000/user/detail"
    r = session.get(url=get_user_detail_url)
    print(r.cookies.get("y-token"))
    print(r.json())
