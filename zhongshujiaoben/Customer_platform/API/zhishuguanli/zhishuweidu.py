

import requests
import json
from config import *

class Index_weidu():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #维度管理-标准维度查询
    def list_biaozhunweidu(self):
        url = f'{self.url}/api/v2/agent/dimension/dimensionTree'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "type": "1"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_biaozhunweidu())

    #维度管理-自定义维度
    #新增自定义维度
    def add_zidingyiweidu(self):
        name = f'维度{requestTime}'
        url = f'{self.url}/api/v2/agent/dimension/dimensionAdd'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "pid": None,
                "type": "2",
                "bizType": "2",
                "name": name
              }
            }

        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),name
    # print(add_zidingyiweidu())

    #列出自定义维度
    def list_zidingyiweidu(self):
        url = f'{self.url}/api/v2/agent/dimension/dimensionTree'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "type": "2"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_zidingyiweidu())

    #编辑维度
    def edit_zidingyiweidu(self,id):
        url = f'{self.url}/api/v2/agent/dimension/dimensionEdit'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "id":id,
                "name": f"维度{requestTime}+a"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(edit_zidingyiweidu(333))

    #停用自定义维度
    def stop_zidingyiweidu(self,id):
        url = f'{self.url}/api/v2/agent/dimension/dimensionStateChange'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "id": id,
                "state": 0
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(stop_zidingyiweidu(333))

    #启用自定义维度
    def qiyong_zidingyiweidu(self,id):
        url = f'{self.url}/api/v2/agent/dimension/dimensionStateChange'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "id": id,
                "state": 1
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(qiyong_zidingyiweidu(331))







