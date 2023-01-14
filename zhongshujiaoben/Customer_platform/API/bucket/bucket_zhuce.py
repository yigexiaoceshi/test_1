#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import json
import time
import requests
from config import *
from faker import Factory
fake=Factory.create("zh_CN")


class bucket_zc:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token
    #bucket注册
    def bucket_chuanjian(self):
        # aaa = int(time.time())
        # timeArray = time.localtime(aaa)
        # effectiveTime = time.strftime("%Y_%m_%d%H_%M_%S", timeArray)
        bucket_name=fake.name()
        url=f'{self.url}/api/v2/agent/fc/customer/create/bucket'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqHeader":{
                "userId":self.userid,
                "userName":self.username,
                "token":self.token,
                "clientType":"web",
                "requestTime":"1610429300921",
                "requestId":"123456789012"
            },
            "reqBody":{
                "bucketName":bucket_name,
                "bucketSpace":10737418240,
                "maxFileSize":fake.ean(length=8),
                "openRead":"2",
                "description":"测试",
                "categoryCode":"5"
            }
        }

        res=requests.post(url,headers=header,data=json.dumps(data))
        bucketcode=res.json()["data"]
        return res.json(),bucketcode,bucket_name
    # print(bucket_chuanjian())

# if __name__ == '__main__':
    # print(bucket_zc(XXX_customer_url,userId_jierufang01,username01,token_jierufang01).bucket_chuanjian())





