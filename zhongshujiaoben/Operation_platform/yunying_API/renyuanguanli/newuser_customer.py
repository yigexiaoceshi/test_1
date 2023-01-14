#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-

import requests,json
from config import *
from faker import Factory
fake=Factory.create("zh_CN")
fake01=Factory.create("en_US")
import random

#接入方类型:AREA（区县平台）、DEPT（部门）、PUB_SERV（公共服务商）、TEOR（第三方质检机构)
leixing=["AREA","DEPT","PUB_SERV","TEOR"]



class new_customer:
    def __init__(self,url,userid,token,username):
        self.url=url
        self.userid=userid
        self.token=token
        self.username=username

    #获取区县接口
    def quxian(self):
        url = f'{self.url}/api/v2/operation/customerTypeList'
        header={'Content-Type': 'application/json'}
        data={
                "reqHeader": {
                    "userId": self.userid,
                    "userName": self.username,
                    "token": self.token,
                    "clientType": "web",
                    "requestTime": "1617786617527",
                    "requestId": "123456789012"
                },
                "reqBody": {}
            }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        code=res["data"]["areaInfos"][random.randint(0,10)]['areaCode']
        return res,code

    #创建接入方账号
    def add_jierufang(self,appType,appTypeCode=None):
        appShortName = fake.company()
        email=fake.free_email()
        url = f'{self.url}/api/v2/operation/createCustomer'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId": self.userid,
                "token": self.token,
              },
              "reqBody": {
                "loginName": "aa"+fake01.name(),
                "appName": appShortName+"浙江全称",
                "appShortName":"浙江"+appShortName,
                "userName": "测试人员",
                "mobile": fake.phone_number(),
                "email": email,
                "telephone": "0571-8446466",
                "techName": f"测试{requestTime}",
                "techMobile": fake.phone_number(),
                "techEmail":email,
                "appType": appType, #'接入方类型:AREA（区县平台）、DEPT（部门）、PUB_SERV（公共服务商）、TEOR（第三方质检机构）'
                "appTypeCode": appTypeCode
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),appShortName
    # print(add_jierufang())

    #运营用户详情接口验证
    def user_info(self):
        url=f'{self.url}/api/v2/operation/central/interconnected/zs/info'
        header={'Content-Type':'application/json'}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": "超级管理员",
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {}
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(user_info())

    #获取接入方简称
    # def customer_name(self):
    #     url=f'{self.url}/api/v2/Operation/customerList'
    #     header = {'Content-Type': 'application/json'}
    #     data = {
    #     "reqHeader": {
    #         "userId": self.userid,
    #         "userName": self.username,
    #         "token": self.token,
    #         "clientType": "web",
    #         "requestTime": requestTime,
    #         "requestId": "123456789012"
    #     },
    #     "reqBody": {
    #         "appShortName": "",
    #         "state": "",
    #         "appType": "",
    #         "size": 10,
    #         "page": 1
    #     }
    # }
    #     res = requests.post(url, headers=header, data=json.dumps(data))
    #     customer_name=res.json()['data']['records']
    #     appInfoId=res.json['data']['records'][0]['appInfoId']
    #     list1=[]
    #     list2=[]
    #     list3=[]
    #     for i in range(len(customer_name)):
    #         list1.append(res.json()['data']['records'][i]['appShortName'])
    #         state=res.json()['data']['records'][i]['state']
    #         if state==1:
    #             nn = res.json()['data']['records'][i]['userId']
    #             list2.append(nn)
    #
    #     appShortName=random.choice(list1)
    #     userId=random.choice(list2)
    #
    #     return appShortName,userId,appInfoId
    # print(customer_name()[1])

    #接入方列表简称查询
    def user_chaxun(self,appShortName):
        url=f'{self.url}/api/v2/operation/customerList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId": self.userid,
                "token": self.token,
              },
              "reqBody": {
                "loginName": self.username,
                "appName": f"接入方{requestTime}",
                "appShortName":appShortName,
                "userName": f"测试{requestTime}",
                "mobile": "177000000001",
                "telephone": "0571-8446466",
                "techName": f"测试{requestTime}",
                "techMobile": "17700000001",
                "techEmail": "17700000001@163.com",
                "appType": "DEPT"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        userid = res.json()['data']['records'][0]['userId']
        appInfoId=res.json()['data']['records'][0]['appInfoId']
        # print(list)
        return userid,appInfoId,res.json()
    # print(user_chaxun())

    #接入方用户编辑
    def user_detail(self,appInfoId,userId):
        mobile_customer=str(13)+str(round(requestTime / 10000))
        print(mobile_customer)
        url=f'{self.url}/api/v2/operation/editCustomer'
        header={'Content-Type':"application/json"}
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
                "userName": '测试'+str(a),
                "mobile": str(mobile_customer),
                "telephone": "0571-8446466",
                "techName": '测试'+str(a),
                "techMobile": str(mobile_customer),
                "techEmail": "177000000016@163.com",
                "appInfoId": appInfoId,
                "userId": userId
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(user_detail())

    # 接入方用户停用
    def user_out(self, userId):
        url = f'{self.url}/api/v2/operation/customerState'
        header = {'Content-Type': 'application/json'}
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
                "state": 0,
                "id": userId
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(user_out())

    #接入方用户启动
    def user_open(self,userId):
        url=f'{self.url}/api/v2/operation/customerState'
        header={'Content-Type':'application/json'}
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
                "state": 1,
                "id": userId
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(user_open())

# for i in range(600):
#     if __name__ == '__main__':
#         leixing_type=random.choice(leixing)
#         xx = new_customer(yunying_url,userId_yunying,token_yunying,username_yunying)
#         if  leixing_type in 'AREA':
#             code=xx.quxian()[1]
#             aa=xx.add_jierufang(leixing_type,code)
#             type=aa[1]
#             res=aa[0]
#             print(leixing_type)
#             print(type)
#             print(res)
#             print("----------")
#         else:
#             bb=xx.add_jierufang(leixing_type)
#             type=bb[1]
#             res=bb[0]
#             print(leixing_type)
#             print(type)
#             print(res)
#             print("----------")
