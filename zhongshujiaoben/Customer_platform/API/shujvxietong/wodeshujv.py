

from config import *
import requests,json
from Customer_platform.API.shujvxietong.shujvzhuce import *

class My_Data():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token


    #从用户详情获取接入方编号
    def appInfoId(self):
        url = f'{self.url}/api/v2/agent/userCenter'
        header = {'Content-Type': 'application/json'}
        data = {
                    "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {

              }
            }
        res = requests.post(url,headers=header,data=json.dumps(data))
        return res.json()['data']['appInfoId']
    # print(appInfoId())

    #查询我的数据(已注册)
    def list_shujvzhuce(self,datacode):
        url = f'{self.url}/api/v4/dc/metaData/myData'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        name=f'ods_{self.appInfoId()}_{datacode}'
        data = {
              "dataCode": name,
              "status": 1,
              "size": 20,
              "page": 1
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),name
    # print(list_shujv(shujvjiegou()[1]))

    #查询我的数据（已授权）
    def list_shujvshouquan(self,datacode):
        url = f'{self.url}/api/v4/dc/metaData/authAndSubList'
        header = {'Content-Type': 'application/json','userId': str(self.userid)}
        # name=f'ods_{self.appInfoId()}_{datacode}'
        data = {
              "dataCode": datacode,
              "size": 20,
              "page": 1
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_shujvshouquan(shujvjiegou()[1]))


