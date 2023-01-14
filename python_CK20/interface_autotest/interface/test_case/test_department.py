#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys

import pytest
from jsonpath import jsonpath
import allure
import uuid

from interface_autotest.interface.apis.wechat_department import Department
from interface_autotest.interface.utils.log_utils import logger


@allure.feature("部门管理")
class TestDepartment:
    def setup_class(self):
        # 将wechat_department.py模块里的Department类实例化，对象赋值给类变量self.department
        self.department = Department()

    def get_uid(self):
        # 生成的UUID进行切割
        uid = str(uuid.uuid1()).split("-")[0]
        # 返回切割后的UUID
        return uid

    @allure.story("获取部门列表")
    def test_get_department(self):
        # 调用get_department()方法
        r = self.department.get_department()
        # assert r.json()["errcode"] == 0
        assert r.json().get("errcode") == 0

    @allure.story("创建部门")
    @pytest.mark.parametrize("name,parentid,expect1,expect2", [("交付中心", 13, 0, True), ("", 13, 40058, False)])
    def test_create_department(self, name, parentid, expect1, expect2):
        with allure.step("创建部门"):
            uid = self.get_uid()
            data = {
                "name": f"{name}_{uid}" if name else "",
                "parentid": parentid
            }
            # 调用模块方法里的创建部门方法，创建部门，传入data参数，等到一个返回的响应正文的文件流
            r = self.department.create_department(data)
            # 返回码的断言
            assert r.json().get("errcode") == expect1
            # 断言改造,调用一次获取部门列表的方法，得到json格式的响应数据体：lis为所有部门的数据
            lis = self.department.get_department().json()
            # 使用封装好的logger打印下lis
            # logger.info(lis)
            #  使用jsonpath语法提取响应体中所有的name，得到一个name的列表（得到列表，如果是复杂数据体的话，因为无法解析导致无法用in进行断言）
            # print("name的列表为：", jsonpath(lis, "$.department.[*].name"))  # 获取所有节点的name：$..name
            # 这样就可以使用string in ["string1","string2"]进行断言了
            # assert f"交付中心_{uid}" in jsonpath(lis, "$.department.[*].name")
            """使用in断言有时并不准确，可以由主键字段精准匹配得到name，断言是否相等，如下"""
            print("r.json()的值为：", r.json())
            # 从json格式的响应数据体中得到该部门ID
            department_id = r.json().get("id")
            print("所有的部门ID为：", department_id)
            #  使用jsonpath表达式，定义好条件(当id==department_id时，所有的$.department.name)，过滤表达式:[?(表达式)]，@为当前节点,一个点点表示当前节点的子节点
            department_name = f"$.department[?(@.id=={department_id})].name"
            # 在所有部门数据的响应体中，传入定义好的条件，得到该部门ID对应的部门名称name
            li = jsonpath(lis, department_name)
            print("该部门ID对应的部门名称li为", li)
            # print("jsonpath(lis, department_name)[0]为", jsonpath(lis, department_name)[0])  # 如果name为空则会报布尔类型不可下标的错：TypeError: 'bool' object is not subscriptable
            # 如果name的列表不为空
            if li:
                # assert f"{name}_{uid}" == jsonpath(lis, expr)[0]
                assert (f"{name}_{uid}" == jsonpath(lis, department_name)[0]) == expect2
            else:
                assert li == expect2

    def test_update_department(self):
        # 生成一个UUID
        uid = self.get_uid()
        create_data = {
            "name": f"交付中心_{uid}",
            "parentid": 13
        }
        # 调用模块里创建部门的方法，创建部门，传入create_data参数
        r = self.department.create_department(create_data)
        # 可先断言是否创建成功
        assert r.json().get("errcode") == 0
        # 获取已创建部门的部门ID
        dep_id = r.json().get("id")
        # 再生成一个UUID
        uid = self.get_uid()
        update_data = {
            "id": dep_id,
            "name": f"交付中心_update_{uid}"
        }
        # 调用模块里更新部门的方法，更新部门，传入update_data参数
        r = self.department.update_department(update_data)
        # 断言返回状态码
        assert r.json().get("errcode") == 0

    def test_delete_department(self):
        # 生成一个UUID
        uid = self.get_uid()
        create_data = {
            "name": f"交付中心_{uid}",
            "parentid": 13
        }
        # 调用模块里创建部门的方法，创建部门，传入create_data参数
        r = self.department.create_department(create_data)
        # 可先断言是否创建成功
        assert r.json().get("errcode") == 0
        # 获取已创建部门的部门ID
        dep_id = r.json().get("id")
        # 调用模块里删除部门的方法，删除部门，传入部门ID
        r = self.department.delete_department(dep_id)
        # 断言删除接口的返回状态码
        assert r.json().get("errcode") == 0


"""
多进程执行用例：pip install pytest-xdist
pytest -n 3 -sv XXX.py
多线程：
print()方法好像无法输出
"""
