#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import json
import  time

class my_device:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid= userid
        self.username=username
        self.token=token

    #我的视频源-列表接口
    def device_list(self,deviceCode=None):
        url=f'{self.url}/api/v2/agent/myDevice/registeredList'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "deviceCode": deviceCode,
                "size": 20,
                "page": 1,
                "ascCreateTime": False
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610935801628",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        devicecode=res["data"]["list"][0]["deviceCode"]
        return  res,devicecode
    # print(device_list(10000000331))

    #我的视频源详情-基本信息
    def device_xiangqing_jibenxinxi(self,id=None):
        url=f'{self.url}/api/v2/agent/deviceApply/baseInfo'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610936813395",
                "token": self.token,
                "userId": self.userid,
                "userName":self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(device_xiangqing_jibenxinxi(122))

    #我的视频源详情-推流记录
    def device_xiangqing_tuiliu(self,id=None):
        url=f'{self.url}/api/v2/agent/deviceApply/pushStreamInfo'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "size": 20,
                "page": 1,
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610937078610",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(device_xiangqing_tuiliu(122))

    #我的视频源详情-授权记录
    def device_xiangqing_shouquan(self,id=None):
        url=f'{self.url}/api/v2/agent/deviceApply/authorizationRecord'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "size": 20,
                "page": 1,
                "ascPassTime": True,
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610938036149",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(device_xiangqing_shouquan(122))

    #我的视频源详情-区块信息
    def device_xiangqing_qukuai(self,sourceId):
        # print("区块链入链需等待十五秒...")
        # time.sleep(20)
        url=f'{self.url}/api/v2/blockchain/current'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "sourceId": sourceId,
                "type": 9
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610938292422",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        txId=res["data"]["txId"]
        return  res,txId
    # print(device_xiangqing_qukuai(10000000331)[1])

    #我的视频源详情-区块详情
    def device_xiangqing_qukuaixiangqing(self,txId=None):
        url=f'{self.url}/api/v2/blockchain/fetch/bizData2BC'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "txId": txId
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610938548190",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(device_xiangqing_qukuaixiangqing())

    #我的视频源-编辑
    def device_upadte(self,deviceCode,id):
        bbb = int(time.time())
        timeArray = time.localtime(bbb)
        effectiveTime = time.strftime("%Y_%m_%d%H_%M_%S", timeArray)
        effectiveTime01 = time.strftime("%H_%M_%S", timeArray)
        url=f'{self.url}/api/v2/agent/myDevice/update'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "deviceCode": deviceCode,
                "sourceCode": "最新test"+effectiveTime,
                "name": "最新视频源接口"+effectiveTime01,
                "typeId": 11,
                "type": "VIDEO",
                "pushStreamProtocol": "RTMP",
                "openRead": "2",
                "remark": "接口自动化测试",
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610949181374",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(device_upadte(10000000334,123))


# if __name__ == '__main__':
#     print(my_device(test_customer_url,45,"周一","mockToken").device_xiangqing_qukuai(10000000416))