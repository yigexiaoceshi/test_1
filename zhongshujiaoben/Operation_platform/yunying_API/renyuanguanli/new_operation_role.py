# !/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
import random
from  time import sleep,time
from  config import *


class new_role:
    def __init__(self,url,userid,token,username):
        self.url=url
        self.userid=userid
        self.token=token
        self.username=username

    #新增角色
    def add_role(self):
        roleName= "测试脚本"+str(a)
        url=f'{self.url}/api/v2/operation/privilege/role/create'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "roleName": roleName,
                "purviewIds":operation_quanxiandian
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json(),roleName
    # print(add_role())

    #获取角色ID和角色名称
    def see_role(self,roleName):
        #随机获取角色ID
        url=f'{self.url}/api/v2/operation/privilege/role/search'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "page": 1,
                "roleName":roleName,
                "size": 10
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        id=res.json()["data"]["items"][0]["id"]
        name=res.json()["data"]["items"][0]["roleName"]
        return id,name

    #查看角色详情
    def obtain(self,id):
        url=f'{self.url}/api/v2/operation/privilege/role/purview'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "id": id
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(see_role())

    #删除角色
    def delete_role(self,id):
        url=f'{self.url}/api/v2/operation/privilege/role/delRole'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "roleId": id
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(delete_role())

    #编辑角色
    def edit_role(self,roleName,id):
        #编辑角色
        url01=f'{self.url}/api/v2/operation/privilege/role/edit'
        header01={"Content-Type":"application/json"}
        data01={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "roleName": roleName,
                "purviewIds": operation_quanxiandian,
                "id": id
            }
        }
        res=requests.post(url01,headers=header01,data=json.dumps(data01))
        return res.json()
    # print(edit_role())

    #搜索栏查询验证
    def query_yanzheng(self,roleName):
        #角色名称查询
        url=f'{self.url}/api/v2/operation/privilege/role/search'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "page": 1,
                "size": 10,
                "roleName": roleName
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()

    def query_yanzheng01(self,):
        #角色类型查询
        url=f'{self.url}/api/v2/operation/privilege/role/search'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "page": 1,
                "size": 10,
                "areDefault": "0"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(query_yanzheng())

if __name__ == '__main__':
    aa=new_role(yunying_url,userId_yunying,token_yunying,username_yunying).add_role()[1]
    bb=new_role(yunying_url,userId_yunying,token_yunying,username_yunying).see_role(aa)
    print(bb)

