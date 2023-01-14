#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import *
from faker import  Factory

fake=Factory.create("zh_CN")

#新增lot设备
def new_equipment(productId,productName):
    url=f'{yanshi_customer_url}/api/v2/agent/device/add'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "clientType": "web",
            "requestId": "123456789012",
            "requestTime": "1615893000455",
            "token": "mockToken",
            "userId": 757,
            "userName": "周一"
        },
        "reqBody": {
            "productId": productId,
            "productName": productName,
            "code": fake.ean8(),
            "name": fake.name()+"的设备",
            "ip": fake.ipv4(network=False),
            "serverName": "接口脚本服务器",
            "remark": "接口脚本数据"
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
print(new_equipment(24,"编辑后崔金凤手机"))