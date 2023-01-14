


from config import *
import requests,json


class Data_signin():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #数据注册
    #1.定义数据结构
    def shujvjiegou(self,xitongname,xitongid):
        datacode = f"datazhuce{requestTime}"
        url = f'{self.url}/api/v4/dc/metaData/dataRegistration'
        header = {'Content-Type': 'application/json','userId': str(self.userid)}
        data = {
              "dataCode": datacode,
              "dataName": f"数据注册{requestTime}",
              "securityLevel": 2,
              "syncSecurityLevel": 2,
              "properties": [
                {
                  "key": 0,
                  "propCode": "qweq",
                  "propName": "胜多负少",
                  "propDataType": "number",
                  "isPrimaryKey": 0,
                  "isNotNull": 0,
                  "maxNum": 20
                }
              ],
              "systemSourceName": xitongname,
              "subSystemId": xitongid,
              "categoryRelDTOS": [

              ]
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),datacode
    # print(shujvjiegou())