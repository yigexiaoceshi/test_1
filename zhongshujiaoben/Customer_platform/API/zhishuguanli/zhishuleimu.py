

import  requests
import json
from config import *


class Index_leimu():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #查询标准指数类目
    def list_biaozhunzhishuleimu(self):
        url = f'{self.url}/api/v2/agent/category/categoryList'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "pageNum": 1,
                "pageSize": 20,
                "parentId": None,
                "bizType": "indicator",
                "type": "standard"
              }
            }
        res = requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(list_biaozhunzhishuleimu())

    #新增自定义类目
    def add_zhishuzhidingyileimu(self):
        name = f'自定义类目{requestTime}'
        url = f'{self.url}/api/v2/agent/category/categoryAdd'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "bizType": "indicator",
                "type": "Customer",
                "parentId": None,
                "name": name
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),name
    #print(add_zhishuzhidingyileimu())

    #查询自定义类目
    def list_zhishuzidingyileimu(self):
        url = f'{self.url}/api/v2/agent/category/categoryList'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "pageNum": 1,
                "pageSize": 20,
                "parentId": 0,
                "bizType": "indicator",
                "type": "Customer"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_zhishuzidingyileimu())

    #编辑自定义类目
    def edit_zhishuzidingyileimu(self,id):
        url = f'{self.url}/api/v2/agent/category/categoryEdit'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "id": id,
                "name": f"自定义类目{requestTime+1}"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # id1 = list_zhishuzidingyileimu()['data']['records']
    # id2=id1[0]['id']
    # print(edit_zhishuzidingyileimu(id2))

    #删除自定义类目
    def del_zhishuzidingyileimu(self,id):
        url = f'{self.url}/api/v2/agent/category/categoryDelete'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "categoryId": id
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # id1 = list_zhishuzidingyileimu()['data']['records']
    # id2=id1[0]['id']
    # print(del_zhishuzidingyileimu(id2))



