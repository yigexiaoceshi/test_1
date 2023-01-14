

from config import *
import requests,json


class Role():

    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #新增角色
    def add_role(self,):
        name = f'角色{requestTime}'
        url = f'{self.url}/api/v2/privilege/role/create'
        header = {'Content-Type':'application/json'}
        data = {
              "reqHeader": {
                "userId": self.userid,
                "token":self.token
              },
              "reqBody": {
                "roleName":name,
                "purviewIds": quanxian_list
              }
            }
        res = requests.post(url,headers = header,data=json.dumps(data))
        return res.json(),name
    # print(add_role())

    #查询角色
    def list_role(self,roleName=None):
        url = f'{self.url}/api/v2/privilege/role/search'
        header = {'Content-Type': 'application/json'}
        data ={
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "page": 1,
                "size": 10,
                "roleName": roleName
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    #print(list_role())

    #编辑角色
    def edit_role(self,rolename,id):
        url = f'{self.url}/api/v2/privilege/role/edit'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "roleName": rolename,
                "purviewIds": quanxian_list,
                "id": id
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # id1 = list_role()['data']['items']
    # print(edit_role('角色000000',id1[0]['id']))

    #删除角色
    def del_role(self,id):
        url = f'{self.url}/api/v2/privilege/role/delRole'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "roleId": id
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # id1 = list_role()['data']['items']
    # print(del_role(id1[0]['id']))
if __name__ == '__main__':
    rm = Role(kaifa_jierufang_url,userId_jierufang02,token_jierufang02)
    print(rm.add_role())