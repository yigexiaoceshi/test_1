#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import  requests,json
import random
import time
from  config import *

class new_operation:
    def __init__(self,url,userid,token,username):
        self.url=url
        self.userid=userid
        self.token=token
        self.username=username
    #创建运营账号
    def add_operationuser(self):
        suiji_number=int(round(requestTime / 1000))
        suiji_number01 = int(round(requestTime / 10000))
        loginName = "kobe" + str(suiji_number)
        userName="科比"+str(suiji_number)
        # print(suiji_number01)
        url=f'{self.url}/api/v2/operation/createAccount'
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
                "loginName": loginName,
                "userName":userName,
                "mobile": "13"+str(suiji_number01),
                "telephone": "0571-"+str(suiji_number01),
                "email": "13"+str(suiji_number01)+"@163.com"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json(),loginName,userName
    # print(add_operationuser())


    #获取运营用户名、用户ID、已停用的用户
    # def operation_query(self):
    #     url=f'{yunying_url}/api/v2/Operation/accountList'
    #     header={"Content-Type":"application/json"}
    #     data={
    #         "reqHeader": {
    #             "userId": self.userid,
    #             "userName": self.username,
    #             "token": self.token,
    #             "clientType": "web",
    #             "requestTime": requestTime,
    #             "requestId": "123456789012"
    #         },
    #         "reqBody": {
    #             "pageNumber":2,
    #             "pageSize": 10
    #         }
    #     }
    #     res=requests.post(url,headers=header,data=json.dumps(data))
    #     userid=res.json()["data"]["list"][0]["userId"]
        # number=res.json()["data"]["list"]
        # # print(len(number))
        # list1=[]
        # list2=[]
        # list3=[]
        # list4=[]
        # list5=[]
        # for i in range(len(number)):
        #     # time.sleep(1)
        #     list1.append(res.json()["data"]["list"][i]["loginName"])
        #     list2.append(res.json()["data"]["list"][i]["userId"])
        #     list4.append(res.json()["data"]["list"][i]["userName"])
        #     state = res.json()["data"]["list"][i]["state"]
        #     if state==0:
        #         list3.append(res.json()["data"]["list"][i]["userId"])
        #     else:
        #         list5.append(res.json()["data"]["list"][i]["userId"])
        # loginname=random.choice(list1)
        # userName=random.choice(list4)
        # userid=random.choice(list2)
        # userid_0_state=random.choice(list3)
        # userid_1_state=random.choice(list5)
        # print(type(userid_1_state))
        # return loginname,userName,userid,userid_0_state,userid_1_state

    # print(operation_query()[4])

    #运营列表用户名查询
    def operation_list_chaxun01(self,loginName):
        url=f'{self.url}/api/v2/operation/accountList'
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
                "pageNumber": 1,
                "pageSize": 10,
                "loginName": loginName
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        username = res.json()["data"]["list"][0]["userName"]
        userid = res.json()["data"]["list"][0]["userId"]
        return res.json(),userid,username
    # print(operation_list_chaxun01())

    #运营列表账号负责人查询
    def  operation_list_chaxun02(self,userName):
        url = f'{self.url}/api/v2/operation/accountList'
        header = {"Content-Type": "application/json"}
        data = {
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "userName": userName
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(operation_list_chaxun02())

    #运营列表账号状态查询
    def  operation_list_chaxun03(self):
        url = f'{self.url}/api/v2/operation/accountList'
        header = {"Content-Type": "application/json"}
        data = {
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "state": "0"
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        num=len(res.json()["data"]["list"])
        return res.json(),num
    # print(operation_list_chaxun03())

    #随机获取角色
    def user_role(self):
        url=f'{self.url}/api/v2/operation/privilege/role/getAppRole'
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
            "reqBody": {}
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        role=res.json()["data"]
        list1=[]
        list2=[]
        for i in range(len(role)):
            list1.append(res.json()["data"][i]["roleName"])
            list2.append(res.json()["data"][i]["id"])
        # print(list)
        userrole=random.choice(list1)
        roleId=random.choice(list2)
        return  userrole,roleId
    # print(user_role()[1])

    #授权用户角色
    def shouquan_role(self,userId,roleId):
        url=f'{self.url}/api/v2/operation/privilege/user/authorization'
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
                "userId": userId,
                "roleId": roleId
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(shouquan_role())

    #编辑运营用户
    def edit_user(self,userId):
        xiugai=str(round(requestTime /100000))
        # print(xiugai)
        url=f'{self.url}/api/v2/operation/accountEdit'
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
                "userId":userId,
                "userName": "zcj",
                "mobile": "177"+xiugai,
                "telephone": "0571-"+xiugai,
                "email": "177"+xiugai+"@163.com"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(edit_user())

    #停用运营用户账号
    def out_user(self,userid_1_state):
        url=f'{self.url}/api/v2/operation/accountState'
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
                "userIds": [userid_1_state],
                "state": 0
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(out_user())

    #启用运营用户账号
    def open_user(self,userid_0_state):
        url=f'{self.url}/api/v2/operation/accountState'
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
                "userIds": [userid_0_state],
                "state": 1
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(open_user())

    #运营账号重置密码
    # def user_password:
    #     url=f'{yunying_url}'

for i in range(100):
    if __name__ == '__main__':
        cc=new_operation(yunying_url,userId_yunying,token_yunying,username_yunying).add_operationuser()
        print(cc)

