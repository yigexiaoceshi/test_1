

from config import *
import requests,json

class API_Leimu():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #标准类目查询
    def list_biaozhunleimu(self,categoryName=None):
        url = f'{self.url}/api/v2/agent/category/categoryList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "categoryName": categoryName,
                "pageNum": 1,
                "pageSize": 10,
                "parentId": None,
                "bizType": "api",
                "type": "standard"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_biaozhunleimu())

    #新增自定义类目
    def add_zidingyileimu(self):
        name = f'类目{requestTime}'
        url = f'{self.url}/api/v2/agent/category/categoryAdd'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "bizType": "api",
                "type": "Customer",
                "parentId": None,
                "name": name
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),name
    # print(add_zidingyileimu('类目类目11'))

    #查询自定义类目
    def list_zidingyileimu(self,categoryName=None,zidingyileimuid=None):
        url = f'{self.url}/api/v2/agent/category/categoryList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "categoryName": categoryName,
                "pageNum": 1,
                "pageSize": 10,
                "parentId":zidingyileimuid,
                "bizType": "api",
                "type": "Customer"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_zidingyileimu())

    #编辑自定义类目
    def edit_zidingyileimu(self,leimuid):
        url = f'{self.url}/api/v2/agent/category/categoryEdit'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "id": leimuid,
                "name": f'类目{requestTime+1000000000}'
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(edit_zidingyileimu(372))

    #删除自定义类目
    def del_zidingyileimu(self,leimuid):
        url = f'{self.url}/api/v2/agent/category/categoryDelete'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "categoryId": str(leimuid)
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(del_zidingyileimu(373))