#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
# !/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from Customer_platform.UI.User_login.login import login, logout
from faker import Factory
from Customer_platform.UI.User_login.login import driver
import time

fake = Factory.create('zh_CN')




# 从控制台进入某个产品菜单
def topic_menu():
    # 悬浮产品菜单
    move = driver.find_element_by_xpath('//*[@class="cbd-page-header-menu-layout"]/div[2]//span')
    ActionChains(driver).move_to_element(move).perform()
    # 点击消息协同菜单
    driver.find_element_by_xpath('//*[@class="cbd-page-header-sub-menu-layout"]/div[4]/span[2]').click()
    time.sleep(1)

#topic注册
def new_topic(topicname,beizhu):
    # 点击topic注册列表
    driver.find_element_by_xpath('//*[@class="ant-menu-item-group-list"]/li[1]/span').click()
    time.sleep(1)
    # topic注册-输入topic名称
    driver.find_element_by_xpath('//*[@class="ant-spin-container"]/form/div[1]/div[2]/div/div[1]//input').send_keys(topicname)
    time.sleep(0.5)
    # 选择消息特性
    driver.find_element_by_xpath('//*[@class="ant-spin-container"]/form/div[1]/div[2]/div/div[2]//*[@class="ant-form-item-children"]//input[1]').click()
    time.sleep(0.5)
    # 选择开放订阅(下拉框)
    # 点击下拉框，弹出选项
    driver.find_element_by_xpath('//*[@class="ant-spin-container"]/form/div[1]/div[2]/div/div[3]//*[@class="ant-select ant-select-enabled"]/div/div/div').click()
    time.sleep(0.5)
    # 选择授权订阅权限选项
    driver.find_element_by_xpath('//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]/div/ul/li[2]').click()
    # 输入topic说明
    driver.find_element_by_xpath('//*[@class="ant-spin-container"]/form/div[1]/div[2]/div/div[5]//textarea').send_keys("UI自动化数据")
    #滑动至确认按钮位置
    moo=driver.find_element_by_xpath('//*[@class="ant-spin-nested-loading"]/div/div/button')
    time.sleep(0.5)
    driver.execute_script("arguments[0].scrollIntoView();",moo)
    time.sleep(0.5)
    # 点击添加子节点按钮
    driver.find_element_by_xpath('//*[@class="ant-col ant-col-2 col-item col-item-setting"]/span[2]/i').click()
    time.sleep(1)
    #输入参数名称
    driver.find_element_by_xpath('//*[@class="ant-col ant-col-9 col-item col-item-desc"]/span//input').send_keys(beizhu)
    time.sleep(0.5)
    # 点击确定按钮
    driver.find_element_by_xpath('//*[@class="ant-spin-nested-loading"]/div/div/button').click()
    time.sleep(1)
    # 关闭注册成功弹窗
    driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/button').click()
    print("topic注册成功！")
    time.sleep(1)

#我的topic
def my_topic(topicname,beizhu):
    #点击我的topic列表
    driver.find_element_by_xpath('//*[@class="ant-menu-item-group-list"]/li[4]/span').click()
    time.sleep(1)
    #topic名称查询
    driver.find_element_by_xpath('//*[@class="search-wrap"]/form/div/div[2]/div/div[2]//input').send_keys(topicname)
    time.sleep(0.5)
    #点击查询按钮
    driver.find_element_by_xpath('//*[@class="search-wrap"]/form/div/div[4]/div/button[1]').click()
    time.sleep(1)
    # 获取topiccode
    topic_code = driver.find_element_by_xpath('//*[@class="ant-table-body"]/table/tbody/tr[1]/td[2]').text
    #查询详情
    driver.find_element_by_xpath('//*[@class="ant-table-wrapper"]/div/div/div/div/div/table/tbody/tr[1]/td[7]/a[1]').click()
    time.sleep(1)
    #判断详情是否正常显示
    canshuname=driver.find_element_by_xpath('//*[@class="ant-table-body"]/table/tbody/tr[2]/td[4]').text
    time.sleep(1)
    if canshuname == beizhu:
        print("详情显示正常！")
    else:
        driver.get_screenshot_as_file('/Users/apple/PycharmProjects/zhongshujiaoben/screenshots/topic_xiangqing.png')
        print("详情显示异常！")
    #点击面包屑返回列表
    driver.find_element_by_link_text("我的Topic").click()
    time.sleep(1)
    return topic_code


#topic申请
def topic_apply(topic_code):
    #点击topic申请列表
    driver.find_element_by_xpath('//*[@class="ant-menu-item-group-list"]/li[2]/span').click()
    time.sleep(1)
    #输入topic_code
    driver.find_element_by_xpath('//*[@class="ant-row"]/div[3]/div/div[2]/div/span/input').send_keys(topic_code)
    time.sleep(0.5)
    #点击查询按钮
    driver.find_element_by_xpath('//*[@class="ant-row"]/div[4]//button[1]').click()
    time.sleep(0.5)
    #点击申请授权按钮
    driver.find_element_by_xpath('//*[@class="ant-table-body-outer"]/div/table/tbody/tr/td/a[2]').click()
    time.sleep(1)
    #输入申请方联系人
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[2]/div[2]//input').send_keys("自动化")
    time.sleep(0.3)
    #输入联系方式
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[3]/div[2]//input').send_keys("17700000000")
    time.sleep(0.3)
    #上传附件
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[4]/div[2]//input').send_keys("/Users/apple/Downloads/111.pdf")
    time.sleep(0.8)
    #输入申请理由
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[5]/div[2]//textarea').send_keys("UI自动化测试数据")
    time.sleep(0.5)
    #点击提交按钮
    driver.find_element_by_xpath('//*[@class="cbd-detail-page-card-footer"]//button[1]').click()
    time.sleep(1)




