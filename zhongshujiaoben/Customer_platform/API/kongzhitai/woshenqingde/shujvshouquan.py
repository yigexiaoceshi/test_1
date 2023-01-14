#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import json
import random
from config import  *



class shujv():
    def __init__(self,url,userid,token):
        self.url=url
        self.userid=userid
        self.token=token

    #随机获取申请单号
    def huoqudanhao(self):
        url=f'{self.url}/api/v2/agent/customerIndicatorList'
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
                "pageNumber": 1,
                "pageSize": 10,
                "sourceApiCode": None,
                "apiDesc": None,
                "targetAppName": "",
                "applyBillCode": "",
                "applyType": 3
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        total=res.json()["data"]["total"]
        list1=[]
        for i in range(int(total)):
            list1.append(res.json()["data"]["list"][i]["applyBillCode"])
            # print(res.json()["data"]["list"][i]["applyBillCode"])
        num=random.choice(list1)
        return  num

    #单号查询
    def shujvdanhaochaxun(self,applyBillCode=None):
        url=f'{self.url}/api/v2/agent/customerIndicatorList'
        header = {"Content-Type": "application/json"}
        data = {
            "reqHeader": {
                "userId": self.userid,
                "userName": username,
                "token": self.token,
                "clientType": "web",
                "requestTime": requestTime,
                "requestId": "123456789012"
            },
            "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "sourceApiCode": None,
                "apiDesc": None,
                "targetAppName": "",
                "applyBillCode": applyBillCode,
                "applyType": 3
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()

    # print(shujvdanhaochaxun())

    #查看详情
    def seexiangqing(self,applyBillCode=None):
        url=f'{self.url}/api/v2/data/apply/detail'
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
        accessory=res.json()["data"]["attachment"]
        return  res.json(),accessory

    # print(seexiangqing())

    #查看附件
    def seefujian(self,accessory=None):
        url=f'{self.url}'+str(accessory)
        res=requests.get(url)
        return res.status_code


if __name__ == '__main__':
    aa=shujv(jierufang_url,userId_jierufang01,token_jierufang).huoqudanhao()
    print(type(a))