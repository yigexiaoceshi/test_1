#!/usr/local/bin python3.8
# -*- coding: utf-8 -*-
import base64
import requests,json
from config import *

def list_quanbuAPI(i):
    url = f'{test_customer_url}/api/v2/agent/apiMarket'
    header = {'Content-Type': 'application/json'}
    data = {
        "reqHeader": {
            "userId": 685,
            "userName": "测试",
            "token": "mockToken",
            "mainUser": 1,
            "clientType": "web",
            "requestTime": "1626769872859",
            "requestId": "123456789012"
        },
        "reqBody": {
            "page": 1,
            "size": 10,
            "appShortName":"工程院专班"
        }
    }
    res = requests.post(url, headers=header, data=json.dumps(data))
    code=res.json()["data"]["records"][i]["apiCode"]
    return code

def file():
    url=f'{test_customer_url}/api/v2/netdisk/upload'
    # request_file = {'pdf': (('接口PDF', open('/Users/apple/Desktop/111.pdf')), 'image/jpeg')}
    file_data = {"bizType": (None, 1),
                 'file': ("111.pdf", open('/Users/apple/Downloads/111.pdf', 'rb'), 'application/pdf')}#"rb"二进制格式读文件
    res=requests.post(url,files=file_data).json()
    file_key=res["data"]["fileKey"]
    return file_key
    # print(file())

#提交申请
def shenqing(apiCode,filePath):
    url=f'{test_customer_url}/api/v2/agent/asyncApplyAuth'
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
        "reqHeader": {
            "userId": 685,
            "userName": "测试",
            "token": "mockToken",
            "mainUser": 1,
            "clientType": "web",
            "requestTime": "1626770354881",
            "requestId": "123456789012"
        },
        "reqBody": {
            "contact": "申请一",
            "phone": "17757565002",
            "fileName": "111.pdf",
            "remark": "测试",
            "applyType": 1,
            "approveBy": 0,
            "resourceCodeList": [apiCode],
            "filePath": filePath,
            "applyBillCode": "",
            "indicatorAreaAuthList": [{
                "resourceCode": apiCode,
                "dimensionValueCodes": [1000855]
            }]
        }
    }
    res=requests.post(url,headers=header,data=json.dumps(data))
    return res.json()
# print(bucket_shenqing())

if __name__ == '__main__':
    list=[]
    for i in range(3):
        code=list_quanbuAPI(i)
        list.append(code)
    print(list)

    for code in list:
        path=file()
        print(path)
        jm_path=str(base64.b64encode(path.encode("utf-8")),"utf-8")
        ow_paht=jm_path[:-1]
        print(ow_paht)
        print(code)
        print(shenqing(int(code),str(jm_path)))
        # 同用户五秒后才能提交
        # time.sleep(1)

