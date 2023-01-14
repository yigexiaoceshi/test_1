

from config import *
import requests,json,random
# zhishuapi_name=f'指数API{requestTime}'
#yewuapi_name=f'业务API{requestTime}'
num = random.randint(1,100)
class Api():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #创建指数类API

    def add_zhishuAPI(self,serverCode):
        zhishuapi_name = f'指数API{requestTime+num}'
        sourceApiCode = requestTime
        url = f'{self.url}/api/v2/agent/addApiV2'
        header = {'Content-Type': 'application/json'}
        data = {
          "reqHeader": {
            "userId": self.userid,
            "token":self.token
          },
          "reqBody": {
            "relationCategorys": [

            ],
            "serviceName":zhishuapi_name,
            "contactor": "dvsv",
            "contactorMobile": "13245789658",
            "relationSubSys": [

            ],
            "apiDesc": "测试",
            "method": "POST",
            "sourceApiCode":str(sourceApiCode),
            "apiInterval": "600",
            "path": "/biz/api-list/add",
            "serverCode": serverCode,
            "businessType": "INDICATOR",
            "metaJson": json01,
            "metaJsonExample":json03,
            "indicatorCodes": [

            ],
            "effectiveTime": "",
            "testPath": "",
            "remarks": "<p></p>"
          }
        }
        # print(json.dumps(json01))
        # print(json.dumps(data))
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json(),zhishuapi_name,sourceApiCode
    # print(add_zhishuAPI(10000005203))

    #创建业务类API
    #1. API基本信息
    def jibenxinxi(self,belongSystem):
        yewuapi_name = f'业务API{requestTime}'
        yewuapicode = requestTime+1
        url = f'{self.url}/api/v2/agent/addApiV3/defservie'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "serviceName":yewuapi_name,
                "serviceVersion": "1.0",
                "contactor": "dvsv",
                "contactorMobile": "13245789658",
                "sourceApiCode": yewuapicode,
                "belongSystem": belongSystem,
                "serviceDesc": "测试专用",
                "relationCategorys": [
                ]
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()['data'],yewuapi_name,yewuapicode

    #2. API配置
    def APIpeizhi(self,uuid):
        url = f'{self.url}/api/v2/agent/addApiV3/defprotocal'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "protocolIn": "rest",
                "uuid": uuid,
                "apiPath": "/api/list_aaa",
                "requestMethod": "get",
                "apiInterval": "600",
                "metaJson": json.dumps(json02)
            }}
        requests.post(url, headers=header, data=json.dumps(data))


    #3.访问限制
    def fangwenxianzhi(self,uuid):
        url = f'{self.url}/api/v2/agent/addApiV3/defproperties'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "uuid": uuid,
                "qps": 300,
                "cacheTime": 50,
                "onCache": 1
              }
            }
        requests.post(url, headers=header, data=json.dumps(data))

    # uuid1 = jibenxinxi(10000005203)[0]
    # APIpeizhi(uuid1)
    # fangwenxianzhi(uuid1)
    #4. 发布
    def fabu(self,uuid):
        # uuid1 = self.jibenxinxi(xitongcode)
        # self.APIpeizhi(uuid1[0])
        # self.fangwenxianzhi(uuid1[0])
        url = f'{self.url}/api/v2/agent/addApiV3'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "uuid": uuid
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        time.sleep(25)
        return res.json()

    # print(fabu(10000005104))

    #查询API
    def list_zijianAPI(self,sourceApiCode=None):
        url = f'{self.url}/api/v2/agent/apiList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "sourceApiCode":sourceApiCode,
                "apiDesc": "",
                "serverCode": "",
                "page": 1,
                "size": 40
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data)).json()
        api_code=res["data"]["records"][0]["apiCode"]
        return res,api_code
    # print(list_zijianAPI())

    #API详情
    def xiangqing_API(self,appApiId):
        url = f'{self.url}/api/v2/agent/apiDetail'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "appApiId": appApiId
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    #print(xiangqing_API(372398))

    #API停用
    def stop_API(self,id):
        url = f'{self.url}/api/v2/agent/apiState'
        header = {'Content-Type': 'application/json'}
        data = {
          "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
          "reqBody": {
            "id": id,
            "effectiveTime": effectiveTime,
            "state": 0
          }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    #print(stop_API(372398))

    #API启用
    def state_API(self,id):
        url = f'{self.url}/api/v2/agent/apiState'
        header = {'Content-Type': 'application/json'}
        data = {
            "reqHeader": {
            "userId":self.userid,
            "token":self.token
          },
            "reqBody": {
                "id": id,
                "state": 1
            }
        }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    #print(state_API(372398))


if __name__ == '__main__':
    ap = Api('http://172.18.111.84:8080',793,'mockToken')
    print(ap.add_zhishuAPI(10000000813))

