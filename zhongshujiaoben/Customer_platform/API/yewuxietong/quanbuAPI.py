

from config import *
import requests,json
class All_API():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #全部API列表展示
    def list_quanbuAPI(self,apiCode=None):
        url = f'{self.url}/api/v2/agent/apiMarket'
        header = {'Content-Type': 'application/json','userId':str(self.userid)}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
              "reqBody": {
                "page": 1,
                "size": 10,
                "apiCode": apiCode,
                "appShortName": None,
                "apiDesc": None
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    #print(list_quanbuAPI())



    #上传附件
    def shangchuanfujian(self):
        url = f'{self.url}/api/v2/agent/getUploadUrl'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "uploadFileName": f"{requestTime}.pdf",
                "applyType": 1
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()['data']
    #print(shangchuanfujian())
    # aaa = shangchuanfujian()
    #上传附件接口
    def shangchuanfujian01(self,path):
        url = f'{self.url}{path["path"]}'
        # print(url)
        header = {'Content-Type': 'application/octet-stream','x-oss-object-acl':'private'}
        res = requests.put(url,headers=header)
        return res.status_code
    #print(shangchuanfujian01())
    #申请授权接口
    def shangchuanwenjian02(self,apicode,path):
        url = f'{self.url}/api/v2/agent/asyncApplyAuth'
        header = {'Content-Type': 'application/json'}
        data = {
                "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "contact": "任务单",
                "phone": "17131059693",
                "fileName": "思维导图：面向对象.doc",
                "applyType": 1,
                "approveBy": 0,
                "resourceCodeList": [
                  apicode
                ],
                "filePath": path["path"],
                "applyBillCode": ""
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    #print(shangchuanwenjian02())


    #已授权数据展示
    def list_yishouquanAPI(self,apiCode=None):
        url = f'{self.url}/api/v2/agent/authApiList'
        header = {'Content-Type': 'application/json'}
        data = {
          "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
          "reqBody": {
            "page": 1,
            "size": 10,
            "apiCode":apiCode
          }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

if __name__ == '__main__':
    al = All_API('http://standard.cspiretech.com:8080',757,'mockToken')
    print(al.shangchuanwenjian02())


