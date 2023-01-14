#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import json
from config import *
from Operation_platform.yunying_API.renyuanguanli.newuser_customer import new_customer
from faker import Factory
fake=Factory.create("zh_CN")

#指数注册
def zhishu_zhuce():
    #获取注册接入方的名称
    jierufang_name=new_customer(XXX_operation_url,userId_yunying,token_yunying,username_yunying).add_jierufang()[1]
    # print(jierufang_name)
    #根据名称去获取接入方ID
    responsibleAppInfoId=new_customer(XXX_operation_url,userId_yunying,token_yunying,username_yunying).user_chaxun(jierufang_name)[1]
    # print(responsibleAppInfoId)
    url=f'{XXX_customer_url}/api/v2/agent/indicator/addIndicator'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "cientType": "web",
            "requestTime": "1611663755116",
            "requestId": "123456789012"
        },
        "reqBody": {
            "indicatorName": "接口脚本+"+effectiveTime,
            "indicatorUnit": "m",
            "sourceIndicatorCode": "",
            "indicatorNote": "接口自动化数据",
            "computeNote": "测试规则",
            "businessContacts": fake.name(),
            "businessPhone": fake.phone_number(),
            "responsibleAppInfoId": responsibleAppInfoId,
            "responsibleLeader": "周三",
            "indicatorCategorys": [],
            "refreshCycle": {
                "dimensionCode": "1000075",
                "name": "每时",
                "isPeriodically": 1
            },
            "applyRange": {
                "dimensionCode": 1000082,
                "name": "乡镇"
            },
            "usableDimension": [],
            "step": 1
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return  res
# print(zhishu_zhuce())
