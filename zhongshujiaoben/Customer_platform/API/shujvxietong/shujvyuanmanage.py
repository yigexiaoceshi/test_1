

from config import *
import requests,json

# dataSourceCode1 = f"sjy{requestTime}"


class Data_source():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #新增数据源
    def add_shujvyuan(self,xitongid,xitongname):
        dataSourceCode1 = f"sjy{requestTime}"
        url = f'{self.url}/api/v4/dc/metaData/addDataSource'
        header = {'Content-Type': 'application/json','userId': str(self.userid)}
        data = {
          "dataSourceType": 1,
          "dataSourceCode": dataSourceCode1,
          "dataSourceCnName": f"数据源{requestTime}",
          "dataSourceHost": "172.0.45.44",
          "dataSourcePort": "5050",
          "dataSourceName": "哈哈",
          "dataSourceUserName": "saxas11",
          "dataSourcePassWord": "12345611",
          "subSystemId": str(xitongid),
          "subSystemName": xitongname
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),dataSourceCode1
    # print(add_shujvyuan(dataSourceCode1,1228,"系统8968757876"))

    #查询数据源
    def list_shujvyuan(self,dataSourceName=None):
        url = f'{self.url}/api/v4/dc/metaData/findDataSource'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "dataSourceName": dataSourceName,
              "size": 20,
              "page": 1
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    #print(list_shujvyuan(dataSourceCode1))


    #编辑数据源
    def edit_shujvyuan(self,data1):
        dict2 = {}
        dict1 = data1['data']['list']
        dict2["dataSourceType"] = dict1[0]["dataSourceType"]
        dict2["dataSourceCnName"] = dict1[0]["dataSourceCnName"]
        dict2["dataSourcePassWord"] = dict1[0]["dataSourcePassWord"]
        dict2["dataSourcePort"] = dict1[0]["dataSourcePort"]
        dict2["dataSourceHost"] = dict1[0]["dataSourceHost"]
        dict2["dataSourceName"] = dict1[0]["dataSourceName"]
        dict2["id"] = dict1[0]["id"]
        dict2["dataSourceCode"] = dict1[0]["dataSourceCode"]
        dict2["dataSourceDesc"] = dict1[0]["dataSourceDesc"]
        dict2["dataSourceUserName"] = dict1[0]["dataSourceUserName"]
        dict2["subSystemId"] = dict1[0]["subSystemId"]
        url = f'{self.url}/api/v4/dc/metaData/editDataSource'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = dict2
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    #print(edit_shujvyuan(8,1228,dataSourceCode1))
    # dict2 = {}
    # dict1 = list_shujvyuan(dataSourceCode1)['data']['list']
    # dict2['dataSourceHost']=dict1[0]['dataSourceHost']
    # dict2['dataSourceName']=dict1[0]['dataSourceName']
    # dict2['dataSourcePassWord']=dict1[0]['dataSourcePassWord']
    # dict2['dataSourcePort']=dict1[0]['dataSourcePort']
    # dict2['dataSourceType']=dict1[0]['dataSourceType']
    # dict2['dataSourceUserName']=dict1[0]['dataSourceUserName']
    #测试数据源
    def tc_shujvyuan(self,datayuanliat):
        dict2 = {}
        dict1 = datayuanliat['data']['list']
        dict2['dataSourceHost']=dict1[0]['dataSourceHost']
        dict2['dataSourceName']=dict1[0]['dataSourceName']
        dict2['dataSourcePassWord']=dict1[0]['dataSourcePassWord']
        dict2['dataSourcePort']=dict1[0]['dataSourcePort']
        dict2['dataSourceType']=dict1[0]['dataSourceType']
        dict2['dataSourceUserName']=dict1[0]['dataSourceUserName']
        url = f'{self.url}/api/v4/dc/metaData/testDataSource'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = dict2
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.status_code
    # print(test_shujvyuan(dict2))

