#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
import datetime
from config import *
from faker import Factory
fake=Factory.create("zh_CN")

#新增系统
def new_system():
    sourceServerCode=fake.ean8()
    sourceServerName="新系统"+fake.name()
    url=f'{test_customer_url}/api/v2/agent/addSubSys'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "cientType": "web",
            "requestTime": "1613722946317",
            "requestId": "123456789012"
        },
        "reqBody": {
            "sourceServerName":sourceServerName ,
            "sourceServerCode":sourceServerCode,
            "protocol": "http",
            "remark": "测试",
            "serverIp": fake.ipv4(network=False),
            "domainName": None
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res,sourceServerName
# print(new_system())

#系统查询list
def system_list(sourceServerName):
    url=f'{test_customer_url}/api/v2/agent/subSysList'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "clientType": "web",
            "requestTime": "1613723083592",
            "requestId": "123456789012"
        },
        "reqBody": {
            "pageNumber": 1,
            "pageSize": 10,
            "sourceServerName": sourceServerName
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    serverCode=res["data"]["list"][0]["serverCode"]
    return res,serverCode
# print(system_list())

#系统编辑
def system_edit(serverCode):
    url=f'{test_customer_url}/api/v2/agent/editSubSys'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "clientType": "web",
            "requestTime": "1613805609988",
            "requestId": "123456789012"
        },
        "reqBody": {
            "serverCode": serverCode,
            "sourceServerName": "业务系统一",
            "sourceServerCode": "10000123",
            "protocol": "http",
            "remark": "测试",
            "serverIp": "172.18.110.60:36117",
            "domainName": None,
            "id": 20
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data))
    return res.json()
# print(system_edit(10000000214))

#系统停用
def system_no(serverCode):
    new_effectiveTime=(datetime.datetime.now()+datetime.timedelta(hours=13)).strftime("%Y-%m-%d %H:%M:%S")
    url=f'{test_customer_url}/api/v2/agent/subSysStop'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "clientType": "web",
            "requestTime": "1613805934155",
            "requestId": "123456789012"
        },
        "reqBody": {
            "serverCode": serverCode,
            "effectiveTime": str(new_effectiveTime)
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data))
    return res.json()
# print(system_no(10000000401))

#系统启用
def system_off(serverCode):
    url=f"{test_customer_url}/api/v2/agent/subSysResume"
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mocktoken",
            "clientType": "web",
            "requestTime": "1613805960807",
            "requestId": "123456789012"
        },
        "reqBody": {
            "serverCode": serverCode
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data))
    return res.json()
# print(system_off(10000000401))
