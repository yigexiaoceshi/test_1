#!/usr/bin/python3
# -*- coding:utf-8 -*-


# 通讯录页面定义为一个类
class ContactPage:

    # 通讯录页面方法1：跳转添加成员页面
    def go_to_addmemberpage_contact(self):
        from web_autoTest.PageObject.Page_Class_and_def.AddMemberPage import AddMemberPage
        return AddMemberPage()

    # 通讯录页面方法2：获取成员列表
    def get_members(self):
        return ["Timo"]
