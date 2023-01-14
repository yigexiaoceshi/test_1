#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os

from selenium import webdriver


class BaseSelenium:
    def setup(self):
        """
        针对命令行使用，前面加上参数:browers=firefox pytest test_008_windows_frame.py::TestFrame::test_frame
        :return:
        """
        brower = os.getenv("browers")  # 返回环境变量键的值（字符串），否则返回默认值
        if brower == "firefox":
            self.brower = webdriver.Firefox()
        elif brower == "headless":
            self.brower = webdriver.PhantomJS()
        else:
            self.brower = webdriver.Chrome()
        self.brower.maximize_window()
        self.brower.implicitly_wait(10)

    def teardown(self):
        self.brower.quit()
