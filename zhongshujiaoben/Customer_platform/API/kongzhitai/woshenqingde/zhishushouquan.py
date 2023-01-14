#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import  requests
import  json
import random
from config import *


class zhishu:
    def __init__(self,url,userld,token):
        self.url=url
        self.userld=userld
        self.token=token

#指数授权-获取申请单号
    def huoqudanhao(self):
        url=f'{self.url}/api/v2/agent/customerIndicatorList'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userld,
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
                "applyType": 2
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        s = res.json()["data"]["list"]
        dd = res.json()["data"]["total"]
        list = []
        for i in range(dd):
            list.append(s[i]["applyBillCode"])
        num=(random.choice(list))
        return  num
    # print(huoqudanhao())


    #单号查询
    def zhishuchaxun(self,applyBillCode=None):
        url = f'{self.url}/api/v2/agent/customerIndicatorList'
        header = {"Content-Type": "application/json"}
        data = {
            "reqHeader": {
                "userId": self.userld,
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
                "applyType": 2
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(zhishuchaxun(huoqudanhao()))


    #查看详情
    def chakanxiangqing(self,applyBillCode=None):
        url=f'{self.url}/api/v2/agent/custIndiAuthBillDetail'
        header={"Content-Type":"application/json"}
        data={
            "reqHeader": {
                "userId": self.userld,
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
        accessory= res.json()["data"]["applyBillDetail"]["filePath"]
        return  res.json(),accessory
    # print(chakanxiangqing())

    #查看附件
    # a = chakanxiangqing().split('9999')
    # print(a)
    def chakanfujian(self,accessory):
        url=f'{self.url}'+str(accessory)
        res=requests.get(url)
        return  res.status_code
    # print(chakanfujian())
