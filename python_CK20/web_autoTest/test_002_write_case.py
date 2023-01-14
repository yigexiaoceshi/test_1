#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、官方文档介绍
"""

"""
示例：
1、打开百度
2、点击搜索框，输入霍格沃兹测试学员，点击百度一下按钮
3、在搜索结果页找到"霍格沃兹测试学员 - 主页"
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:  # 定义测试类
    def setup(self):
        # 实例化当前类，初始化浏览器
        self.brower = webdriver.Chrome()  # 加个self.之后，brewer就编程了类变量，teardown里就可以直接self.brower使用了
        # get方法打开当前网站
        self.brower.get("https://www.baidu.com")
        self.brower.implicitly_wait(3)  # 隐式等待3秒，应用于当前类，每条用例执行都有3秒的时间去寻找元素，寻找频率默认每个0.5秒

    def teardown(self):
        self.brower.close()

    def test_baidu_hogwarts(self):
        shurukuang = self.brower.find_element(By.ID, "kw")
        shurukuang.send_keys("霍格沃兹测试学院")
        baiduyixia_buttom = self.brower.find_element(By.ID, "su")
        baiduyixia_buttom.click()
        hogwarts_result = self.brower.find_element(By.LINK_TEXT, "霍格沃兹测试学院 - 主页")
        result = hogwarts_result.text
        print(result)
        assert "霍格沃兹测试学院 - 主页" in result
