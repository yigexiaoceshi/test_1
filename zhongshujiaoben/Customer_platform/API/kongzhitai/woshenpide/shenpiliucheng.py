
from config import *
import requests,json

class Approval_process():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #我申请的-指数授权
    def shenqing_zhishu(self,shenqingdanhao):
        url = f'{self.url}/api/v2/agent/customerIndicatorList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token,
              },
              "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "targetAppName": "",
                "applyBillCode":shenqingdanhao,
                "applyType": 2
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(shenqing_zhishu('1220201027000007'))

    #我申请的-API授权
    def shenqing_API(self,shenqingdanhao):
        url = f'{self.url}/api/v2/agent/customerIndicatorList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "targetAppName": "",
                "applyBillCode":shenqingdanhao,
                "applyType": 1
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(shenqing_API(1220201027000007))

    #我申请的-数据授权
    def shenqing_shujv(self,shenqingdanhao):
        url = f'{self.url}/api/v2/agent/customerIndicatorList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "createTimeList": [

                ],
                "targetAppName": "",
                "applyBillCode":shenqingdanhao,
                "applyType": 3
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(shenqing_shujv(1220201027000007))

    #我申请的-Topic授权
    def shenqing_Topic(self,topicCode):
        url = f'{self.url}/api/v2/topic/apply/list'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "page": 1,
                "size": 10,
                "appName": "",
                "applyBillCode":"",
                "topicCode":topicCode
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(shenqing_Topic(1220201027000007))

    #我审批的-待审批
    def shenpi_daishenpi(self,shenqingdanhao,pageNumber=1):
        url = f'{self.url}/api/v2/agent/approvalList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "pageNumber": pageNumber,
                "pageSize": 10,
                "applyBillCode":str(shenqingdanhao),
                "targetApproveStatus": [
                  "ING"
                ]
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(shenpi_daishenpi(1220201027000007))

    #我审批的-已审批
    def shenpi_yishenpi(self,shenqingdanhao):
        url = f'{self.url}/api/v2/agent/approvalList'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "pageNumber": 1,
                "pageSize": 10,
                "applyBillCode":shenqingdanhao,
                "targetApproveStatus": [
                  "PASS",
                  "REJECT"
                ]
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(shenpi_yishenpi(1220201027000007))

    #接入方审批通过
    def jieru_shenpi_yes(self,shenpidanhao):
        url = f'{self.url}/api/v2/agent/approval'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "billCodeList": [
                  shenpidanhao
                ],
                "approveStatus": "PASS"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    #接入方审批不通过
    def jieru_shenpi_no(self,shenpidanhao):
        url = f'{self.url}/api/v2/agent/approval'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "billCodeList": [
                  shenpidanhao
                ],
                "approveStatus": "REJECT",
                "refuseReason": "测试"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
