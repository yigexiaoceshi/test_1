#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import random
import json
from config import *
import pymysql


class topic:
    def __init__(self,url,userid,token):
        self.url=url
        self.userid=userid
        self.token=token
    #topic_随机获取单号
    def topichuoqu(self):
        url=f'{self.url}/api/v2/topic/apply/list'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "page": 1,
                "size": 10,
                "appName": "",
                "applyBillCode": "",
                "topicCode": ""
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        title=res.json()["data"]["totalCount"]
        suijiquzhi=res.json()["data"]["records"]
        list=[]
        for i in range(title):
            list.append(suijiquzhi[i]["applyBillCode"])

        num=(random.choice(list))
        return  num
    # print(topicchaxun())

    #单号查询
    def danhaochaxun(self,applyBillCode=None):
        url=f'{self.url}/api/v2/topic/apply/list'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "page": 1,
                "size": 10,
                "appName": "",
                "applyBillCode": applyBillCode,
                "topicCode": ""
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(danhaochaxun(topicchaxun()))

    #查看审批详情
    def seexiangqing(self,applyBillCode):
        url=f'{self.url}/api/v2/topic/apply/detail'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "applyBillCode": applyBillCode
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        topic_code=res.json()["data"]["resourceList"][0]["topicCode"]
        filePath=res.json()["data"]["filePath"]
        return  topic_code,filePath,res.json()

    # print(seexiangqing())

    #查看topic详情
    def topic_xiangqing(self,topicCode):
        url=f'{self.url}/api/v2/topic/detail'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":username,
                "token":self.token,
                "clientType":"web",
                "requestTime":requestTime,
                "requestId":"123456789012"
            },
            "reqBody":{
                "topicCode":topicCode
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()

    # print(topic_xiangqing())

    #查看附件
    def seefujian(self,fujian):
        url=f'{kaifa_jierufang_url}'+str(fujian)
        res=requests.get(url)
        return res.status_code
    # print(seefujian())