from config import *
import requests,json


class Key():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #查询密钥
    def list_key(self):
        url = f'{self.url}/api/v2/secret/subSecretList'
        header = {'Content-Type':'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "page": 1,
                "size": 10,
                "relationUserId":self.userid,
                "userId":self.userid
              }
            }
        res = requests.post(url,headers = header,data=json.dumps(data))
        return res.json()

    #print(list_key())
    #密钥详情
    def details_key(self):
        url = f'{self.url}/api/v2/secret/secretInfo'
        header = {'Content-Type': 'application/json'}
        data ={
          "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
          "reqBody": {
            "userId":self.userid
          }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(details_key())

    #列出所有关联账号
    def list_guanlianzhanghao(self):
        url = f'{self.url}/api/v2/secret/subSecretList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "page": 1,
                "size": 10,
                "userId":self.userid
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        guanlianzhanghaoid1 = res.json()['data']['items']
        guanlianzhanghaoid2 = guanlianzhanghaoid1[0]['id']
        userid = guanlianzhanghaoid1[0]['userId']
        return guanlianzhanghaoid2,userid
    # print(list_guanlianzhanghao())

    #列出所有API获取apicode给密钥和公钥授权调用
    def list_suoyouapi(self,guanlianzhanghao_id):
        url = f'{self.url}/api/v2/warrant/getApiResource'
        header = {'Content-Type': 'application/json'}
        data = {
               "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "page": 1,
                "size": 10,
                "objectId":guanlianzhanghao_id,
                "objectType": 2
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        apicode1 = res.json()['data']['items']
        apicode2 = apicode1[0]['apiCode']
        return apicode2
    # print(list_suoyouapi(8089))


    #密钥管理申请授权
    def miyao_shengqingshouquan(self,guanlianzhanghao_id,apicode):
        url = f'{self.url}/api/v2/warrant/addResource'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "objectId": guanlianzhanghao_id,
                "objectType": 2,
                "items": [
                  {
                    "itemCode": apicode,
                    "itemType": 1
                  }
                ]
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(miyao_shengqingshouquan(8074,11000096623))



    #上传公钥
    def add_gongyao(self,guanlianzhanghaoid):
        name = f'gongyao{requestTime}'
        url = f'{self.url}/api/v2/security/addPublicKey'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "name": name,
                "algorithm": "RSA",
                "relationUserId":str(guanlianzhanghaoid),
                "publicKey": f"miyao{requestTime}",
                "endTime": "2120-10-14"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),name
    # print(add_gongyao(list_guanlianzhanghao()[1]))

    #公钥查询
    def list_gongyao(self,gongyaoname):
        url = f'{self.url}/api/v2/security/publicKeys'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "page": 1,
                "size": 10,
                "name": gongyaoname
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_gongyao("gongyao1602645422000"))

    #公钥申请授权
    def gongyaoshengqingshouquan(self,gongyaoid,apicode):
        url = f'{self.url}/api/v2/warrant/addResource'
        header = {'Content-Type': 'application/json'}
        data = {
               "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "objectId":gongyaoid,
                "objectType": 1,
                "items": [
                  {
                    "itemCode":apicode,
                    "itemType": 1
                  }
                ]
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(gongyaoshengqingshouquan(16,11000096623))

    #公钥停用
    def stop_gongyao(self,gongyaoid):
        url = f'{self.url}/api/v2/security/publicKey/state'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "state": 0,
                "id": gongyaoid
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(stop_gongyao(16))

    # 公钥启用
    def qiyong_gongyao(self,guanlianzhanghaoid):
        url = f'{self.url}/api/v2/security/publicKey/state'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "state": 1,
                "id": guanlianzhanghaoid
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(qiyong_gongyao(16))