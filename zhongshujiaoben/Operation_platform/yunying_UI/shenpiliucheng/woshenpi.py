#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

#添加文件下载设置，"0"禁止弹窗
option = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': '/Users/apple/Desktop'}
#添加一个传递给Chrome的实验性选项,name, value
option.add_experimental_option('prefs', prefs)

#初始化chrome_options
driver = webdriver.Chrome(options=option)
# driver.get("http://standard.cspiretech.com:30038")
driver.maximize_window()
#设置隐式等待
driver.implicitly_wait(5)
#登录运营平台
# def user_login(url,username,password):
driver.get("http://standard.cspiretech.com:30038")
sleep(2)
driver.find_element_by_id("username").send_keys('api')
driver.find_element_by_id("password").send_keys('Aa123456')
driver.find_element_by_tag_name("button").click()
sleep(3)

#我审批-API审批
driver.find_element_by_xpath('//*[@class="cbd-page-side-bar-wrapper"]/ul/li[5]//*[@class="cbd-page-side-bar-menu-item"]').click()
#选择申请类型
driver.find_element_by_xpath('//*[@class="ant-form ant-form-inline"]/div[1]/div[3]//*[@class="ant-col ant-form-item-control-wrapper"]/div').click()
driver.find_element_by_xpath('//*[@id="root"]/following-sibling::div[2]//ul/li[1]').click()
#输入申请单号查询
driver.find_element_by_xpath('//*[@class="ant-form ant-form-inline"]/div[1]/div[1]//input').send_keys(1120201130000001)
driver.find_element_by_xpath('//*[@class="ant-form ant-form-inline"]/div[2]/button[1]').click()
sleep(2)
#点击审批按钮
driver.find_element_by_xpath('//*[@class="ant-table-fixed-right"]//button').click()
sleep(2)
#判断审批详情数据是否展示
list01=driver.find_element_by_xpath('//*[@class="ant-drawer-content-wrapper"]//*[@class="ant-row"]/div/div[2]').text
# list02 = [i.text for i in list01]
if list01=='1120201130000001':
    print("详情正常显示")
else:
    print("详情有问题")
    driver.get_screenshot_as_file("/Users/apple/Desktop/测试附件/API详情_png.png")
#查看附件
driver.find_element_by_link_text("查看附件").click()
sleep(2)
#点击返回
driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/div/button').click()
sleep(2)
#点击下载附件
driver.find_element_by_link_text("下载附件").click()
sleep(2)
#查看详情
driver.find_element_by_xpath('//*[@class="ant-drawer-body"]//*[@class="ant-table-fixed-right"]//*[@class="ant-table-tbody"]//a').click()
sleep(2)
#判断详情标识
list02=driver.find_element_by_xpath('//*[@id="root"]/following-sibling::div[4]//*[@class="label-item-wrapper"]/span').text
print(list02)
#点击关闭抽屉弹窗
driver.find_element_by_xpath('//*[@id="root"]/following-sibling::div[4]//*[@class="ant-drawer-header-no-title"]/button').click()
# #点击不通过按钮
# driver.find_element_by_xpath('//*[@class="ant-drawer-body"]//button[1]').click()
# #不通过弹窗
# driver.find_element_by_xpath('//*[@class="ant-modal-body"]//*[@class="ant-form-item-children"]/textarea').send_keys("测试不通过")
# driver.find_element_by_xpath('//*[@class="ant-modal-body"]//button[1]').click()
sleep(2)
#关闭浏览器
# driver.get_screenshot_as_file("")
driver.quit()