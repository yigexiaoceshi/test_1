#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Customer_platform.UI.User_login.login import login,logout
from Customer_platform.UI.User_login.login import driver
from Customer_platform.UI.Topic_together.New_topic import topic_menu
from faker import Factory
import time

fake=Factory.create('zh_CN')

requestTime = int(round(time.time() * 1000))
# print(requestTime)
aaa = int(time.time())



#从控制台进入某个产品菜单
def api_menu():
    #悬浮产品菜单
    move=driver.find_element_by_xpath('//*[@class="cbd-page-header-menu-layout"]/div[2]//span')
    ActionChains(driver).move_to_element(move).perform()
    #点击业务协同
    driver.find_element_by_xpath('//*[@class="cbd-page-header-sub-menu-layout"]/div[2]/span[2]').click()
    time.sleep(2)

#自建API-基本信息
def new_api(apiname,bianma):
    #点击自建API菜单
    driver.find_element_by_xpath('//*[@class="ant-menu-item-group-list"]/li[1]').click()
    time.sleep(1)
    #点击新增API
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div[1]/div/div[2]/button').click()
    time.sleep(1)
    #输入API名称
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div[1]/div[1]/div[2]//span/input').send_keys(apiname)
    #输入接入方API编码
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div[2]/div[1]/div[2]//span/input').send_keys(bianma)
    #点击选择系统选项
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/span').click()
    time.sleep(0.5)
    #选择所属系统
    driver.find_element_by_xpath('//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]/div/ul/li[1]').click()
    time.sleep(0.5)
    #输入API说明
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div[2]/div[4]/div[2]/div/span/textarea').send_keys(fake.ean8())
    time.sleep(0.5)
    #输入版本号
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div[2]//input').send_keys("1.0")
    time.sleep(0.5)
    #输入联络人
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div[1]/div[4]/div[2]//input').send_keys("UI自动化周一")
    time.sleep(0.5)
    #输入联络电话
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div[1]/div[5]/div[2]//input').send_keys("17757565001")
    time.sleep(0.5)
    #点击下一步
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[1]/div/div/div/button').click()
    time.sleep(1)

#自建API-API配置
def new_api_configuration(dataname):
    #输入API访问路径
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div[1]/div[2]//input').send_keys("/sjzyj/zjhz/sjjsfzhcxjkmxx")
    time.sleep(0.5)
    #选择请求方式
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div[2]/div[2]/div//div[1]').click()
    time.sleep(0.5)
    #选择post
    driver.find_element_by_xpath('//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]//li[2]').click()
    time.sleep(0.5)

    #点击form按钮
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/label[1]//input').click()
    #输入入参信息-点击query参数按钮
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/div/div[1]/div[2]/div/div[2]/div[2]//button').click()
    time.sleep(0.5)
    #输入参数名称
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/input').send_keys("ui自动化")
    time.sleep(0.5)
    #输入参数示例
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div[4]/textarea').send_keys("自动化测试数据")
    time.sleep(0.5)
    #输入备注信息
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div[5]/textarea').send_keys("测试备注")

    #滑动到下一步位置
    abc = driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/div/button[2]')
    time.sleep(0.5)
    driver.execute_script("arguments[0].scrollIntoView();", abc)

    #输入出参信息-点击"➕"往data新增子节点
    svg=driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/div/div[2]/div[2]//*[@class="schema-content"]/div/div[4]/div[1]/div[5]/i')
    ActionChains(driver).move_to_element(svg).perform()
    time.sleep(0.5)
    #点击子节点按钮
    driver.find_element_by_xpath('//*[@class="ant-dropdown ant-dropdown-placement-bottomLeft"]//*[@class="ant-dropdown-menu-item"]').click()
    time.sleep(0.5)
    #输入参数名称
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/div/div[2]/div[2]//*[@class="schema-content"]/div/div[4]/div[2]/div/div/div[1]/div[3]//input').send_keys(dataname)
    time.sleep(0.5)
    #输入备注
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/div/div[2]/div[2]//*[@class="schema-content"]/div/div[4]/div[2]/div/div/div[1]/div[4]//input').send_keys("测试备注")
    time.sleep(0.5)
    #点击下一步
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[2]/div/button[2]').click()
    time.sleep(1)


#访问限制
def new_apilimit(apiname):
    #输入最大QPS
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[3]/form/div/div[1]/div[2]/div/div[1]/div/div[2]//input').send_keys(100)
    time.sleep(0.5)
    #输入缓存时间
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[3]/form/div/div[1]/div[2]/div/div[5]//input').send_keys(200)
    time.sleep(0.5)
    #点击下一步按钮
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[3]/div/button[2]').click()
    time.sleep(1)

    #滑动至发布按钮位置
    moob=driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[4]/div[7]/button[2]')
    time.sleep(0.5)
    driver.execute_script("arguments[0].scrollIntoView();",moob)
    #点击发布按钮
    driver.find_element_by_xpath('//*[@class="cbd-page-card-wrapper"]/div/div/div[2]/div[4]/div[7]/button[2]').click()
    time.sleep(1)
    #API列表拿到所有数据的API名称
    detail_all=driver.find_elements_by_xpath('//*[@class="ant-table-scroll"]//*[@class="ant-table-tbody"]/tr/td[2]/span')
    time.sleep(1)
    for i in detail_all:
        # print(i.text)
        if i.text ==apiname:
            print("列表找到新增API，自建API验证通过！")
            time.sleep(2)
            break
        else:
            driver.get_screenshot_as_file('/Users/apple/PycharmProjects/zhongshujiaoben/screenshots/api.png')
            print("自建API失败！已截图api.png")

#自建API列表-查询/进入详情
def api_detail(apiname,dataname,bianma):
    #获取当前窗口句柄
    handle=driver.current_window_handle
    #点击自建API菜单
    driver.find_element_by_xpath('//*[@class="ant-menu-item-group-list"]/li[1]').click()
    time.sleep(0.5)
    #API列表拿到所有数据,一整条
    detail_all=driver.find_elements_by_xpath('//*[@class="ant-table-scroll"]//*[@class="ant-table-tbody"]/tr')
    time.sleep(1)
    #循环遍历列表数据
    for i in detail_all:
        #列表中匹配与创建APi名称一致的数据
        if  str(apiname) in i.find_element_by_css_selector('td:nth-child(2)').text:
            time.sleep(1)
            #在搜索栏-查询创建API编码
            driver.find_element_by_css_selector('[class="cbd-page-card-wrapper"] [class="ant-form ant-form-horizontal"]>div>div:nth-child(2)>div>div:nth-child(2) span>input').send_keys(bianma)
            time.sleep(0.5)
            #点击查询按钮
            driver.find_element_by_css_selector('[class="cbd-page-card-wrapper"] [class="ant-form ant-form-horizontal"]>div>div:nth-child(6) button:nth-child(1)').click()
            time.sleep(1)
            #点击详情按钮，默认进入第一条数据child(1)
            driver.find_element_by_css_selector('[class="ant-table-fixed-right"] [class="ant-table-tbody"]>tr:nth-child(1)>td>a').click()
            time.sleep(1)
            break

    #获取当前两个网页句柄
    handles=driver.window_handles
    #对窗口进行遍历
    for newhandle in handles:
        if newhandle != handle:
            #切换至详情窗口
            driver.switch_to.window(newhandle)
            time.sleep(1)
            #判断详情中数据与创建的数据是否匹配
            #点击data展开按钮
            driver.find_element_by_xpath('//*[@class="simplebar-content"]/div/div/div/div/div/div[4]//*[@class="ant-table-body"]/table/tbody/tr[4]//div').click()
            time.sleep(1)
            #获取新增字段参数名称
            can_name=driver.find_element_by_xpath('//*[@class="simplebar-content"]/div/div/div/div/div/div[4]//*[@class="ant-table-body"]/table/tbody/tr[5]/td[4]/span').text
            if dataname == can_name:
                print("详情验证通过！")
                time.sleep(2)
                #关闭当前详情页面
                print("关闭详情页")
                time.sleep(1)
                driver.close()
                #切换至主页面
                driver.switch_to.window(handles[0])
                time.sleep(1)
            else:
                driver.get_screenshot_as_file('/Users/apple/PycharmProjects/zhongshujiaoben/screenshots/api_xiangqing.png')
                print("详情验证失败！已截图api.png")
                # 关闭当前详情页面
                print("关闭详情页")
                time.sleep(1)
                driver.close()
                # 切换至主页面
                driver.switch_to.window(handles[0])
                time.sleep(1)

#全部API-申请授权
def all_api(apiname):
    #点击全部API菜单
    driver.find_element_by_xpath('//*[@class="ant-menu-item-group-list"]/li[3]').click()
    time.sleep(1)
    #输入"账号一创建API-API名称"
    driver.find_element_by_xpath('//*[@class="ant-tabs-content ant-tabs-content-animated ant-tabs-top-content"]/div[1]/div[2]//*[@class="ant-row"]/div[2]/div/div[2]/div/span/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="ant-tabs-content ant-tabs-content-animated ant-tabs-top-content"]/div[1]/div[2]//*[@class="ant-row"]/div[2]/div/div[2]/div/span/div/div//input').send_keys(apiname)
    time.sleep(1)
    #点击模糊搜索项
    driver.find_element_by_xpath('//*/body/div[3]/div/div/div/ul/li[1]').click()
    time.sleep(1)
    #点击查询按钮
    driver.find_element_by_xpath('//*[@class="ant-tabs-content ant-tabs-content-animated ant-tabs-top-content"]/div[1]/div[2]//*[@class="ant-row"]/div[8]//button[1]').click()
    time.sleep(1)
    #点击申请授权按钮
    driver.find_element_by_xpath('//*[@class="ant-tabs-content ant-tabs-content-animated ant-tabs-top-content"]/div[1]/div[2]/div[1]/div[2]//*[@class="ant-table-fixed-right"]//*[@class="ant-table-tbody"]/tr[1]/td/a[2]').click()
    time.sleep(1)
    #进入申请提交页面-输入申请方联系人
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[3]//input').send_keys("UI自动化")
    time.sleep(0.5)
    #输入联系方式
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[4]//input').send_keys("17700000001")
    time.sleep(0.5)
    #点击上传文件
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[6]//input').send_keys("/Users/apple/Downloads/111.pdf")
    time.sleep(1)
    #输入申请理由
    driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[7]//textarea').send_keys("ui自动化数据")
    time.sleep(1)
    #点击提交按钮
    driver.find_element_by_xpath('//*[@class="ant-card-body"]/div/div/div[3]/button[1]').click()
    time.sleep(2)


if __name__ == '__main__':
    #创建API名称
    api_name="api名称"+str(aaa)
    #API编码
    bian_ma=fake.ean8()
    #创建API-data节点参数名称
    data_name="测试"+str(aaa)
    try:
        # 登录接入方平台
        login("zhouwenfeng","Zhouchengjie123")
        # 进入菜单
        api_menu()
        #创建API
        new_api(api_name,bian_ma)
        #创建API配置
        new_api_configuration(data_name)
        #创建API访问限制
        # new_apilimit(api_name)
        #自建API列表搜索查询及进入详情页
        # api_detail(api_name,data_name,bian_ma)
        #退出当前账号
        # logout()
        #登录第一个账号
        # Customer("Kobe","Aa123456")
        #进入全部API菜单
        # all_api(api_name)
    finally:
        # 关闭系统
        print("111")
        # driver.quit()



