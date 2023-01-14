#!/usr/bin/python3
# -*- coding:utf-8 -*-


# 添加成员页面定义一个类
from web_autoTest.PageObject.Page_Class_and_def.ContactPage import ContactPage


class AddMemberPage:

    # 添加成员页面方法1：添加成员流程成功，返回通讯录页面
    def add_member(self):
        return ContactPage()

    # 添加成员页面方法2：点击取消，返回通讯录页面
    def go_to_contactpage(self):
        return ContactPage()
