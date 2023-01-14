#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import json
from config import  *

class device_shenqing:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token
    #视频源申请-列表查询
    def device_shenqing_list(self,deviceCode):
        url=f'{self.url}/api/v2/agent/deviceApply/search'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "deviceCode": deviceCode,
                "sourceCode": None,
                "size": 20,
                "page": 1,
                "ascCreateTime": False
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610950637444",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(device_shenqing_list(10000000322))

    #视频源申请-详情-基本信息
    def device_shenqing_xiangqing(self,id):
        url = f'{self.url}/api/v2/agent/deviceApply/baseInfo'
        header = {"Content-Type": "application/json;charset=UTF-8"}
        data = {
            "reqBody": {
                "id": id
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610936813395",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(device_shenqing_xiangqing(111))

    #视频源申请-详情-推流记录
    def device_shenqing_tuiliu(self,id=None):
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
    # print(device_shenqing_tuiliu(111))

    #视频源申请-上传附件
    def device_file(self):
        url=f'{self.url}/api/v2/netdisk/upload'
        files={
            "bizType":(None,9),
            "file":("111",open("/Users/apple/Desktop/111.pdf","rb"),"application/pdf")
        }
        res=requests.post(url=url,files=files).json()
        fileKey=res["data"]["fileKey"]
        return res,fileKey
    # print(device_file())

    #视频源申请-提交申请
    def device_tijiaoshenqing(self,filePath,deviceCode=None):
        url=f'{self.url}/api/v2/agent/asyncApplyAuth'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "contact": "申请一",
                "phone": "17757565002",
                "fileName": "111.pdf",
                "remark": "接口自动化测试",
                "applyType": 9,
                "approveBy": 0,
                "resourceCodeList": [deviceCode],
                "filePath": filePath
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1610953511853",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(device_tijiaoshenqing(10000000322))

# if __name__ == '__main__':
#     device_shenqing(XXX_customer_url,userId_jierufang02,username02,token_jierufang02).device_tijiaoshenqing("cdd10511b6872658b759da7512782d8bd0e2974380f8fa69e7ee86b73b4f7e66",10000000408)