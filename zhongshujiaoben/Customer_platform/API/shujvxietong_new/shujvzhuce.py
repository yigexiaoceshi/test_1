#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import  *
from faker import Factory
fake=Factory.create("zh_CN")

#数据注册
def data_zhuce():
    url=f'{test_customer_url}/api/v4/dc/metaData/dataRegistration'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"41"}
    data={
        "dataCode": "test_"+fake.language_code(),
        "dataName": "数据协同接口测试"+str(fake.pyint()),
        "securityLevel": 2,
        "syncSecurityLevel": 2,
        "dataDesc": "测试",
        "categoryCodes": [],
        "properties": [{
            "key": 3,
            "propCode": "name",
            "propName": "用户名",
            "propDataType": "string",
            "maxLength": 256,
            "isIndexKey": 0,
            "isNotNull": 0,
            "maxNum": 256,
            "isPrimaryKey": 0,
            "isArea": 0,
            "isSubTable": 0,
            "isSubLib": 0
        }, {
            "key": 4,
            "propCode": "id",
            "propName": "编号",
            "propDataType": "integer",
            "isIndexKey": 0,
            "isNotNull": 0,
            "isPrimaryKey": 0,
            "isArea": 0,
            "isSubTable": 0,
            "isSubLib": 0
        }]
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    code=res["data"]
    return  res,code
print(data_zhuce())