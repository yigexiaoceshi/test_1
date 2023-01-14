#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
三种等待：
强制等待：强制等待一段时间，time.sleep(3)
隐式等待：智能等待3秒，查找元素，一般用于时间变化波动不大时，self.brower.implicitly.wait(3)
显式等待：定义等待条件，条件发生时才会继续执行，WebDriverWait配合until()和until_not()方法一起使用，根据条件进行等待
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.brower = webdriver.Chrome()
        self.brower.get("https://ceshiren.com/")
        self.brower.implicitly_wait(3)
        self.brower.maximize_window()

    def teardown(self):
        self.brower.quit()

    def test_wait(self):
        # self.brower.find_element(By.XPATH,'//*[@title="所有分类"]').click()
        # self.brower.find_element(By.XPATH,'//*[@title="过去一年、一个月、一周或一天中最活跃的话题"]').click()
        # self.brower.find_element(By.XPATH,'//*[@id="navigation-bar"]/li[7]').click()
        self.brower.find_element(By.CSS_SELECTOR, '#navigation-bar>li:nth-child(7)').click()
        sleep(1)
        # self.brower.find_element(By.XPATH,'//*[@id="navigation-bar"]/li[2]').click()
        self.brower.find_element(By.CSS_SELECTOR, '#navigation-bar>li:nth-child(2)').click()
        sleep(1)
        print("Hello")
