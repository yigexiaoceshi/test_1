#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import json
from config import *
import random

def APIshouquan(applyBillCode=None):
        url = f'{kaifa_jierufang_url}/api/v2/agent/customerIndicatorList'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId": userId_jierufang01,
                "userName": username,
                "token": token_jierufang,
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
        a=int(num)
        b=str(num)
        # number=json.dumps(num)
        return a,b
# print(APIshouquan()[0])


# 申请单号查询
def APIshouquanchaxun(applyBillCode=None):
        url = f'{kaifa_jierufang_url}/api/v2/agent/customerIndicatorList'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId": userId_jierufang01,
                "userName": username,
                "token": token_jierufang,
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
                "applyBillCode": APIshouquan(),
                "applyType": 1
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()


# print(APIshouquanchaxun(APIshouquan()))


def chakanxiangqing(applyBillCode=None):
        url = f'{kaifa_jierufang_url}/api/v2/agent/getApiAuthBillDetail'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId": userId_jierufang01,
                "userName": username,
                "token": token_jierufang,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "applyBillCode": APIshouquan()
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        photo = res.json()["data"]["authApplyBillDTO"]["filePath"]
        apibianma = res.json()["data"]["appApiThirdAuths"][0]["apiCode"]
        mdd=str(apibianma)
        return photo,mdd

# print(type(chakanxiangqing()[1]))


# 查看API详情
def api_xiangqing(apibianma=None):
        url = f'{kaifa_jierufang_url}/api/v2/agent/getApiDetail'
        header = {"Content-Type": "application/json"}
        data = {
            "reqHeader": {
                "userId": userId_jierufang01,
                "userName": username,
                "token": token_jierufang,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "apiCode": chakanxiangqing()[2]
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

# print(api_xiangqing())

def see_fujian():
    url = f'{kaifa_jierufang_url}'+chakanxiangqing()[0]
    print(url)
    res = requests.get(url)
    return res.status_code

print(see_fujian())


# def test_APIshouquan():
#     danhao = APIshouquan()
#     return  danhao
# print(test_APIshouquan())
#
# def test_APIxiangqingbianma():
#     bianma=chakanxiangqing()
#     return  bianma
# print(test_APIxiangqingbianma())