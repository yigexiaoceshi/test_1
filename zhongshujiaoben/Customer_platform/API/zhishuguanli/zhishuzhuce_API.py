
import requests,random
import json
from config import *
num = random.randint(1,10)

class Index_signin():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #指数基本信息一
    def zhishujibenxinxi(self):
        indicatorName= f'指数{requestTime+num}'
        url=f'{self.url}/api/v2/agent/indicator/addIndicator'
        header={'Content-Type':'application/json','userId':str(self.userid)}
        data={
            "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
            "reqBody": {
                "indicatorCategorys": [],
                "indicatorName": indicatorName,
                "indicatorUnit": "中枢",
                "computeFrequency": "60",
                "frequencyUnit": "s",
                "indicatorNote": "指数定义",
                "computeNote": "测试数据",
                "businessContacts": "陈三",
                "businessPhone": "17757565999",
                "responsibleAppInfoId": 70,
                "responsibleLeader": "周三",
                "refreshCycle": {
                    "dimensionCode": 1000075,
                    "name": "时"
                },
                "applyRange": {
                    "dimensionCode": 1000079,
                    "name": "省"
                },
                "usableDimension": []
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()['data']['id'],indicatorName,res.json()['data']['indicatorCode']
    # print(zhishujibenxinxi())

    #指数填写信息二
    def xiangxixinxi(self,id):
        url=f'{self.url}/api/v2/agent/indicator/indicatorDetail'
        header={'Content-Type':'application/json','userId':str(self.userid)}
        data={
            "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
            "reqBody": {
                "id": str(id)
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return  res.json()['data']
    # a = jibenxinxi()[0]['data']['id']
    # print(a)
    # print(xiangxixinxi(a))

    #指数关联API
    def guanlian_api(self,apiCode):
        url=f'{self.url}/api/v2/agent/getApiDetail'
        header={'Content-Type':'application/json','userId':str(self.userid)}
        data={
            "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
            "reqBody": {
                "apiCode": apiCode
            }
        }
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(guanlian_api()['data']['appInfoId'])
    # aaa=xiangxixinxi()
    #关联数据
    def guanlian_num(self,aaa,apiCode):
        aaa['apiCode']=apiCode
        aaa['indicatorCategorys']=[]
        aaa['indicatorValue']='data.field_1'
        aaa['apiRequestParamDetail']={}
        aaa['apiResponseParamDetail']={}
        del aaa['relationCategorys']
        url=f'{self.url}/api/v2/agent/indicator/updateIndicator'
        header={'Content-Type':'application/json','userId':str(self.userid)}
        data={
            "reqHeader": {
                "userId":self.userid,
                "token":self.token
            },
            "reqBody":aaa
        }
        #print(aaa)
        res=requests.post(url,headers=header,data=json.dumps(data))
        return res.json()
    # print(guanlian_num(11000096612))





