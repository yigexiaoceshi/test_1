#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Customer_platform.UI.User_login.login import login,logout
from Customer_platform.UI.User_login.login import driver
from faker import Factory
import time


fake=Factory.create('zh_CN')

requestTime = int(round(time.time() * 1000))
# print(requestTime)
aaa = int(time.time())


#从控制台进入某个产品菜单
def menu():
    #悬浮产品菜单
    move=driver.find_element_by_xpath('//*[@class="cbd-page-header-menu-layout"]/div[2]//span')
    ActionChains(driver).move_to_element(move).perform()
    #点击业务协同
    driver.find_element_by_xpath('//*[@class="cbd-page-header-sub-menu-layout"]/div[2]/span[2]').click()
    time.sleep(2)

#系统接入
def new_system(name):
    #点击系统接入菜单
    driver.find_element_by_xpath('//*[@class="ant-menu-item-group-list"]/li[2]').click()
    time.sleep(0.5)
    #点击新增系统
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div/div/button').click()
    time.sleep(0.5)
    #输入系统名称
    driver.find_element_by_xpath('//*[@class="ant-modal-body"]//*[@class="ant-form ant-form-horizontal"]/div[1]/div[2]//input').send_keys(name)
    #输入系统唯一编码
    driver.find_element_by_xpath('//*[@class="ant-modal-body"]//*[@class="ant-form ant-form-horizontal"]/div[2]/div[2]//input').send_keys(aaa)
    #选择请求协议（选择http）
    driver.find_element_by_xpath('//*[@class="ant-modal-body"]//*[@class="ant-form ant-form-horizontal"]/div[3]//*[@class="ant-form-item-children"]/div/label[1]/span[1]').click()
    #输入IP地址
    driver.find_element_by_xpath('//*[@class="ant-modal-body"]//*[@class="ant-form ant-form-horizontal"]/div[5]/div/div[2]//input').send_keys(fake.ipv4(network=False))
    #输入系统说明
    driver.find_element_by_xpath('//*[@class="ant-modal-body"]//*[@class="ant-form ant-form-horizontal"]/div[6]/div[2]//textarea').send_keys("测试数据"+str(aaa))
    #点击确认按钮
    driver.find_element_by_xpath('//*[@class="ant-modal-body"]//*[@class="ant-form ant-form-horizontal"]/div[7]//button[1]').click()
    time.sleep(1)
    #判断是否提交成功
    nnn=driver.find_elements_by_xpath('//*[@class="ant-message"]//*[@class="ant-message-notice-content"]')
    # print(nnn)
    if nnn ==[]:
        driver.get_screenshot_as_file('/Users/apple/PycharmProjects/zhongshujiaoben/screenshots/sys.png')
        print("新增失败！已截图sys.png")

#子系统查询
def query(sysname):
    #列表-系统名称查询
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div/div[1]/div/div[2]//input').send_keys(sysname)
    time.sleep(0.5)
    #点击查询按钮
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div/div[2]/div/button[1]').click()
    time.sleep(2)
    #验证信息是否正确
    name=driver.find_element_by_xpath('//*[@class="ant-table-body"]//tbody/tr/td[2]/span').text
    if name==sysname:
        print("列表找到新增系统，创建系统验证通过！")
    else:
        print("创建系统验证失败！")


if __name__ == '__main__':
    #创建系统名称
    sys_name="UI自动化数据"+str(aaa)
    try:
        # 登录接入方平台
        login("zhouwenfeng","Aa123456")
        # 进入菜单
        menu()
        # 新增系统
        new_system(sys_name)
        #子系统查询
        query(sys_name)
    finally:
        driver.quit()