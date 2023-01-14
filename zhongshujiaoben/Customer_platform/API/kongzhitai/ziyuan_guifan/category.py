#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import  *
from faker import  Factory

fake=Factory.create("zh_CN")

class category:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token

    #新增自定义类目
    def add_category(self):
        name=fake.name()+"接口测试脚本类目一"
        url=f'{self.url}/api/v2/agent/category/categoryAdd'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1615961991407",
                "requestId": "123456789012"
            },
            "reqBody": {
                "name":name,
                "appTypes": [{
                    "appCode": "api",
                    "required": 0
                }, {
                    "appCode": "data",
                    "required": 0
                }, {
                    "appCode": "indicator",
                    "required": 0
                }],
                "child": [{
                    "id": 1615961970720,
                    "lev": 1,
                    "name": "接口类目一",
                    "parentId": 0,
                    "tier": 1,
                    "children": [],
                    "addAction": True,
                    "editAction": True,
                    "delAction": True
                }],
                "categoryDesc": "接口脚本数据",
                "type": "Customer",
                "addType": "group"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res,name
    # print(add_category())

    #类目获取类目ID接口
    def cate_huoqu(self,cate_name):
        # cate_name=self.add_category()[1]
        url=f'{self.url}/api/v2/agent/category/categoryTree'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1615963671224",
                "requestId": "123456789012"
            },
            "reqBody": {
                "type": "Customer"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        data01=res["data"]
        lwn=len(data01)
        for i in range(lwn):
            name=res["data"][i]["name"]
            if cate_name==name:
                # print(name)
                id = res["data"][i]["id"]
                return res,id
    # print(cate_huoqu())

    #添加子类目
    def cate_zileimu(self,id):
        url=f'{self.url}/api/v2/agent/category/categoryAdd'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1615962820463",
                "requestId": "123456789012"
            },
            "reqBody": {
                "name": "接口类目二_添加子类目"+fake.ean8(),
                "parentId": id,
                "type": "Customer",
                "addType": "category"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return  res
    # print(cate_zileimu(cate_huoqu("周建国接口测试脚本类目一")))

    #编辑类目
    def cate_edit(self,name,id):
        url=f'{self.url}/api/v2/agent/category/categoryEdit'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1616033564886",
                "requestId": "123456789012"
            },
            "reqBody": {
                "name": name,
                "appTypes": [{
                    "appCode": "api",
                    "required": 0
                }, {
                    "appCode": "data",
                    "required": 0
                }, {
                    "appCode": "indicator",
                    "required": 0
                }],
                "categoryDesc": "编辑后的接口脚本数据",
                "type": "Customer",
                "addType": "group",
                "id": id
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(cate_edit(1144))


    #停用类目
    def cate_state(self,id):
        url=f'{self.url}/api/v2/agent/category/stateChange'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1615970892334",
                "requestId": "123456789012"
            },
            "reqBody": {
                "id": id,
                "state": 0
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(cate_state(1144))

    #启用类目
    def cate_state_off(self,id):
        url=f'{self.url}/api/v2/agent/category/stateChange'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1615970892334",
                "requestId": "123456789012"
            },
            "reqBody": {
                "id": id,
                "state": 1
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(cate_state(1144))

    #删除类目
    def cate_delete(self,id):
        url=f'{self.url}/api/v2/agent/category/categoryDelete'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1615966552301",
                "requestId": "123456789012"
            },
            "reqBody": {
                "categoryId": id
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(cate_delete(1142))


if __name__ == '__main__':
    dddd=category(yanshi_customer_url,userId_jierufang01,username01,token_jierufang01)
    dddd.add_category()