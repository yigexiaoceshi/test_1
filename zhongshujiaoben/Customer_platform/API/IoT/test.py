#!/usr/local/bin python3.8
# -*- coding: utf-8 -*-
import requests,json

def test():
    url="http://standard.cspiretech.com:8080/api/v2/agent/iot/customer/channel/create"
    header={"Content-Type":"application/json;charset=UTF-8"}
    data={
            "reqHeader": {
                "clientType": "web",
                "requestId": "123456789012",
                "requestTime": "1628234110592",
                "token": "mockToken",
                "userId": 756,
                "userName": "周文峰"
            },
            "reqBody": {
                "type": 2,
                "name": "111",
                "protocolCode": "melsec_mc",
                "remark": "cs "
            }
        }
    res=requests.post(url,headers=header,data=json.dumps(data))
    return res.json()
# print(api())

if __name__ == '__main__':
    for i in range(2):
        print(test())
