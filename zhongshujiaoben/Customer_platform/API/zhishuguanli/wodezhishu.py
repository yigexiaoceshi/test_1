

import  requests
import json
from config import *

class My_Index():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #我的指数查询（已注册）
    def list_yizhucezhishu(self,indicatorName=None):
        url = f'{self.url}/api/v2/agent/indicator/getIndicatorList'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "page": 1,
                "size": 20,
                "indicatorName":indicatorName
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_yizhucezhishu("指数1602569459000"))

    #我的指数查询（已授权）
    def list_yishouquanzhishu(self,indicatorName):
        url = f'{self.url}/api/v2/agent/indicator/getAuthIndicatorList'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "page": 1,
                "size": 20,
                "indicatorName":indicatorName
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_yishouquanzhishu("指数1602569459000"))

    #指数停用
    def stop_zhishu(self,id):
        url = f'{self.url}/api/v2/agent/indicator/indicatorStateChange'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "id": id,
                "indicatorState": 0
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(stop_zhishu(5223))


    #指数启用
    def qiyong_zhishu(self,id):
        url = f'{self.url}/api/v2/agent/indicator/indicatorStateChange'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
          "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
          "reqBody": {
            "id": id,
            "indicatorState": 1
          }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(qiyong_zhishu(5223))

# from AccessManage.APIlib.yewuxietong.xitongjieru import *
# from AccessManage.APIlib.yewuxietong.zijianAPI import *
# from AccessManage.APIlib.zhishuguanli.zhishuzhuce_API import *
# xitongname = add_xitong()[1]
# print(xitongname)
# rebody = list_xitong(xitongname)['data']['list']
# print(rebody)
# serverCode = rebody[0]['serverCode']
# print(serverCode)
# zhishuapicode = add_zhishuAPI(serverCode)[0]['data']
# print(zhishuapicode)
# xinxi = zhishujibenxinxi()
# xiangxixinxi1 = xiangxixinxi(xinxi[0])
# guanlian_api(zhishuapicode)
# guanlian_num(xiangxixinxi1, zhishuapicode)
# result = list_yizhucezhishu(xinxi[1])
# print(result)
#
# xitongname1 = add_xitong()[1]
# print(xitongname1)
# rebody1 = list_xitong(xitongname1)['data']['list']
# print(rebody1)
# serverCode1 = rebody[0]['serverCode']
# print(serverCode1)
# zhishuapicode1 = add_zhishuAPI(serverCode1)[0]['data']
# print(zhishuapicode1)
# xinxi11 = zhishujibenxinxi()
# xiangxixinxi11 = xiangxixinxi(xinxi11[0])
# guanlian_api(zhishuapicode1)
# guanlian_num(xiangxixinxi11, zhishuapicode1)
# result1 = list_yizhucezhishu(xinxi11[1])
# print(result1)

