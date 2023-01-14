

import  requests
import json
from config import *


class Index_applyfor():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #指数申请查询
    def list_zhishushengqing(self,zhishuname=None):
        url = f'{self.url}/api/v2/agent/indicatorMarket'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "page": 1,
                "size": 20,
                "indicatorName": zhishuname
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_zhishushengqing())


    #上传附件
    def zhishushangchuanfujian(self):
        url = f'{self.url}/api/v2/agent/getUploadUrl'
        header = {'Content-Type': 'application/json','userId': str(self.userid)}
        data = {
              "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "uploadFileName": f"{requestTime}.pdf",
                "applyType": 2
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()['data']
    #print(shangchuanfujian())
    # aaa = zhishushangchuanfujian()
    #上传附件接口
    def zhishushangchuanfujian01(self,aaa1):
        url = f'{self.url}{aaa1["path"]}'
        header = {'Content-Type': 'application/octet-stream','x-oss-object-acl':'private'}
        res = requests.put(url,headers=header)
        return res.status_code
    #print(shangchuanfujian01())
    #申请授权接口
    def zhishushangchuanwenjian02(self,indicatorCode,aaa1):
        url = f'{self.url}/api/v2/agent/asyncApplyAuth'
        header = {'Content-Type': 'application/json','userId': str(self.userid)}
        data = {
                "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "contact": "任务单",
                "phone": "17131059693",
                "fileName": "思维导图：面向对象.doc",
                "applyType": 2,
                "approveBy": 0,
                "resourceCodeList": [
                  indicatorCode
                ],
                "filePath": aaa1["path"]
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(zhishushangchuanwenjian02(10000000555,aaa))