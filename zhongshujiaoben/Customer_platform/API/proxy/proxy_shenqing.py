#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-

import requests,json
from config import  *
from faker import Factory

fake=Factory.create("zh_CN")


class Shenqing_proxy:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token
    #服务申请-文件上传(方式一)
    def proxy_file(self):
        url=f'{self.url}/api/v2/netdisk/upload'
        file={"bizType":(None,3),
              "file":("111.pdf",open('/Users/apple/Desktop/111.pdf', 'rb'),"application/pdf")}
        res=requests.post(url,files=file).json()
        filePath=res["data"]["fileKey"]
        fileName=res["data"]["fileName"]
        return res,filePath,fileName
    # print(proxy_file())

    # def proxy_file02():
    #     url=f'{test_customer_url}/api/v2/netdisk/upload'
    #     file_data={"bizType":3}
    #     file={"file":("111.pdf",open('/Users/apple/Desktop/111.pdf', 'rb'),"application/pdf")}
    #     res=requests.post(url,data=file_data,files=file).json()
    #     return res
    # print(proxy_file02())

    #服务申请-提交
    def proxy_tijiao(self,zsCode,fileName,filePath):
        url=f'{self.url}/api/v2/agent/asyncApplyAuth'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "resourceCodeList": [zsCode],
                "fileName": fileName,
                "filePath": filePath,
                "applyType": 10,
                "contact": "申请一",
                "phone": "17757565001",
                "remark": "测试"
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1615353277270",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        return res
    # print(proxy_tijiao(1407374889844765,"111.pdf","file://yunyang-zs/private/datatable/prod/1615347224972/111.pdf"))

# if __name__ == '__main__':
    # print(Shenqing_proxy(yanshi_customer_url,757,"周一","mockToken").proxy_file())
    # print(Shenqing_proxy(yanshi_customer_url,757,"周一","mockToken").url)