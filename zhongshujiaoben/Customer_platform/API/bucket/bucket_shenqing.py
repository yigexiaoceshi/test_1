#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
from config import  *
import json
import time

class buckek_shenqing:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token
    #bucket申请列表查询
    def bucket_shenqing_list(self,bucketCode):
        url=f'{self.url}/api/v2/agent/fc/customer/search/bucket'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610527305925",
                "requestId":"123456789012"
            },
            "reqBody":{
                "bucketCode": bucketCode,
                "page":1,
                "size":10
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        # bucketcode=res.json()["data"]["buckets"][2]["bucketCode"]
        return res.json()
    # print(bucket_shenqing_list())

    #bucket申请详情-基本信息
    def bucket_shenqing_xiangqing(self,bucketCode):
        url=f'{self.url}/api/v2/agent/fc/customer/bucket/base'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610527632637",
                "requestId":"123456789012"
            },
            "reqBody":bucketCode
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(bucket_shenqing_xiangqing())


    #bucket申请详情-文件信息
    def bucket_shenqing_xiangqing_file(self,bucketCode):
        url=f'{self.url}/api/v2/agent/fc/customer/search/file'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610430239622",
                "requestId":"123456789012"
            },
            "reqBody":{
                "page":1,
                "size":10,
                "conds":{
                    "bucketCode":bucketCode,
                    "bucketCodeCmp":"="
                },
                "sort":{
                    "ascModifyTime":True
                }
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(bucket_shenqing_xiangqing_file())

    #bucket上传附件
    def bucket_file(self):
        url=f'{self.url}/api/v2/netdisk/upload'
        # request_file = {'pdf': (('接口PDF', open('/Users/apple/Desktop/111.pdf')), 'image/jpeg')}
        file_data = {"bizType": (None, 8),
                     'file': ("111.pdf", open('/Users/apple/Desktop/111.pdf', 'rb'), 'application/pdf')}#"rb"二进制格式读文件
        res=requests.post(url,files=file_data).json()
        file_key=res["data"]["fileKey"]
        return res,file_key
    # print(bucket_file())

    #bucket提交申请
    def bucket_shenqing(self,bucketCode,file_key):
        url=f'{self.url}/api/v2/agent/asyncApplyAuth'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader": {
                "userId": self.userid,
                "userName": self.username,
                "token": self.token,
                "clientType": "web",
                "requestTime": "1611056934862",
                "requestId": "123456789012"
            },
            "reqBody": {
                "resourceCodeList": [bucketCode],
                "fileName": "111.pdf",
                "filePath":file_key,
                "applyType": 8,
                "contact": "测试一",
                "phone": "17757565001",
                "remark": "cs"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(bucket_shenqing())


# if __name__ == '__main__':
# #     print(buckek_shenqing(XXX_customer_url,userId_jierufang02,username02,token_jierufang02).bucket_shenqing("44040212","file://yunyang-zs/private/file/prod/1611056931524/111.pdf"))
#     print(buckek_shenqing(XXX_customer_url,userId_jierufang02,username02,token_jierufang02).bucket_file())
#
