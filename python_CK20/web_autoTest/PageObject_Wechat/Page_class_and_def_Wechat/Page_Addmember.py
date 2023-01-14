#!/usr/bin/python3
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from web_autoTest.PageObject_Wechat.Page_class_and_def_Wechat.Page_Contact import TestPageContact
from web_autoTest.PageObject_Wechat.Page_class_and_def_Wechat.base_page import BasePage


# 添加员工页面：定义一个类


class TestPageAddMember(BasePage):

    # 方法1：添加员工，添加成功，跳转通讯录页面
    def add_member_success(self):
        # 输入必填项：姓名、账号、手机号，点击【保存】
        self.brower.find_element(By.ID, "username").send_keys("提莫队长15")
        self.brower.find_element(By.ID, "memberAdd_acctid").send_keys("Timo15")
        self.brower.find_element(By.ID, "memberAdd_phone").send_keys("18800000016")
        self.brower.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return TestPageContact(self.brower)
        # self.brower.find_element..  #为什么此处找不到self.brower了

    # 方法2：添加员工，点击【取消】，回到通讯录页面
    # def add_member_cancel(self):
    #
    #     return TestPageContact()
