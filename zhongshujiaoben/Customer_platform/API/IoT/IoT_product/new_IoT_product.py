#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
import random
from config import *
from faker import  Factory

fake=Factory.create("zh_CN")

#IoT新增产品
def new_product():
    list=["手表","电脑","手机","耳机","平板","电动车","电动窗帘"]
    url=f'{yanshi_customer_url}/api/v2/agent/product/singleCreate'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqBody": {
            "name": fake.name()+"的"+random.choice(list),
            "vendor": fake.company(),
            "version": fake.pyint(),
            "protocolCode": "modbus_tcp",
            "remark": "测试",
            "categoryCodes": [1000704]
        },
        "reqHeader": {
            "clientType": "web",
            "requestId": "123456789012",
            "requestTime": "1615890474628",
            "token": "mockToken",
            "userId": 757,
            "userName": "周一"
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(new_product())

#lot产品列表查询
def product_list(name):
    url=f'{yanshi_customer_url}/api/v2/agent/product/searchProducts'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqBody": {
            "page": 1,
            "size": 10,
            "name": name
        },
        "reqHeader": {
            "clientType": "web",
            "requestId": "123456789012",
            "requestTime": "1615891367819",
            "token": "mockToken",
            "userId": 757,
            "userName": "周一"
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    id=res["data"]["list"][0]["id"]
    return res,id
# print(product_list("黄佳的手机"))

#lot产品-详情
def product_xiangqing(id):
    url=f'{yanshi_customer_url}/api/v2/agent/product/selectInfo'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqBody": {
            "id": id
        },
        "reqHeader": {
            "clientType": "web",
            "requestId": "123456789012",
            "requestTime": "1615891513762",
            "token": "mockToken",
            "userId": 757,
            "userName": "周一"
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(product_xiangqing(24))

#IoT产品-新增指令
def product_zhiling(businessId):
    url=f'{yanshi_customer_url}/api/v2/agent/productInstruction/add'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqBody": {
            "name": fake.word(),
            "remark": "接口脚本测试",
            "parameters": [{
                "must": 1,
                "name": "id",
                "remark": "编号",
                "type": "number",
                "id": None
            }, {
                "must": 1,
                "name": "name",
                "remark": "用户名",
                "type": "string",
                "id": None
            }],
            "metaJson": "{\"APIResponseStructure\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,"
                        "\"set\":true},\"defaultData\":{\"data\":{\"object\":{\"properties\":{},\"required\":[\"indicatorCycle\",\"areaCode\"]},"
                        "\"array\":{\"items\":{\"type\":\"object\",\"properties\":{},\"disabled\":{\"name\":true,\"type\":true,\"del\":true,"
                        "\"set\":true,\"required\":true},\"required\":[\"indicatorCycle\",\"areaCode\"]}}}},\"properties\":{\"data\":{\"type\":\"object\","
                        "\"title\":\"参数名称\",\"properties\":{},\"required\":[\"indicatorCycle\",\"areaCode\"],\"types\":[\"object\"]}},\"required\":[\"code\","
                        "\"message\",\"success\",\"data\"]}}",
            "businessId": businessId
        },
        "reqHeader": {
            "clientType": "web",
            "requestId": "123456789012",
            "requestTime": "1615891829164",
            "token": "mockToken",
            "userId": 757,
            "userName": "周一"
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(product_zhiling(24))

#IoT产品-编辑
def product_edit(id):
    list01 = ["手表", "电脑", "手机", "耳机", "平板", "电动车", "电动窗帘"]
    url=f'{yanshi_customer_url}/api/v2/agent/product/updateProduct'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqBody": {
            "name": "编辑后"+fake.name()+random.choice(list01),
            "vendor": "黄石金承传媒有限公司",
            "version": "9898",
            "protocolCode": "modbus_tcp",
            "remark": "编辑后的接口脚本数据",
            "categoryCodes": ["1000704"],
            "id": id
        },
        "reqHeader": {
            "clientType": "web",
            "requestId": "123456789012",
            "requestTime": "1615892175745",
            "token": "mockToken",
            "userId": 757,
            "userName": "周一"
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(product_edit(24))

#IoT产品-删除
def product_delete(id):
    url=f'{yanshi_customer_url}/api/v2/agent/product/deleteProduct'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqBody": {
            "secondaryConfirm": True,
            "id": id
        },
        "reqHeader": {
            "clientType": "web",
            "requestId": "123456789012",
            "requestTime": "1615892519378",
            "token": "mockToken",
            "userId": 757,
            "userName": "周一"
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(product_delete(22))