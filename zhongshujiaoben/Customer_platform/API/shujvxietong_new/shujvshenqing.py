#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import *
from faker import Factory
fake=Factory.create("zh_CN")

#数据申请-详情
def data_shenqing():
    url=f'{test_customer_url}/api/v4/dc/metaData/tableDetail?'
    header={"userId":"41"}
    data={"id":6}
    res=requests.post(url,headers=header,data=data).json()
    return res
# print(data_shenqing())

#数据申请-上传附件
def data_file():
    url=f'{test_customer_url}/api/v2/netdisk/upload'
    # header = {"Content-Type": "multipart/form-data"}
    file_data={"bizType":(None,3),
          "file":("111.pdf",open("/Users/apple/Desktop/111.pdf","rb"),'application/pdf')}  #"rb"二进制格式读文件
    res=requests.post(url,files=file_data).json()
    filePath=res["data"]["fileKey"]
    fileName=res["data"]["fileName"]
    return res,filePath,fileName
# print(data_file())

#数据申请-提交
def data_tijiao(resourceCode,fileName,filePath):
    url=f'{test_customer_url}/api/v4/dc/dataAuth/volumeAuth'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"41"}
    data={
        "resourceCodeList": [resourceCode],
        "fileName": fileName,
        "filePath": filePath,
        "contact": "申请一",
        "phone": "17757565002",
        "remark": "接口测试数据，PDF不可看",
        "indicatorAreaAuthList": [{
            "resourceCode": resourceCode,
            "dimensionValueCodes": []
        }]
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
print(data_tijiao("20201221195754595","fileName","file://yunyang-zs/private/datatable/prod/1614735487149/111.pdf"))

