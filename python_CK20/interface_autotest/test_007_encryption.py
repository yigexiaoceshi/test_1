#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
只是用base64解密算法对响应正文做解密处理。

本机demo演示环境准备：
1、准备一个json文件，比如：demo.json
2、使用命令进行加密：base64 demo.json > demo.txt
3、在demo.txt的当前目录启动一个Python服务：python -m http.server 9999
4、本机即可在浏览器访问：http://127.0.0.1:9999
5、新增一个方法，创建一个请求，对http://127.0.0.1:9999/demo/txt发起请求时，返回的结果是一个已经base64算法加密过后的信息
6、当前演示就是给这个加密过的响应体进行解密展示
"""
import json
import requests
import base64


class ApiRequest():

    def send(self, data: dict):
        res = requests.request(data['method'], data['url'], headers=data['headers'])
        #  根据不同的加解密算法，走不同的分支
        #  分支1：直接将响应体的二进制内容res.content以base64算法进行解密之后转换为JSON格式返回
        if data['encoding'] == 'base64':
            return json.loads(base64.b64decode(res.content))
        #  分支2：支持的其他算法，返回解密后的响应体
        elif data['encoding'] == 'md5':
            return 'xxxxxxxxxxxxxxxxxxx'
        #  分支3：把加密过后的响应体作为参数发送给第三方服务，让第三方服务做解密，将解析后的数据返回
        elif data['encoding'] == 'private':
            return requests.post("url", data=res.content)


#  对于环境准备中的通过base64算法对demo.json加密过后的文件demo.txt里的内容进行解密
def test_encryption():
    url = 'http://127.0.0.1:9999/demo.txt'
    r = requests.get(url=url)
    print(r.text)
    # Python自带的base64模块有自带的base64解密方法b64decode()
    # res = base64.b64decode(r.content)
    # 处理成JSON格式：json.loads()
    res = json.loads(base64.b64decode(r.content))
    print("通过base64算法解密过后的内容转化为JSON格式：", res)
