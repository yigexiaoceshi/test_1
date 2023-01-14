#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

#使用谷歌浏览器
driver=webdriver.Chrome()
#登录接入方
driver.get("http://172.18.109.59:8080/")
driver.implicitly_wait(5)
driver.maximize_window()
sleep(2)

#登录
def login(username,password):
    #输入账号、密码
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    #点击登录按钮
    driver.find_element_by_xpath('//*[@class="ant-btn puer-Customer-form-button ant-btn-primary"]').click()
    sleep(2)


#登出
def logout():
    #点击右上角用户名
    driver.find_element_by_xpath('//*[@class="cbd-page-header-user-center-wrapper"]/div/i').click()
    #点击退出按钮
    driver.find_element_by_xpath('//*[@class="cbd-page-header-user-center-menu-wrapper"]/div[2]/span/span').click()
    sleep(2)
    # driver.quit()

