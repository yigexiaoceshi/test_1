#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
# !/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import json
from config import *
import random


# from Customer_platform.API.renyuanguanli.woshenqingde.zhishushouquan import chakanxiangqing


class api():
    def __init__(self, url, userid, token):
        self.url = url
        self.userid = userid
        self.token = token

    # API授权-随机获取申请单号
    def APIshouquan(self, applyBillCode=None):
        url = f'{self.url}/api/v2/agent/customerIndicatorList'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId": self.userid,
                "userName": username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "sourceApiCode": None,
                "apiDesc": None,
                "targetAppName": "",
                "applyBillCode": applyBillCode,
                "applyType": 1
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        total = res.json()["data"]["total"]
        list1 = []
        for i in range(total):
            list1.append(res.json()["data"]["list"][i]["applyBillCode"])
        num = random.choice(list1)

        return num

    # 申请单号查询
    def APIshouquanchaxun(self, applyBillCode=None):
        url = f'{self.url}/api/v2/agent/customerIndicatorList'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId": self.userid,
                "userName": username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "sourceApiCode": None,
                "apiDesc": None,
                "targetAppName": "",
                "applyBillCode": applyBillCode,
                "applyType": 1
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    # print(APIshouquanchaxun())

    # 查看详情
    def chakanxiangqing(self, applyBillCode=None):
        url = f'{self.url}/api/v2/agent/getApiAuthBillDetail'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId": self.userid,
                "userName": username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "applyBillCode": applyBillCode
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        photo = res.json()["data"]["authApplyBillDTO"]["filePath"]
        apibianma = res.json()["data"]["appApiThirdAuths"][0]["apiCode"]
        return res.json(), apibianma, photo

    # a=chakanxiangqing()[0].split('9999')
    # print(a[1])

    # 查看附件
    def see_fujian(self, photo=None):
        url = f'{self.url}' + str(photo)
        # print(url)
        res = requests.get(url)
        return res.status_code

    # print(see_fujian())

    # 查看API详情
    def api_xiangqing(self, apiCode=None):
        url = f'{self.url}/api/v2/agent/getApiDetail'
        header = {"Content-Type": "application/json"}
        data = {
            "reqHeader": {
                "userId": self.userid,
                "userName": username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "apiCode": apiCode
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()


if __name__ == '__main__':
    danhao = api(5, 'zhou', 'kkkkkk')
    num = danhao.APIshouquan()
    nus = danhao.chakanxiangqing()
