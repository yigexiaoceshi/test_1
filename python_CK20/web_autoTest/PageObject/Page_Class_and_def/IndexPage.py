#!/usr/bin/python3
# -*- coding:utf-8 -*-


# 企业微信首页，定义一个类
from web_autoTest.PageObject.Page_Class_and_def.AddMemberPage import AddMemberPage
from web_autoTest.PageObject.Page_Class_and_def.ContactPage import ContactPage


class IndexPage:
    # 企业微信首页方法1：跳转到通讯录页面，返回通讯录页面类的实例
    def go_to_contactpage(self):
        return ContactPage()

    # 企业微信首页方法2：跳转添加成员页面，返回添加成员页面类的实例
    def go_to_addmemberpage_index(self):
        return AddMemberPage()
