

from config import *
import requests,json



class Data_task():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token
    #新建任务

    def add_renwu(self,APIcode,dataname,datacode):
        taskcode = f"renwu{requestTime}"
        url = f'{self.url}/api/v4/dc/taskManage/addTask'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "taskCode":taskcode ,
              "taskName": f"任务{requestTime}",
              "dataSourceType": 1,
              "taskType": 0,
              "maxPageSize": 10,
              "totalApiName": "测试专用",
              "totalApiCode": APIcode,
              "pageDataApiName": "测试专用",
              "pageDataApiCode": APIcode,
              "targetTableName": dataname,
              "targetTableCode": str(datacode)
            }
        res = requests.post(url,headers=header,data=json.dumps(data))
        return res.json(),taskcode
    # print(add_renwu(11000096623,"数据注册",20201012833493714))

    #查询任务
    def list_renwu(self,renwuname):
        url = f'{self.url}/api/v4/dc/taskManage/taskList'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "taskCode": renwuname,
              "size": 20,
              "page": 1
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_renwu('renwu1602498105000'))

    #停用任务
    def tingyong_renwu(self,shujvyuanid,renwuid):
        url = f'{self.url}/api/v4/dc/taskManage/switchTask?'
        header = {'userId': str(self.userid)}
        data = {'id': shujvyuanid,
                'taskID': renwuid,
                'status': 0}
        res = requests.post(url, headers=header, data=data)
        return res.json()
    # print(tingyong_renwu(8,38))

    #启用任务
    def qiyong_renwu(self,shujvyuanid,renwuid):
        url = f'{self.url}/api/v4/dc/taskManage/switchTask?'
        header = {'userId': str(self.userid)}
        data = {'id': shujvyuanid,
                'taskID': renwuid,
                'status': 1}
        res = requests.post(url, headers=header, data=data)
        return res.json()
    # print(qiyong_renwu(8,38))

    #任务执行
    def zhixing_renwu(self,shujvyuanid,renwuid):
        url = f'{self.url}/api/v4/dc/taskManage/executeTask?'
        header = {'userId': str(self.userid)}
        data = {'id': shujvyuanid,
                'taskID': renwuid}
        res = requests.post(url, headers=header, data=data)
        return res.json()
    # print(zhixing_renwu(8,38))

    #执行记录查看
    def list_zhixingjilu(self,renwuname):
        url = f'{self.url}/api/v4/dc/log/getExecutedLog'
        header = {'Content-Type':'application/json','userId':str(self.userid)}
        data = {
              "taskCode": renwuname,
              "size": 20,
              "page": 1
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # print(list_zhixingjilu('renwu111'))

    #停止执行
    def stop_zhixing(self,id):
        url = f'{self.url}/api/v4/dc/taskManage/switchTask?'
        header = {'userId': str(self.userid)}
        data = {
            'id':id,
            'status': 0
        }
        res = requests.post(url, headers=header, data=data)
        return res.status_code
    # print(stop_zhixing(14))