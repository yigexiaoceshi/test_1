#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests

from interface_autotest.interface.apis.we_work import WeWork
from interface_autotest.interface.utils.file_tools import FileTools


class Department(WeWork):
    def __init__(self):
        super().__init__()  # 继承父类（及底层）所有的init方法，当前父类BaseApi无init方法，可不写
        # 调用yaml文件读取方法，读取yaml文件数据
        yaml_data = FileTools.read_yaml("secrets")
        # 从yaml文件流里获取corpid和corpsecret
        corpid = yaml_data.get("corpid").get("tester_company")
        corpsecret = yaml_data.get("corpsecret").get("department")
        # 调用父类的get_access_token方法获取access_token
        self.access_token = self.get_access_token(corpid, corpsecret)
        # print(self.access_token)

    def create_department(self, data):
        """
        创建部门
        :param data:
        :return:
        """
        # 字面量赋值的方式拼接URL
        create_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}'
        r = self.send("POST", create_url, tool="requests", json=data)
        return r

    def update_department(self, data):
        """
        更新部门
        :param data:
        :return:
        """
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}"
        r = self.send("POST", update_url, tool="requests", json=data)
        return r

    def delete_department(self, del_id):
        """
        删除部门
        :param del_id:
        :return:
        """
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id={del_id}'
        r = self.send("GET", delete_url, tool="requests")
        return r

    def get_department(self):
        """
        获取部门列表
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}'
        r = self.send("GET", url, tool="requests")
        # 返回r，不是r.json()，因为返回的不一定是JSON标准数据格式，在取值的时候灵活使用r.json()或r.text等等
        return r
