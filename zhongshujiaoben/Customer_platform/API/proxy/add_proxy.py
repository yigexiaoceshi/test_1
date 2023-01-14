#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import  *
from faker import   Factory
fake=Factory.create("zh_CN")

newtime = effectiveTime

class Add_proxy:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token

    #创建代理服务
    def add_newproxy(self):
        appcode="zcj"+fake.ean8()
        name=fake.name()+"的代理服务"
        data_url="http://"+fake.ipv4(network=False)
        healthPath="/"+fake.uri_path(deep=None)
        url=f'{self.url}/api/v2/agent/proxyServer/create/create'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody": {
                "appCode": appcode,
                "name":name,
                "url":data_url ,
                "healthPath":healthPath ,
                "accessPermission": "2",
                "remark": "测试数据   "+newtime
            },
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1615342263177",
                "token": self.token,
                "userId": self.userid,
                "userName": self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        print("单个新注册的数据，正在入链中，需要等待")
        # days = 365
        # for i in range(days):
        #     print("\r进度条百分比：{}%".format(round((i + 1) * 100 / days)), end="", flush=True)
        #     time.sleep(0.04)
        #     if i==364:
        #         break
        return res,appcode
    # print(Add_newproxy())

# if __name__ == '__main__':
#     print(Add_proxy(yanshi_customer_url,757,"周一","mockToken").add_newproxy())