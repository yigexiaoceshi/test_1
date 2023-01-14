#!/usr/bin/python3
# -*- coding:utf-8 -*-
import yaml
from selenium import webdriver
from time import sleep


class TestLoginWechat:

    def setup(self):
        self.brower = webdriver.Chrome()
        self.brower.implicitly_wait(3)

    def teardown(self):
        self.brower.quit()

    def test_get_wechat_cookies(self):
        self.brower.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.brower.maximize_window()
        # 等待十秒，人工扫码
        sleep(10)
        cookies = self.brower.get_cookies()
        print(cookies)
        with open("cookies.yaml", "w") as cookies_file:
            yaml.safe_dump(cookies, cookies_file)
        sleep(2)

    def test_add_wechat_cookies(self):
        self.brower.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        wechat_cookie = yaml.safe_load(open("cookies.yaml"))
        for i in wechat_cookie:
            self.brower.add_cookie(i)
        self.brower.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(1)
