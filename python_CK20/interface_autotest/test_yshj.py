#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests

# access_token = []
host = 'http://standard.cspiretech.com'


def test_login():
    url = host + '/api/v1/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic Yjc4MThmN2EwODg2NGRkNDllNTkwMjdiODAzMGU3ZDc6NDAxMThlMGJiZjNiNDY4ZDgzYzA2ZWU1YzkyYTM2ODI=',
        "Connection": 'keep-alive'
    }
    body = dict(grant_type='client_credentials')
    res = requests.post(url, headers=headers, data=body)
    print(res.text)
    # global access_token
    access_token = res.json()['access_token']
    # access_token.append(res.json()['access_token'])
    # print('access_token是：', access_token)
    # print('access_token第一个元素是：', access_token[0])
    return access_token


def test_api():
    access_token = test_login()
    print('access_token是：', access_token)
    url = host + '/api/v1/source/10000004100'
    headers = {
        'Authorization': access_token
    }
    res = requests.get(url, headers=headers)
    print(res.text)
    print(res.status_code)


def test_indicator():
    access_token = test_login()
    url = host + '/api/v2/indicator/10000007000'
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    body = {
        "areaCodes": ["330106000000", "330108000000"],
        "indicatorCycles": ["20220101", "20220202", "20220303"],
        "sex": "女"
    }
    res = requests.post(url, headers=headers, json=body)
    print(res.text)
    print(res.status_code)
    assert res.json()['success'] == True
