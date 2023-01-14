#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
实现原理：发起请求之前，对请求URL进行替换：
1、需要二次封装request是，对请求进行定制化
2、将请求的结构体的URL从一个写死的IP或域名更改为任意一个域名：str(data['url']).respace(old_url,new_url)完成字符串的部分或全部替换
3、使用env配置文件，存放各个环境的配置信息
4、将请求结构体中的URL替换为配置文件中个人选择的URL，通过self.env['testing-studio']读取{'dev':'127.0.0.1','test':'127.0.0.2'}，
通过self.env['default']进一步获取IP地址对应的key
5、将env配置文件使用yaml进行管理
"""
import requests
import yaml


class Api:
    env = yaml.safe_load(open('test_008_yaml'))

    def send(self, data: dict):
        """
        1、替换url中的testing-studio为default的value就可以了，最后修改就只需要修改配置文件的default的value就可
        2、将data['url']转换成字符串，使用str.replace()方法将'testing-studio'替换为self.env['testing-studio']对应的value值，
        该value值为一个字典，进一步获取到该字典的key，通过self.env['default']得到test还是dev
        3、self.env['testing-studio'][self.env['default']]等同于self.env['testing-studio'].['dev']]
        """

        data['url'] = str(data['url']).replace('testing-studio', self.env['testing-studio'][self.env['default']])
        r = requests.request(method=data['method'], url=data['url'], headers=data['headers'])
        return r
