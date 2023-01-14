#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import  *
# from Customer_platform.API.shujvxietong_new.shujvzhuce import data_zhuce

#我的数据-已注册-code查询
def mydata_yizhuce_chaxun(metaTableCode):
    url=f'{test_customer_url}/api/v4/dc/metaData/myData'
    header={"Content-Type":"application/json;charset=UTF-8","userid":"41"}
    data={
        "metaTableCode": metaTableCode,#数据code
        "status": 1,
        "size": 20,
        "page": 1
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    id=res["data"]["list"][0]["id"]
    return res,id
# print(mydata_yizhuce_chaxun(20201118896616057))

#我的数据-已注册-详情
def mydata_yizhuce_xiangqing(id):
    url=f'{test_customer_url}/api/v4/dc/metaData/tableDetail?'
    header={"userId":"41"}
    data={
        "id":id
    }
    res=requests.post(url,headers=header,data=data).json()
    id=res["data"]["id"]
    metaTableCode=res["data"]["metaTableCode"]
    dataName=res["data"]["dataName"]
    dataCode=res["data"]["dataCode"]
    columnInfoDTOS=res["data"]["columnInfoDTOS"]
    return res,id,metaTableCode,dataName,dataCode,columnInfoDTOS
# print(mydata_yizhuce_xiangqing())


#我的数据-已注册-编辑
def mydata_yizhuce_edit():
    url=f'{test_customer_url}/api/v4/dc/metaData/editTable'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"41"}
    data={
        "id": mydata_yizhuce_xiangqing()[1],
        "metaTableCode": mydata_yizhuce_xiangqing()[2],
        "dataCode": mydata_yizhuce_xiangqing()[4],
        "dataName": mydata_yizhuce_xiangqing()[3],
        "securityLevel": 2,
        "syncSecurityLevel": 2,
        "dataDesc": "接口编辑数据"+effectiveTime,
        "categoryCodes": [],
        "properties": mydata_yizhuce_xiangqing()[5]
    }
    res=requests.post(url,headers=header,data=json.dumps(data))
    return res.json()
# print(mydata_yizhuce_edit())

#我的数据-授权给我-查询
def shouquan_chaxun(dataCode):
    url=f'{test_customer_url}/api/v4/dc/metaData/authAndSubList'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"41"}
    data={
        "dataCode": dataCode,
        "size": 20,
        "page": 1
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(shouquan_chaxun("ods_1016_datazhuce1605689090911"))

#我的数据-授权给我-详情
def shouquan_xiangqing(id):
    url=f'{test_customer_url}/api/v4/dc/metaData/tableDetail?'
    header={"userId":"41"}
    data={"id":id}
    res=requests.post(url,headers=header,data=data).json()
    return res
# print(shouquan_xiangqing())

#我的数据-授权给我-设置订阅
def shouquan_xiangqing_dingyue(tableCode,callBackApiName,pushApiCode):
    url=f'{test_customer_url}/api/v4/dc/subscription/setSubscription'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"41"}
    data={
        "tableCode": tableCode,#数据表code
        "subscriptionType": 1,
        "maxPageSize": 0,
        "callBackApiName": callBackApiName,#接受API名称
        "pushApiCode": pushApiCode #接受APIcode
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(shouquan_xiangqing_dingyue())

#我的数据-订阅中-取消订阅
def dingyue_no():
    url=f'{test_customer_url}/api/v4/dc/subscription/cancelSubscription?'
    header={"userId":"41"}
    data={"tableCode": "20201118890916723"}
    res=requests.post(url,headers=header,data=data).json()
    return res
print(dingyue_no())