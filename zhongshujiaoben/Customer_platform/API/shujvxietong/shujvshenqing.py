

from config import *
import requests,json

class Data_applyfor():
    def __init__(self, url, userId, token):
        self.url = url
        self.userid = userId
        self.token = token

    #获取数据申请的所有数据
    def shujvshenqing_list(self,tableName=None):
        url = f'{self.url}/api/v4/dc/dataAuth/applicableList'
        header = {'Content-Type': 'application/json', 'userId': str(self.userid)}
        data = {
              "tableName": tableName,
              "size": 20,
              "page": 1
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()



    #上传附件
    def shangchuanfujian_shujvxietong(self):
        url = f'{self.url}/api/v4/dc/file/getUploadUrl'
        header = {'Content-Type': 'application/json','userId':str(self.userid)}
        data = {
              "uploadFileName": f"{requestTime}.pdf",
              "applyType": 3
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()['data']
    #print(shangchuanfujian())
    # aaa = shangchuanfujian()
    #上传附件接口
    def shangchuanfujian01_shujvxietong(self,path):
        url = f'{self.url}{path["path"]}'
        # print(url)
        header = {'Content-Type': 'application/octet-stream','x-oss-object-acl':'private'}
        res = requests.put(url,headers=header)
        return res.status_code
    #print(shangchuanfujian01())
    #申请授权接口
    def shangchuanwenjian02_shujvxietong(self,apicode,path):
        url = f'{self.url}/api/v4/dc/dataAuth/volumeAuth'
        header = {'Content-Type': 'application/json','userId':str(self.userid)}
        data = {
              "tableCodes": [
                apicode
              ],
              "applyContacts": "无法vwe",
              "applyContactsTel": "13562478252",
              "applyAttach": path["downloadFilePath"],
              "fileName": "Python单元测试框架.pdf"
            }
        res = requests.post(url, headers=header, data=json.dumps(data))
        return res.json()
    # a = shangchuanfujian_shujvxietong()
    # print(shangchuanfujian01_shujvxietong(a))
    # print(shangchuanwenjian02_shujvxietong('20200916696295829',a))