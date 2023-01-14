#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-


import requests,json
import re
import pyDes,base64
Des_Key = b"d6d94543" # 相当于加密盐
Des_IV = b"\x22\x33\x35\x81\xBC\x38\x5A\xE7" # 自定IV向量（不知道什么用，官网例子就是这么写的）
def desencrypt(s):
    k = pyDes.des(Des_Key, pyDes.ECB, Des_IV, pad=None, padmode=pyDes.PAD_PKCS5)
    encrystr = k.encrypt(s)
    aaa = base64.b64encode(encrystr)
    bbb = str(aaa, encoding="utf-8")
    return bbb
#print(desencrypt('Aa123456'))


# python3.6环境
from urllib import request
from http import cookiejar

def SERVERID():
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    opener.open('http://172.18.110.124/')
    # 打印cookie信息
    dict1 = {}
    for item in cookie:
        # print('Name = %s' % item.name)
        # print('Value = %s' % item.value)
        dict1[item.name] = item.value
    return dict1

#判断有没有登录
def login_01():
    url = 'http://172.18.110.124:1001/oauth/authorize?'
    data = {
        'response_type': 'code',
        'client_id':'2bbbe973cfa04332a26110cb0474ae5b',
        'redirect_uri': 'http: // 172.18.110.124',
        'state': 3538
    }
    res = requests.get(url,cookies = SERVERID(),params=data)
    return res.headers



def huoqv_cookie():
    url = 'http://172.18.110.124:1000/'
    res = requests.get(url)
    # cook = res.headers['Set-Cookie']
    # pages = re.findall('(.*?);Path=/',cook, re.S)
    return res.cookies.get_dict()

#获取token
def sessionid(username,password):
    url = 'http://172.18.110.124:1000/login/form'
    #header = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'username': username,
        'password': desencrypt(password)
    }
    res = requests.post(url,data=data,cookies=huoqv_cookie())
    return res.headers

def login():
    url = 'http://172.18.110.124:1000/login/form'
    header = {'Content-Type':'application/x-www-form-urlencoded'}
    data = {
        'username':'test_one',
        'password':'qAHcIhB1wBS9S11pLQqgFQ=='
    }
    res = requests.post(url, headers=header,data=data)
    print(res.headers)
    sessionid = res.headers['Set-Cookie']
    pages = re.findall('SERVERID=(.*?);Path=/',sessionid, re.S)
    return pages[0]


def set_token():
    url = 'http://172.18.110.124:10080/api/v2/getOauthUserInfo'
    header = {'Content-Type': 'application/json','Cookie':'uc-session-id=YmFlYWViOWQtNWY3NC00MzRhLWE2MWEtNDllODc5YTc4NzNl; SERVERID=dd17356ccc9e1183df199aff4a4e69ad|1600324528|1600322920'}
    print(header)
    data = {
          "reqHeader": {

          },
          "reqBody": {
            "code": "HK2Ppm",
            "state": "4880",
            "redirectUri": "http://172.18.110.124:10080"
          }
        }
    res = requests.post(url, headers=header,data=json.dumps(data))
    return res.json()


#API授权
def api_authorization():
    url = 'http://172.18.110.124:10080/api/v2/agent/customerIndicatorList'
    header = {'Content-Type':'application/json'}
    data = {
          "reqHeader": {
            "userId": 763,
            "userName": "周三01",
            "token": "63faad5e-cb08-468d-958f-20a63cb3f563",
            "clientType": "web",
            "requestTime": "1600308063233",
            "requestId": "123456789012"
          },
          "reqBody": {
            "pageNumber": 1,
            "pageSize": 10,
            "approveStatus": "",
            "targetAppName": "",
            "applyBillCode": "",
            "applyType": 1
          }
        }
    res = requests.post(url,headers=header,data=json.dumps(data))
    return res.json()


# from selenium import webdriver
#
# driver = webdriver.PhantomJS()
# url = "http://172.18.110.124/"
# driver.get(url)
# # 获取cookie列表
# cookie_list = driver.get_cookies()
# # 格式化打印cookie
# cookie_dict={}
# for cookie in cookie_list:
#     cookie_dict[cookie['name']] = cookie['value']
#print(cookie_dict)



if __name__ == '__main__':

    print(SERVERID())
#
    print(login_01())
    #print(login_02())
#     print(huoqv_cookie())
#     #print(User_login())
#     #print(sessionid('test_one','Aa123456'))
#     #print(set_token())
#     #print(api_authorization())