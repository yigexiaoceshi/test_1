#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-



from config import *
import requests,json

class ApprovalProcess():

    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #运营方审批通过
    def shenpi_yes(self,shenqingdanhao):
        url = f'{self.url}/api/v2/operation/batchApproval'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "approveStatus": "PASS",
                "billCodeList": [
                  shenqingdanhao
                ]
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    def shenpi_yes_topic(self,shenqingdanhao):
        url = f'{self.url}/api/v2/operation/topic/apply/audit'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token
              },
              "reqBody": {
                "applyBillCode":shenqingdanhao,
                "pass": True
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()

    #运营方审批不通过
    def shenpi_no(self,shenqingdanhao):
        url = f'{self.url}/api/v2/operation/accountApproval'
        header = {'Content-Type': 'application/json'}
        data = {
              "reqHeader": {
                "userId":self.userid,
                "token":self.token

              },
              "reqBody": {
                "applyBillCode":shenqingdanhao,
                "refuseReason": "测试",
                "state": "REJECT"
              }
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()