

from config import *
import requests,json

class Topic_signin():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #Topic注册
    def add_topic(self,xitongid):
        topicCode=f"topic{requestTime}"
        url = f'{self.url}/api/v2/topic/register'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
                "userId":self.userid,
                "token":self.token

              },
              "reqBody": {
                "topicCode": topicCode,
                "chineseName": f"Topic中文{requestTime}",
                "serverCode": xitongid,
                "openAccess": "1",
                "topicDescription": "测试用的11",
                "categoryCode": "333",
                "msgDemo": "{\"type\":\"object\",\"properties\":{}}"
              }
            }
        res = requests.post(url,headers=header,data=json.dumps(data))
        return res.json(),topicCode
    #print(add_topic(10000005203))