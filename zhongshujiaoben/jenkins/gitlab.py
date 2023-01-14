#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from selenium import  webdriver
from time import  sleep
from jenkins.package_liucheng import *

#git参数
git_url='https://gitlab2.cspiretech.com/users/sign_in'
git_username='zhouchengjie'
git_password='yunyang@zcj'

# 添加文件下载设置，"0"禁止弹窗
option = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': '/Users/apple/Desktop'}
# 证书
option.add_argument('--ignore-certificate-errors')
# 添加一个传递给Chrome的实验性选项,name, value
option.add_experimental_option('prefs', prefs)

# 初始化chrome_options
driver03 = webdriver.Chrome(options=option)
#登录gitlab
def login_gitlab(url,username,password):
    driver03.get(url)
    driver03.implicitly_wait(10)
    driver03.find_element_by_xpath('//*[@class="form-control top"]').send_keys(username)
    sleep(1)
    driver03.find_element_by_xpath('//*[@class="form-control bottom"]').send_keys(password)
    sleep(1)
    driver03.find_element_by_xpath('//*[@class="btn btn-success"]').click()
    sleep(2)

def git_liucheng():
    #点击"projects"
    driver03.find_element_by_xpath('//*[@class="list-unstyled navbar-sub-nav"]/li[1]/button').click()
    sleep(1)
    #输入工程名
    driver03.find_element_by_xpath('//*[@class="list-unstyled navbar-sub-nav"]//li[1]//*[@class="frequent-items-dropdown-container"]//input').send_keys(j_name)
    sleep(1)
    driver03.find_element_by_xpath('//*[@class="frequent-items-item-metadata-container"]').click()
    sleep(2)

    #点击tags
    driver03.find_element_by_xpath('//*[@class="limit-container-width"]//*[@class="project-stats"]//li[3]/a').click()
    sleep(2)
    #点击"new tags"
    driver03.find_element_by_xpath('//*[@class="nav-controls"]//*[@class="btn btn-success new-tag-btn"]').click()
    sleep(2)
    #输入tag name
    driver03.find_element_by_xpath('//*[@id="tag_name"]').send_keys(new_fenzhi)
    #点击发布
    driver03.find_element_by_xpath('//*[@class="form-actions"]/button').click()
    #点击tags验证是否发布
    driver03.find_element_by_xpath('//*[@class="breadcrumbs-links js-title-container"]/ul/li[4]/a').click()
    tag_one_name=driver03.find_element_by_xpath('//*[@class="tags"]//li[1]/div[1]/a').text
    if tag_one_name == new_fenzhi:
        print("tag 发布成功！")
        sleep(5)
        driver03.quit()
    else:
        print("tag 发布失败，请查看！")


