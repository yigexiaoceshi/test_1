#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests


class TestGetAccessToekn():
    def test_get_access_token(self):
        # 写法1：以字典形式，通过params参数传递query参数
        data = {
            "corpid": "ww06c7843f5a3300cb",
            "corpsecret": "p10fPmcNBibLSZsp_rZYXXqAKCFkrDw8BVAn1RtIRGI"  # 通讯录同步的secret
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url, params=data)

        # 写法2：通过字符串字面量赋值的写法，写完整的URL
        # corpid = "ww06c7843f5a3300cb"
        # corpsecret = "p10fPmcNBibLSZsp_rZYXXqAKCFkrDw8BVAn1RtIRGI"
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # r = requests.get(url)
        #
        # print("access_token为：", r.json()['access_token'])  # 这种写法当access_token没有值的时候会抛错，keyerror
        print("access_token为：", r.json().get('access_token'))  # 建议使用get('key')的方法获取json里的value值，如果key不存在，获取到空的value不会抛错
        # assert r.json()['errcode'] == 0
        # assert r.json()['errmsg'] == 'ok'
        return r.json()['access_token']
