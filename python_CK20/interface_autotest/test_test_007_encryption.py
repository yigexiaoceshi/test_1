#!/usr/bin/python3
# -*- coding:utf-8 -*-

from interface_autotest import test_007_encryption
from interface_autotest import test_008_more_environment
from unittest import TestCase


class TestApiRequest(TestCase):
    # 定义请求信息
    req_data = {
        'method': 'get',
        'url': 'http://testing-studio:9999/demo.txt',
        'headers': None,
        'encoding': 'base64'
    }

    def test_send(self):
        """
        针对test_007_encryption.py里的ApiRequest类里的send方法设计的一条用例，用来验证分支1
        在send方法名上右键，选择go to，test，就会创建一个py文件，用来编写testcase
        """
        ApiRequest = test_007_encryption.ApiRequest()
        a = ApiRequest.send(self.req_data)
        print(a)

    def test_api_send(self):
        """
        针对test_008_more_environment.py里的Api类里的send方法设计的一条用例，用来验证url是否替换成功
        """
        api_request = test_008_more_environment.Api()
        b = api_request.send(self.req_data)
        print(b.text)

