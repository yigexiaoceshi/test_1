#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、当前脚本结合mitmproxy、mitmweb、mitmdump使用，主要结合mitmdump使用
2、使用方法：mitmdump -p 8989 -s python脚本的绝对路径，将脚本加载并开启监听服务
"""
from mitmproxy import http

"""
1、方法的名字request是固定的写法，使用mitmdump加载当前模块（通过-s参数）后，只要发生了请求，就会自动调用request方法，并将请求信息传入request方法
2、flow是mitmdump拦截到的http的请求流，通过flow.request可以对拦截到的请求数据进行篡改
"""


def request(flow: http.HTTPFlow):
    # 定义请求头信息里的myheader的value为Hello，当key值myheader不存在时则新增
    flow.request.headers['myheader'] = 'Hello'
    # 打印所有的请求头信息
    print(flow.request.headers)


"""
1、方法名字response是固定写法，使用mitmdump加载当前模块（通过-s参数）后，只要有拦截到响应，就会自动调用response方法，并将响应信息传入response方法
2、flow是mitmdump拦截到的http的请求刘，通过flow.response可以抓对拦截到的响应数据进行篡改
"""


def response(flow: http.HTTPFlow):
    flow.response.json()
