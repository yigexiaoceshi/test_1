#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import *
from faker import  Factory
fake=Factory.create("zh_CN")

#iot产品
class product:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token
    #新增IoT产品
    def new_product(self):
        name=fake.name()
        url=f'{self.url}/api/v2/agent/product/singleCreate'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "name": name+"的产品",
                "vendor": name+"有限公司",
                "version": fake.ean8(),
                "protocolCode": "melsec_mc",
                "remark": "测试",
                "categoryCodes": [
                ]
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1616996069444",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        id=res["data"]
        return res,id,name
    # print(new_product())

    #iot产品查询接口
    def product_list(self,name):
        url=f'{self.url}/api/v2/agent/product/searchProducts'
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
                "requestTime": "1617084608677",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(product_list("侯丹丹的产品"))

    #IoT产品详情接口
    def product_xiangqing(self,id):
        url=f'{self.url}/api/v2/agent/product/selectInfo'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1617084824670",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(product_xiangqing("89294"))

    #lot产品编辑接口
    def product_edit(self,id,name):
        url=f'{self.url}/api/v2/agent/product/updateProduct'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "name": name+"编辑后的产品",
                "vendor": "江桂香有限公司",
                "version": "75349332",
                "protocolCode": "melsec_mc",
                "remark": "测试",
                "categoryCodes": [],
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1617086425635",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(product_edit(89296,"江桂香"))

    #iot产品-添加指令接口
    def product_zhiling(self,id):
        name=fake.name()
        url=f'{self.url}/api/v2/agent/productInstruction/add'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "name": f"{name}的指令",
                "remark": "测试",
                "parameters": [{
                    "must": 0,
                    "name": "ID",
                    "remark": "测试编号",
                    "type": "integer",
                    "id": None
                }, {
                    "must": 0,
                    "name": "name",
                    "remark": "测试用户名",
                    "type": "string",
                    "id": None
                }],
                "metaJson": "{\"APIResponseStructure\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true},\"defaultData\":{\"data\":{\"object\":{\"properties\":{},\"required\":[\"indicatorCycle\",\"areaCode\"]},\"array\":{\"items\":{\"type\":\"object\",\"properties\":{},\"disabled\":{\"name\":true,\"type\":true,\"del\":true,\"set\":true,\"required\":true},\"required\":[\"indicatorCycle\",\"areaCode\"]}}}},\"properties\":{\"data\":{\"type\":\"object\",\"title\":\"参数名称\",\"properties\":{},\"required\":[\"indicatorCycle\",\"areaCode\"],\"types\":[\"object\"]}},\"required\":[\"code\",\"message\",\"success\",\"data\"]}}",
                "businessId": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1617085076904",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        zhiling_id=res["data"]
        return res,name,zhiling_id
    # print(product_zhiling("89294"))

    #iot_指令编辑
    def product_zhiling_edit(self,name,id,zhiling_id):
        url=f'{self.url}/api/v2/agent/productInstruction/update'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "name": name+"编辑后的指令",
                "remark": "测试",
                "parameters": [{
                    "must": 0,
                    "name": "ID",
                    "remark": "测试编号",
                    "type": "integer",
                    "id": 35
                }, {
                    "must": 0,
                    "name": "name",
                    "remark": "测试用户名",
                    "type": "string",
                    "id": 36
                }],
                "metaJson": "{\"APIResponseStructure\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true},\"defaultData\":{\"data\":{\"object\":{\"properties\":{},\"required\":[\"indicatorCycle\",\"areaCode\"]},\"array\":{\"items\":{\"type\":\"object\",\"properties\":{},\"disabled\":{\"name\":true,\"type\":true,\"del\":true,\"set\":true,\"required\":true},\"required\":[\"indicatorCycle\",\"areaCode\"]}}}},\"properties\":{\"data\":{\"type\":\"object\",\"title\":\"参数名称\",\"properties\":{},\"required\":[\"indicatorCycle\",\"areaCode\"],\"types\":[\"object\"]}},\"required\":[\"code\",\"message\",\"success\",\"data\"]}}",
                "businessId": id,
                "id": zhiling_id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1617085364232",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(product_zhiling_edit())

    #iot_指令删除
    def product_zhiling_del(self,zhiling_id):
        url=f'{self.url}/api/v2/agent/productInstruction/delete'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "id": zhiling_id,
                "secondaryConfirm": True
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1617086182917",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(product_zhiling_del(23))

    #iot产品_删除
    def product_del(self,id):
        url=f'{self.url}/api/v2/agent/product/deleteProduct'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "secondaryConfirm": True,
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1617086692492",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
# print(product_del())