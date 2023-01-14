
from config import *
import requests,json

class Topic_applyfor():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #列出申请列表中的所有Topic
    def list_suoyoutopic(self,topicCode=None):
        url = f'{self.url}/api/v2/topic/list'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,

                "token":self.token
              },
              "reqBody": {
                "page": 1,
                "size": 40,
                "from": 0,
                "openAccess": 1,
                "topicCode": topicCode

              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_suoyoutopic())


    #上传附件
    def Top_shangchuanfujian(self):
        url = f'{self.url}/api/v2/agent/getUploadUrl'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
            "userId":self.userid,
            "token":self.token

          },
              "reqBody": {
                "uploadFileName": f"{requestTime}.pdf",
                "applyType": 6
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()['data']
    #print(shangchuanfujian())
    # aaa = Top_shangchuanfujian()
    #上传附件接口
    def Top_shangchuanfujian01(self,aaa1):
        url = f'{self.url}{aaa1["path"]}'
        #print(url)
        header = {'Content-Type': 'application/octet-stream','x-oss-object-acl':'private'}
        res = requests.put(url,headers=header)
        return res.status_code
    #print(Top_shangchuanfujian01(aaa))
    #申请授权接口
    def Topic_shangchuanwenjian02(self,topiccode,aaa1):
        url = f'{self.url}/api/v2/topic/apply/submit'
        header = {'Content-Type': 'application/json'}
        data = {
                "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
              "reqBody": {
                "contact": "任务单",
                "phone": "17131059693",
                "fileName": "Python单元测试框架.pdf",
                "applyType": "topic",
                "resourceList": [
                  topiccode
                ],
                "filePath": aaa1["path"]
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    # print(Topic_shangchuanwenjian02("TopicCode003",aaa))