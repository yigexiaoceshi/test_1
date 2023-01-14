#!/usr/bin/python3
# -*- coding:utf-8 -*-

from interface_autotest.interface.apis.base_api import BaseApi


class WeWork(BaseApi):

    def get_access_token(self, corpid, corpsecret):
        """
        获取企业微信各个应用的token
        :param corpid: 公司ID
        :param corpsecret: 每个应用的密钥
        :return:
        """
        # 定义获取token需要的两个入参
        # corpid = "ww06c7843f5a3300cb"
        # corpsecret = "p10fPmcNBibLSZsp_rZYXXqAKCFkrDw8BVAn1RtIRGI"  # 通讯录同步的secret
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        #  获取token的URL是固定的，此处写死
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        #  发起获取token的get请求
        r = self.send("GET", url, params=params, tool="requests")
        #  返回获取到的token值
        # return r.json()['access_token']
        return r.json().get("access_token")
