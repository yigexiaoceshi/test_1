

from config import *
import requests,json

class Account():
    def __init__(self,url,userId,token):
        self.url = url
        self.userid = userId
        self.token = token

    def yonghuxiangqing(self):
        url = f'{self.url}/api/v2/agent/userCenter'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId": self.userid,
                "token":self.token
              },
              "reqBody": {

              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()['data']['loginName']
    # print(yonghuxiangqing())



    #新增账号
    def add_account(self):
        loginname = f"{self.yonghuxiangqing()}_{requestTime}"
        url = f'{self.url}/api/v2/account/createChildAccount'
        header = {'Content-Type':'application/json'}
        data = {
              "reqHeader": {
                "userId": self.userid,
                "token":self.token
              },
              "reqBody": {
                "loginName": loginname,
                "roleId": "-3",
                "userName": f'用户{requestTime}',
                "mobile": "17700000010",
                "secretKeyExpire": "4754966432095"
              }
            }
        res = requests.post(url,headers = header,data=json.dumps(data))
        return res.json(),loginname
    #print(add_account('bbbb','显示'))

    #查询账号
    def list_account(self,name=None):
        url = f'{self.url}/api/v2/account/search'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId": self.userid,
                "token":self.token
              },
              "reqBody": {
                "page": 1,
                "size": 10,
                "loginName": name
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    #print(list_account())

    #账号详情
    def details_account(self,id):
        url = f'{self.url}/api/v2/account/detail'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "id": id
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # id1 = list_account()['data']['items']
    # print(details_account(id1[0]['id']))

    #账号编辑
    def edit_account(self,rebody):
        id1 = rebody['data']['items']
        # print(id1)
        dict1 = self.details_account(id1[0]['id'])['data']
        reqBody = {}
        reqBody["loginName"] = dict1['loginName']
        reqBody["roleId"] = [int(dict1['roleId'])]
        reqBody["userName"] = dict1['userName']
        reqBody["mobile"] = dict1['mobile']
        reqBody["email"] = dict1["email"]
        reqBody["remark"] = dict1["remark"]
        reqBody["userId"] = dict1['id']
        reqBody['userName'] = f'新用户{requestTime}'
        url = f'{self.url}/api/v2/account/accountEdit'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": reqBody
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    # print(edit_account(list_account('zhejiangxunfu_8596')))