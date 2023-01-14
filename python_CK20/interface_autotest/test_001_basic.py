#!/usr/bin/python3
# -*- coding:utf-8 -*-
import json
import requests
from jsonpath import jsonpath
from hamcrest import *
from jsonschema import validate
# from requests_xml import XMLSession


class TestDemo():
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.json())
        print(r.text)
        print(r.status_code)
        assert r.status_code == 200

    def test_query(self):
        # 数字类型的value作为query传参时自动转为字符串类型
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        print(r.json())
        print(r.status_code)
        assert r.status_code == 200

    # def test_upload(self):
    #     files = {
    #         "file":open("path/file-name","rb")
    #     }
    #     r = requests.post("URL",files=files)
    #     print(r.text)
    #     print(r.json())
    #     print(r.status_code)
    #     assert r.status_code == 200

    def test_headers(self):
        r = requests.get("https://httpbin.testing-studio.com/get", headers={"name": "hero"})
        print(r.json())
        print(r.text)
        print(r.status_code)
        assert r.json()["headers"]["Name"] == "hero"

    # form请求：1.请求体数据量不大；2.数据结构层级不深；3.通常以键值对形式传递，Content-Type:application/x-www-form-urlencoded
    def test_post_form(self):
        #  数字类型的value作为data传参时自动转为字符串类型
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        print(r.json())
        print(r.status_code)
        print(r.cookies)
        print(r.raw.read(10))
        print(r.headers)
        print(r.encoding)
        print(r.content)
        print(r.request)
        assert r.status_code == 200

    # json请求：适用于请求体数据量可大可小，数据结构层级可深可不深，JSON格式传递
    def test_post_json(self):
        # 数字类型的value作为JSON传参时仍为数字类型
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["name"] == "seveniruby"

    # def test_xml_post(self):
    #     xml = """<?xml version='1.0' encoding='utf-8'?><a>6<a>"""
    #     headers = {'Content-Type': 'application/xml'}  # 需要手动加请求头，结构化数据类型
    #     r = requests.post("url", data=xml, headers=headers)  # 没有封装xml结构化数据，所以还是以data参数传参
    #     assert r.status_code == 200

    def test_get_json(self):
        r = requests.get('https://ceshiren.com/categories_and_latest')
        print(r.text)
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        # jsonpath表达式语法要熟悉，此处是$开头，2个点点表示中间任意层级忽略，最后一个层级的所有name
        print(jsonpath(r.json(), '$..name'))  # 返回一个列表，列表里的元素是最后一个层级的所有name
        print(r.request)
        # JSONpath语法：jsonpath(json对象,'JSONpath表达式')，第一个参数必须传入一个JSON对象才可以按照后面的表达式解析
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'

    def test_hamcrest(self):
        # hamcrest支持较为复杂的断言场景，多种断言方法需要熟练掌握
        r = requests.get('https://ceshiren.com/categories_and_latest')
        print(r.text)
        # 语法：assert_that(json对象['key'],匹配器('预期结果'))
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('开源项目'))  # equal_to('str')是否相等

    def test_get_login_jsonschema(self):
        # schema断言理解：手动或自动生成一个schema数据格式文件，类似于模板(定义好数据格式长短等)，下次运行对比上次作为参考是否发生改变
        url = 'https://testerhome.com/api/v3/topics.json'
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open('topic_schema.json'))
        validate(data, schema=schema)
