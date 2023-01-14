

from config import *
import requests,json


class My_Topic():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #Topic查询(注册)
    def list_topiczhuce(self,topicCode):
        url = f'{self.url}/api/v2/topic/list'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "size": 15,
                "page": 1,
                "topicCode":topicCode,
                "orderByCreatedTimeDesc": True,
                "from": 1
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_topic('topic1602558540000'))

    #Topic查询(已授权)
    def list_topicshouquan(self,topicCode):
        url = f'{self.url}/api/v2/topic/permission/list'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "size": 15,
                "page": 1,
                "apiDesc": topicCode,
                "orderByCreatedTimeDesc": True
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_topicshouquan('topic1602558540000'))

    #Topic查询(订阅中)
    def list_topicdingyue(self,topicCode):
        url = f'{self.url}/api/v2/topic/permission/list'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "size": 15,
                "page": 1,
                "status": 1,
                "apiDesc": topicCode,
                "orderByCreatedTimeDesc": True
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_topicdingyue('topic1602558540000'))





    #Topic编辑
    def edit_topic(self,topicCode):
        dict1 = {}
        dict2 = self.list_topiczhuce(topicCode)['data']['records']
        dict1["topicCode"] = dict2[0]['topicCode']
        dict1["chineseName"] = f"Topic中文{requestTime}"
        dict1["openAccess"] = dict2[0]['openAccess']
        dict1["topicDescription"] = dict2[0]["topicDescription"]
        dict1["categoryCode"] = dict2[0]['imCategoryId']
        dict1["msgDemo"] = dict2[0]['msgDemo']
        url = f'{self.url}/api/v2/topic/modify'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": dict1
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(edit_topic('topic1602558540000'))