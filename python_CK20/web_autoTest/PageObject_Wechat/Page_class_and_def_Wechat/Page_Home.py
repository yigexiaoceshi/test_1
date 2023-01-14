#!/usr/bin/python3
# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from web_autoTest.PageObject_Wechat.Page_class_and_def_Wechat.Page_Addmember import TestPageAddMember
from web_autoTest.PageObject_Wechat.Page_class_and_def_Wechat.Page_Contact import TestPageContact
from web_autoTest.PageObject_Wechat.Page_class_and_def_Wechat.base_page import BasePage


# 企业微信首页：定义一个类
class TestPageHome(BasePage):

    # 方法1：点击通讯录，跳转通讯录页面
    def go_to_contactpage(self):
        return TestPageContact()

    # 方法2：点击【添加成员】按钮，跳转添加成员页面
    def home_go_to_addmemberpage(self):
        # 点击【添加成员】，跳转添加成员页面
        self.brower.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        sleep(2)
        return TestPageAddMember(self.brower)
