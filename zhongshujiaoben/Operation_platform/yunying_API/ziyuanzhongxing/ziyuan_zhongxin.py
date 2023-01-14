#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import  json
import requests
from config import  *


class ziyuan_zx:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token

    #全部指数查询接口
    def indicator_chaxun(self,indicatorCode):
        url=f'{XXX_operation_url}/api/v2/operation/indicatorMarket'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": 1,
                "userName": "超级管理员",
                "token": "mockToken",
                "clientType": "web",
                "requestTime": "1611225159737",
                "requestId": "123456789012"
            },
            "reqBody": {
                "page": 1,
                "size": 10,
                "indicatorName": "",#指数名称
                "indicatorNote": "",
                "appShortName": "",#接入方简称
                "indicatorCode": indicatorCode   #输入指数code
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(indicator_chaxun())

    #全部API查询接口
    def apilist(self,apiCode):
        url=f'{XXX_operation_url}/api/v2/operation/apiList'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": 1,
                "userName": "超级管理员",
                "token": "mockToken",
                "clientType": "web",
                "requestTime": "1611225746375",
                "requestId": "123456789012"
            },
            "reqBody": {
                "page": 1,
                "size": 10,
                "appShortName": "",#输入接入方简称
                "apiCode": apiCode,#输入中枢APIcode
                "apiDesc": ""#输入API说明
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(apilist())

    #查看api详情
    def api_xiangqing(self,apiCode):
        url=f'{XXX_operation_url}/api/v2/operation/getApiDetail'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
        "reqHeader": {
                "userId": 1,
                "userName": "超级管理员",
                "token": "mockToken",
                "clientType": "web",
                "requestTime": "1611226023536",
                "requestId": "123456789012"
            },
            "reqBody": {
                "apiCode": apiCode   #APIcode
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return  res
    # print(api_xiangqing())

    #系统接入查询
    def system(self,appShortName):
        url=f'{XXX_operation_url}/api/v2/operation/metaDataUrlList'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": 1,
                "userName": "超级管理员",
                "token": "mockToken",
                "clientType": "web",
                "requestTime": "1611226237218",
                "requestId": "123456789012"
            },
            "reqBody": {
                "appShortName": appShortName,#输入接入方简称
                "pageNumber": 1,
                "pageSize": 10
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(metadata())

    #全部指数-区块链详情接口
    def current_indicator(self,sourceId):
        url=f'{XXX_operation_url}/api/v2/operation/blockchain/current'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": 1,
                "userName": "超级管理员",
                "token": "mockToken",
                "clientType": "web",
                "requestTime": "1611226524062",
                "requestId": "123456789012"
            },
            "reqBody": {
                "sourceId": sourceId,
                "type": 3 #指数    #type代理类型：指数、API、系统....等
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(current_indicator())

    #全部API-区块链详情接口
    def current_api(self,sourceId):
        url=f'{XXX_operation_url}/api/v2/operation/blockchain/current'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": 1,
                "userName": "超级管理员",
                "token": "mockToken",
                "clientType": "web",
                "requestTime": "1611226524062",
                "requestId": "123456789012"
            },
            "reqBody": {
                "sourceId": sourceId,
                "type": 2 #API    #type代理类型：指数、API、系统....等
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(current_api())

    #系统接入-区块链详情接口
    def current_system(self,sourceId):
        url=f'{XXX_operation_url}/api/v2/operation/blockchain/current'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": 1,
                "userName": "超级管理员",
                "token": "mockToken",
                "clientType": "web",
                "requestTime": "1611226524062",
                "requestId": "123456789012"
            },
            "reqBody": {
                "sourceId": sourceId,
                "type": 1 #系统接入    #type代理类型：指数、API、系统....等
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(current_matadata())
