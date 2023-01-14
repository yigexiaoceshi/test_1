#!/usr/bin/python3
# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from web_autoTest.PageObject_Wechat.Page_class_and_def_Wechat.base_page import BasePage


# 通讯录页面，定义一个类

class TestPageContact(BasePage):

    # 方法1：点击【添加成员】，跳转添加成员页面
    def contact_go_to_addmemberpage(self):
        """
        1、因为在PageAddMember页面导入了PageContact，所以这里不能再循环导入，解决办法有用到PageAddMember里方法的方法，导入操作
        方在方法体里面
        :return:
        """
        from web_autoTest.PageObject_Wechat.Page_class_and_def_Wechat.Page_Addmember import \
            TestPageAddMember
        return TestPageAddMember()

    # 方法2：当前页面获取成员列表信息，返回具体列表数据
    def get_members(self):
        member_lists = self.brower.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
        print(member_lists)
        phone_list = []
        for i in member_lists:
            phone_list.append(i.text)
        print(phone_list)
        sleep(3)
        return phone_list
