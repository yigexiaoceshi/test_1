#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
from Customer_platform.API.bucket.bucket_zhuce import bucket_zc
from config import  *
import json
import time

class my_bucket:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token
    #列表code查询
    def bucket_list_code(self,bucketCode):
        url=f'{self.url}/api/v2/agent/fc/customer/search/myBucket'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610516799389",
                "requestId":"123456789012"
            },
            "reqBody":{
                "page":1,
                "size":10,
                "bucketCode": bucketCode

            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        # bucketcode=res.json()["data"]["buckets"][0]['bucketCode']
        return res.json()
    # print(bucket_list_code())

    #列表name查询
    def bucket_list_name(self, bucketName):
        url=f'{self.url}/api/v2/agent/fc/customer/search/myBucket'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610516799389",
                "requestId":"123456789012"
            },
            "reqBody":{
                "page":1,
                "size":10,
                "bucketName": bucketName

            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(bucket_list_name())

    #bucket-编辑
    def bucket_edit(self,bucketCode,id):
        aaa = int(time.time())
        timeArray = time.localtime(aaa)
        effectiveTime = time.strftime("%Y_%m_%d%H_%M_%S", timeArray)
        url=f'{self.url}/api/v2/agent/fc/customer/edit/bucket'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610519810502",
                "requestId":"123456789012"
            },
            "reqBody":{
                "bucketName":"jiekou_edit"+str(effectiveTime),
                "bucketSpace":10737418240,
                "maxFileSize":2097152,
                "openRead":"2",
                "description":"测试",
                "categoryCode":"5",
                "bucketCode":bucketCode,
                "id":id
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()
    # print(bucket_edit())

    #查看bucket详情-基本信息
    def bucket_xiangqing(self,bucketCode):
        url=f'{self.url}/api/v2/agent/fc/customer/bucket/base'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610429941399",
                "requestId":"123456789012"
            },
            "reqBody":bucketCode
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(bucket_xiangqing())

    #查看bucket详情-文件信息
    def bucket_xiangqing_file(self,bucketCode):
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
        # fileCode=res.json()["data"]["files"][0]["fileCode"]
        return res.json()
    # print(bucket_xiangqing_file())

    #我的bucket-详情-文件信息-上传文件
    def upload_file(self,bucketCode):
        url=f'{self.url}/api/v2/agent/fc/customer/file/create'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610430758829",
                "requestId":"123456789012"
            },
            "reqBody":{
                "fileKey":"file://yunyang-zs/private/file/prod/1610430744049/111.pdf",
                "fileSize":80000,
                "filePath":"1111",
                "description":"接口测试",
                "fileName":"111",
                "bucketCode":bucketCode,
                "fileExtendName":"pdf"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        fileCode=res["data"]
        return res,fileCode
    # print(upload_file())

    #文件信息-点击预览接口
    def bucket_preview(self,fileCode):
        url=f'{self.url}/api/v2/agent/fc/customer/url/batchSign'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
        "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610431579450",
                "requestId":"123456789012"
            },
            "reqBody":{
                "fileCode":[
                    fileCode
                ],
                "urlType":"file"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(bucket_preview())

    #修改文件信息-重命名
    def bucket_file_rename(self,fileCode):
        url=f'{self.url}/api/v2/agent/fc/customer/file/rename'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610515862549",
                "requestId":"123456789012"
            },
            "reqBody":{
                "fileCode":fileCode,
                "fileName":"接口测试111"
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(bucket_file_rename())

    #文件信息-删除
    def bucket_file_delete(self,fileCode):
        url=f'{self.url}/api/v2/agent/fc/customer/file/delete/list'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
        "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610518144940",
                "requestId":"123456789012"
            },
            "reqBody":{
                "fileCodes":[
                    fileCode
                ]
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(bucket_file_delete())

#
