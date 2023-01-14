

from config import *
import requests,json
import random

class System():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #新增系统
    def add_xitong(self):
        L1 = random.sample(range(1, 60000), 1)
        duankou = str(L1[0])
        sourceServerName = f'系统{requestTime}'
        url = f'{self.url}/api/v2/agent/addSubSys'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "protocol": "http",
                "sourceServerName": sourceServerName,
                "sourceServerCode": requestTime,
                "serverIp": f'172.18.111.2:{duankou}'
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        time.sleep(25)
        return res.json(),sourceServerName
    #print(add_xitong('系统8968757876','aaaaaa','172.18.111.2:9998'))

    #查询系统
    def list_xitong(self,sourceServerName):
        url = f'{self.url}/api/v2/agent/subSysList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "sourceServerName": sourceServerName
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data)).json()
        sevice_code=res["data"]["list"][0]["serverCode"]
        return res,sevice_code
    #print(list_xitong())

    #编辑系统
    def edit_xitong(self,rebody):
        id = rebody['data']['list']
        id1 = id[0]
        dict1 = {}
        dict1["domainName"] = id1['domainName']
        dict1["protocol"] = id1["protocol"]
        dict1["sourceServerName"] = id1["sourceServerName"]
        dict1["sourceServerCode"] = id1["sourceServerCode"]
        dict1["serverIp"] = id1["serverIp"]
        dict1["remark"] = id1["remark"]
        dict1["serverCode"] = id1["serverCode"]
        dict1["id"] = id1["id"]
        url = f'{self.url}/api/v2/agent/editSubSys'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
            "reqBody":dict1
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    #print(edit_xitong(dict1))

    #系统停用
    def stop_xitong(self,code):
        url = f'{self.url}/api/v2/agent/subSysStop'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "serverCode": code,
                "effectiveTime": effectiveTime
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    # id2 = list_xitong()['data']['list']
    # id3 = id2[0]['serverCode']
    #print(stop_xitong(id3))

    #系统启用
    def resume_xitong(self,code):
        url = f'{self.url}/api/v2/agent/subSysResume'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
            "reqBody": {
                "serverCode": code
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # id4 = list_xitong()['data']['list']
    # id5 = id[0]['serverCode']
    # print(resume_xitong(id5))



