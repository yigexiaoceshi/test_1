#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-

import requests
import json
from faker import  Factory
from config import *
from Customer_platform.API.system.new_system  import system_list
#获取第三方随机数据
fake=Factory.create("zh_CN")

#指数API注册
def zhishu_api():
    url=f'{test_customer_url}/api/v2/agent/addApiV2'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "cientType": "web",
            "requestTime": "1613718746861",
            "requestId": "123456789012"
        },
        "reqBody": {
            "serviceName": "接口自动化"+fake.name(),
            "sourceApiCode": fake.ean8(),
            "apiInterval": "60",
            "path": "/api/"+fake.uri_path(deep=None),
            "serverCode": system_list()[1],
            "openLevel": 1,
            "contactor": "周一",
            "contactorMobile": "17757565881",
            "effectiveTime": "2021-02-20 03:11:13",
            "apiDesc": "接口自动化数据",
            "relationCategorys": [],
            "metaJson": "{\"APIRequestStructure\":{\"post\":{\"json\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"set\":true},\"properties\":{\"indicatorCycleRange\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true},\"properties\":{\"start\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true},\"title\":\"开始时间\"},\"end\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true},\"title\":\"结束时间\"}},\"required\":[],\"description\":\"可一次获取一个时间段内的指数值，对应值 start、end\",\"title\":\"时间维度范围\",\"dimensions\":[\"1000071;季;1;time\"]},\"indicatorCycle\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"title\":\"时间维度\",\"description\":\"如果为空，默认返回最新值\",\"dimensions\":[\"1000071;季;1;time\"]},\"indicatorCycles\":{\"type\":\"array\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"items\":{\"type\":\"string\",\"disabled\":{\"type\":true}},\"description\":\"可一次获取多个时刻指数值\",\"title\":\"时间维度集合\",\"dimensions\":[\"1000071;季;1;time\"]},\"areaCode\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"title\":\"区域\",\"dimensions\":[\"1000079;省;1;area\"]},\"areaCodes\":{\"type\":\"array\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"items\":{\"type\":\"string\",\"disabled\":{\"type\":true}},\"description\":\"\",\"title\":\"区域范围\",\"dimensions\":[\"1000079;省;1;area\"]}},\"required\":[\"areaCode\",\"indicatorCycle\"]},\"type\":\"json\"}},\"APIResponseStructure\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true},\"defaultData\":{\"data\":{\"object\":{\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}}},\"required\":[\"indicatorCycle\",\"areaCode\"]},\"array\":{\"items\":{\"type\":\"object\",\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}}},\"disabled\":{\"name\":true,\"type\":true,\"del\":true,\"set\":true,\"required\":true},\"required\":[\"indicatorCycle\",\"areaCode\"]}}}},\"properties\":{\"code\":{\"type\":\"string\",\"title\":\"状态码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true}},\"message\":{\"type\":\"string\",\"title\":\"错误信息\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true}},\"success\":{\"type\":\"boolean\",\"title\":\"是否成功\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true}},\"data\":{\"type\":\"object\",\"title\":\"返回数据\",\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true},\"dimensions\":[\"1000072;月;1;time\"]},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true},\"dimensions\":[\"1000079;省;1;area\"]},\"field_1\":{\"type\":\"number\",\"title\":\"数据一\"}},\"required\":[\"indicatorCycle\",\"areaCode\",\"field_1\"],\"disabled\":{\"name\":true,\"type\":false,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true},\"types\":[\"array\",\"object\"]}},\"required\":[\"code\",\"message\",\"success\",\"data\"]}}",
            "metaJsonExample": "{\"APIRequestStructure\":{\"post\":{\"json\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"set\":true},\"properties\":{\"indicatorCycleRange\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true},\"properties\":{\"start\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true},\"title\":\"开始时间\"},\"end\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true},\"title\":\"结束时间\"}},\"required\":[],\"description\":\"可一次获取一个时间段内的指数值，对应值 start、end\",\"title\":\"时间维度范围\",\"dimensions\":[\"1000071;季;1;time\"]},\"indicatorCycle\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"title\":\"时间维度\",\"description\":\"如果为空，默认返回最新值\",\"dimensions\":[\"1000071;季;1;time\"]},\"indicatorCycles\":{\"type\":\"array\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"items\":{\"type\":\"string\",\"disabled\":{\"type\":true}},\"description\":\"可一次获取多个时刻指数值\",\"title\":\"时间维度集合\",\"dimensions\":[\"1000071;季;1;time\"]},\"areaCode\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"title\":\"区域\",\"dimensions\":[\"1000079;省;1;area\"]},\"areaCodes\":{\"type\":\"array\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"items\":{\"type\":\"string\",\"disabled\":{\"type\":true}},\"description\":\"\",\"title\":\"区域范围\",\"dimensions\":[\"1000079;省;1;area\"]}},\"required\":[\"areaCode\",\"indicatorCycle\"]},\"type\":\"json\"}},\"APIResponseStructure\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true},\"defaultData\":{\"data\":{\"object\":{\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}}},\"required\":[\"indicatorCycle\",\"areaCode\"]},\"array\":{\"items\":{\"type\":\"object\",\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}}},\"disabled\":{\"name\":true,\"type\":true,\"del\":true,\"set\":true,\"required\":true},\"required\":[\"indicatorCycle\",\"areaCode\"]}}}},\"properties\":{\"code\":{\"type\":\"string\",\"title\":\"状态码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true}},\"message\":{\"type\":\"string\",\"title\":\"错误信息\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true}},\"success\":{\"type\":\"boolean\",\"title\":\"是否成功\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true}},\"data\":{\"type\":\"object\",\"title\":\"返回数据\",\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true},\"dimensions\":[\"1000072;月;1;time\"]},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true},\"dimensions\":[\"1000079;省;1;area\"]},\"field_1\":{\"type\":\"number\",\"title\":\"数据一\"}},\"required\":[\"indicatorCycle\",\"areaCode\",\"field_1\"],\"disabled\":{\"name\":true,\"type\":false,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true,\"required\":true},\"types\":[\"array\",\"object\"]}},\"required\":[\"code\",\"message\",\"success\",\"data\"]}}",
            "businessType": "INDICATOR",
            "method": "POST"
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    apiCode=res["data"]
    return res,apiCode
# print(zhishu_api())

#指数API列表查询
def zhishu_api_list(apiCode):
    url=f'{test_customer_url}/api/v2/agent/apiList'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "cientType": "web",
            "requestTime": "1613800121706",
            "requestId": "123456789012"
        },
        "reqBody": {
            "page": 1,
            "size": 20,
            "businessType": "INDICATOR",
            "apiCode":apiCode
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    id=res["data"]["records"][0]["id"]
    return  res,id
# print(zhishu_api_list(10000001402))

#指数API详情
def zhishu_api_xiangqing(apiCode):
    url=f'{test_customer_url}/api/v2/agent/getApiDetail'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "cientType": "web",
            "requestTime": "1613800518754",
            "requestId": "123456789012"
        },
        "reqBody": {
            "apiCode": apiCode
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(zhishu_api_xiangqing(10000001402))

#指数API停用
def zhishu_api_no(id):
    url=f'{test_customer_url}/api/v2/agent/apiState'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "cientType": "web",
            "requestTime": "1613804564454",
            "requestId": "123456789012"
        },
        "reqBody": {
            "id": id,
            "effectiveTime": str(effectiveTime),
            "state": 0
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(zhishu_api_no())

#指数API启用
def zhishu_api_off(id):
    url=f'{test_customer_url}/api/v2/agent/apiState'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 41,
            "userName": "周文峰",
            "token": "mockToken",
            "cientType": "web",
            "requestTime": "1613804564454",
            "requestId": "123456789012"
        },
        "reqBody": {
            "id": id,
            "effectiveTime": str(effectiveTime),
            "state": 1
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(zhishu_api_off())