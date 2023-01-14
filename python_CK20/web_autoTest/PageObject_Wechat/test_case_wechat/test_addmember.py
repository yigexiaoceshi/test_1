#!/usr/bin/python3
# -*- coding:utf-8 -*-
from web_autoTest.PageObject_Wechat.Page_class_and_def_Wechat.Page_Home import TestPageHome


class TestAddMember():

    def setup(self):
        pass

    def teardown(self):
        pass

    # 测试用例1：添加成员正常流程
    def test_add_member(self):
        # 导入起始页面Page_Home模块，引用里面的class和def，必须在最上一层的package开始导入
        # 实例化一个首页对象
        page_home = TestPageHome()
        # 调用首页方法2（点击添加成员按钮，跳转添加成员页面），返回PageAddMember()，所以可以链式调用，直到获取到成员列表数据，赋值
        phone_list = page_home.home_go_to_addmemberpage().add_member_success().get_members()
        print(phone_list)
        # 断言
        assert "name_list" in phone_list
