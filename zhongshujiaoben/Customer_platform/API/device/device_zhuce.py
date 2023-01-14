#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import  requests
import json
from config import  *
import time

class device_zhuce:
    def __init__(self,url,userid,username,token):
        self.url=url
        self.userid=userid
        self.username=username
        self.token=token

    #视频源注册-单一注册
    def device_zhucee(self):
        aaa = int(time.time())
        timeArray = time.localtime(aaa)
        effectiveTime = time.strftime("%Y_%m_%d%H_%M_%S", timeArray)
        effectiveTime01 = time.strftime("%H_%M_%S", timeArray)
        sourceCode="api"+effectiveTime
        name="视频源接口测试一"+effectiveTime01
        url=f'{self.url}/api/v2/agent/deviceCreate/singleCreate'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
            "reqBody":{
                "sourceCode":sourceCode,
                "name":name,
                "typeId":11,
                "type":"VIDEO",
                "pushStreamProtocol":"RTMP",
                "openRead":"2",
                "remark":"测试"
            },
            "reqHeader":{
                "clientType":"web",
                "requestId":"123456789012",
                "requestTime":"1610620450163",
                "token":self.token,
                "userId":self.userid,
                "userName":self.username
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        print("单个新注册的数据，正在入链中，需要等待")
        days = 365
        for i in range(days):
            print("\r进度条百分比：{}%".format(round((i + 1) * 100 / days)), end="", flush=True)
            time.sleep(0.06)
        deviceCode=res["data"]["deviceCode"]
        id=res["data"]["id"]
        return res,deviceCode,id,sourceCode,name

    # 视频源注册-批量注册
    def device_piliang_zhuce(self):
        a = int(time.time())
        url=f'{self.url}/api/v2/agent/deviceCreate/multiCreate'
        header={"Content-Type":"application/json;charset=UTF-8"}
        data={
        "reqBody": {
            "list": [{
                "sourceCode": a+1,
                "name": "api"+str(a+1),
                "type": "视频流",
                "openRead": "授权拉流权限",
                "remark": "测试",
                "typeId": 10,
                "typeStr": "车辆定位器"
            }, {
                "sourceCode": a+2,
                "name": "api"+str(a+2),
                "type": "视频流",
                "openRead": "授权拉流权限",
                "remark": "测试",
                "typeId": 10,
                "typeStr": "车辆定位器"
            }, {
                "sourceCode": a+3,
                "name": "api"+str(a+3),
                "type": "视频流",
                "openRead": "授权拉流权限",
                "remark": "测试",
                "typeId": 10,
                "typeStr": "车辆定位器"
            }]
        },
        "reqHeader": {
            "clientType": "web",
            "requestId": "123456789012",
            "requestTime": "1611024668816",
            "token": self.token,
            "userId": self.userid,
            "userName": self.username
        }
    }
        res=requests.post(url,headers=header,data=json.dumps(data)).json()
        print("\n批量新注册的数据，正在入链中，需要等待")
        days = 365
        for i in range(days):
            print("\r进度条百分比：{}%".format(round((i + 1) * 100 / days)), end="", flush=True)
            time.sleep(0.08)
        return  res




# if __name__ == '__main__':
#     print(device_zhuce(test_customer_url,45,"周一","mockToken").device_zhucee())
