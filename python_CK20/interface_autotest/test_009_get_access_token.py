#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
获取企业微信通讯录模块的access_token
"""
import requests


class TestToken:

    def test_get_access_token(self):
        """

        :return:
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        corpid = 'ww06c7843f5a3300cb'
        corpsecret = 'p10fPmcNBibLSZsp_rZYXXqAKCFkrDw8BVAn1RtIRGI'
        params_data = {
            'corpid': corpid,
            'corpsecret': corpsecret
        }
        #  根据接口文档定义，参数以query的形式传递
        res = requests.get(url=url, params=params_data)
        # 或者将params参数直接写入URL中
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # res = requests.get(url=url)
        print(res.json())
        print("获取到的access_token为：", res.json()['access_token'])
