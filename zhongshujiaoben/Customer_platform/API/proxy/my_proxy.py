#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import *
from faker import  Factory

fake=Factory.create("zh_CN")

newtime = effectiveTime

class My_proxy():
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token

    #我的服务-列表查询
    def my_proxy_list(self,appCode):
        url=f'{self.url}/api/v2/agent/proxyServer/myServer/myList'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "page": 1,
                "size": 10,
                "appCode": appCode
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1615343570119",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        id=res["data"]["list"][0]["id"]
        zsCode=res["data"]["list"][0]["zsCode"]
        return res,id,zsCode
    # print(my_proxy_list(1407374889844762))

    #我的服务-详情
    def my_proxy_xiangqing(self,id):
        url=f'{self.url}/api/v2/agent/proxyServer/myServer/info'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1615343835297",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return  res
    # print(my_proxy_xiangqing(36))

    #我的服务-区块链入链
    #sourceId=zscode  服务code
    def my_proxy_qukuailian(self,sourceId):
        url=f'{self.url}/api/v2/blockchain/current'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1615344576535",
                "requestId": "123456789012"
            },
            "reqBody": {
                "sourceId": sourceId,
                "type": 11 #代理服务
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return  res
    # print(my_proxy_qukuailian(1407374889844761))

    #我的服务-编辑
    def my_proxy_edit(self,zsCode,id):
        url=f'{self.url}/api/v2/agent/proxyServer/myServer/update'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "appCode": "zcj15679253",
                "name": "编辑后"+fake.name()+"的代理服务",
                "url": "http://"+fake.ipv4(network=False),
                "healthPath": "/tags/"+fake.uri_path(deep=None),
                "accessPermission": "2",
                "remark": "测试数据编辑后的时间  "+newtime,
                "zsCode": zsCode,
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1615344105095",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(my_proxy_edit(1407374889844762,36))

    #我的服务-停用
    def my_proxy_disable(self,id):
        url=f'{self.url}/api/v2/agent/proxyServer/myServer/disable'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1615344943186",
                "token": self.token,
                "userId":self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return  res
    # print(my_proxy_disable(36))

    #我的服务-启用
    def my_proxy_enable(self,id):
        url=f'{self.url}/api/v2/agent/proxyServer/myServer/enable'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1615345164956",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return  res
    # print(my_proxy_enable(36))

# if __name__ == '__main__':
#     print(My_proxy(yanshi_customer_url,757,"周一","mockToken").my_proxy_list("zcj96169360"))