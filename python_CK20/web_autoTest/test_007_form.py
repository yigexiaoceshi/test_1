#!/usr/bin/python3
# -*- coding:utf-8 -*-
""""
表单：在一个form表单里的所有元素，提交的时候会一起提交到服务端进行请求
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm:
    def setup(self):
        self.brower = webdriver.Chrome()
        self.brower.maximize_window()
        self.brower.implicitly_wait(3)

    def teardown(self):
        self.brower.close()

    def test_form(self):
        self.brower.get("https://testerhome.com/account/sign_in/")
        login_name = self.brower.find_element(By.ID, "user_login")
        login_name.send_keys("这是获取到的输入的登录用户名")
        print(login_name.get_property("value"))  # 获取输入的值
        login_password = self.brower.find_element(By.ID, "user_password")
        login_password.send_keys("这是获取到的输入的登录密码")
        print(login_password.get_property("value"))
        self.brower.find_element(By.XPATH, '//*[@id="new_user"]/div[3]/div/label').click()
        self.brower.find_element(By.XPATH, '//*[@id="new_user"]/div[4]/input')  # 这里就不点击了，因为密码账号是错的
        sleep(1)
