#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""TouchAction的用法"""
from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        option = webdriver.ChromeOptions()  # 找元素时提示不符合w3c标准，所以添加这三行代码，以后抽时间深究
        option.add_experimental_option("w3c", False)
        self.brower1 = webdriver.Chrome(options=option)
        self.brower1.implicitly_wait(10)
        self.brower1.maximize_window()

    def teardown(self):
        self.brower1.close()

    def test_touchaction(self):
        """
        1、打开百度
        2、输入selenium
        3、通过TouchAction点击"百度一下"按钮
        4、搜索结果页面滑动到底部，点击下一页
        5、关闭浏览器
        :return:
        """
        self.brower1.get("https://www.baidu.com")
        ele_shurukuang = self.brower1.find_element(By.ID, "kw")
        ele_baiduyixia = self.brower1.find_element(By.ID, "su")
        # 创建一个动作容器对象，里面存放这各种等待按照顺序执行的动作队列
        actions_baidu = TouchActions(self.brower1)
        # 鼠标点击输入框，定位光标到输入框
        ele_shurukuang.click()
        # 输入selenium
        ele_shurukuang.send_keys("selenium")
        # 点击"百度一下"按钮
        actions_baidu.tap(ele_baiduyixia).perform()  # 此时进入搜索结果页，下一步操作滑动到底部
        # sleep(3)
        # 我这里必须重新定义一个动作容器对象，不知道啥原因，一个容器对象只能perform()一次，理论上是可以多次
        actions_scroll = TouchActions(self.brower1)
        # 滑动到底部，传入三个参数，第一个是起始位置的元素，第二个和第三个分别是X轴和Y轴滑动的偏移量
        actions_scroll.scroll_from_element(ele_shurukuang, 0, 10000).perform()
        sleep(1)


"""
注：
理论上讲，创建一个动作容器对象，即可多次执行perform()。执行完了可再添加
比如，先添加123三个动作，执行完了1和2，剩一个3动作未执行，此时再添加动作4和5，那等待执行的动作对象就剩下345，待验证！！！！！！！1
"""
