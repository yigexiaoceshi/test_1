#!/usr/bin/python3
# -*- coding:utf-8 -*-


# 定义一个测试类
from web_autoTest.PageObject.Page_Class_and_def.IndexPage import IndexPage


class TestAddMember:

    def setup(self):
        pass

    def teardown(self):
        pass

    # 定义一个测试用例
    def test_addmember(self):
        # 获得起始页面的实例对象
        Index_test = IndexPage()
        name_list = Index_test.go_to_addmemberpage_index().add_member().get_members()
        assert "Timo" in name_list
        """
        报错解析：
        1、初始化首页，test调用首页
        2、首页调用方法跳转添加成员页面，首页调用添加成员页面，1导入3
        3、添加成员页面方法调用添加成员方法，添加成员页面调用通讯录页面，3导入2
        4、通讯录页面调用获取成员列表方法，通讯录页面调用通讯录页面，#2导入2
        """
