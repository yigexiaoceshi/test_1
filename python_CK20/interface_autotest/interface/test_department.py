#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests

from interface_autotest.interface.test_get_access_token import TestGetAccessToekn
"""
在增删改查过程中，如果担心数据重复可以加入时间戳拼接
时间戳并不稳定，保证百分百不重复，可使用uuid
"""

class TestDepartment():
    def setup(self):
        self.access_token = TestGetAccessToekn().test_get_access_token()

    def teardown(self):
        pass

    def test_get_department(self):
        """
        获取所有部门列表，不需要传入部门ID
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}'
        r = requests.get(url)
        print(r.text)
        print(r.json())
        assert r.json()['errcode'] == 0
        assert r.status_code == 200

    def test_get_department_yy(self):
        """
        获取指定部门列表，须传入该部门ID
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}&id={13}'
        r = requests.get(url)
        print(r.text)
        assert r.json()['errcode'] == 0

    def test_create_department(self):
        """
        创建部门：不需要穿英文名称name_en，父部门中的次序order以及部门id（参考接口文档）
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}'
        data = {
            "name": "交付中心",
            "parentid": 13
        }
        r = requests.post(url, json=data)
        print("响应体：", r.text)
        assert r.json()['errcode'] == 0

    def test_updoate_department(self):
        """
        更新部门
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}'
        data = {
            "id": 7,
            "name": "客服中心",
            "name_en": "kfzx"
        }
        r = requests.post(url, json=data)
        print("响应体：", r.text)
        assert r.json()['errcode'] == 0

    def test_delete_department(self):
        """
        删除部门
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id=7'
        r = requests.get(url)
        print("响应体：", r.text)
        assert r.json()['errcode'] == 0
