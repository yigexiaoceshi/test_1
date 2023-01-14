#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import json
from config import *
from faker import Factory
import jsonpath
fake=Factory.create("zh_CN")


def jiashichang(userId):
    url=f'{yanshi_customer_url}/api/v2/agent/cockpit/create'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": userId,
            "userName": "zhouwenfeng",
            "token": "mockToken",
            "mainUser": 1,
            "cientType": "web",
            "requestTime": "1621924199630",
            "requestId": "123456789012"
        },
        "reqBody": {
            "categoryCodes": [],
            "name": fake.name(),
            "businessType": "DEPT_SYSTEM",
            "desc": "cs",
            "areaCode": "330108000000",
            "isSync": 0
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    code01=res['data']['code']
    code=jsonpath.jsonpath(res,'$.data.code')[0]
    return res,code,code01


# print(jiashichang())

# if __name__ == '__main__':
#         print(jiashichang(756))



