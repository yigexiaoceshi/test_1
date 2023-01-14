#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
文件上传接口的一般特征：
1、请求头：Content-Type:multipart/form-data;boundary=i80fsidf0sdfs0fsfiu
2、请求头信息里有时也能看到name或file_name

文件上传接口场景：
1、指定name
2、指定filename
3、指定Content-Type
"""
import requests


def test_upload():
    # 加代理只是为了在Charles上看到请求信息
    r = requests.post('https://httpbin.ceshiren.com/post',
                      # files参数：字典格式，key为文件名，value为一个二进制文件流
                      # files={"upload_filename": open('/Users/liyong/Downloads/123.jpg',"rb")},
                      # 如果想修改filename(即123.jpg)，value可以传入2个元素的元组，第一个元素是新的filename，第二个元素是file对象
                      files={"upload_filename": ('456.jpg', open('/Users/liyong/Downloads/123.jpg', "rb"))},
                      proxies={"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888"},
                      verify=False)
    print(r.json())
