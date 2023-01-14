#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import  sleep
from jenkins.tk import  *
import sys
import time



def login_jenkins(url,username,password):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("-------------登录Jenkins平台-------------")
    print("----------------------------------------")
    driver01.get(url)
    sleep(2)
    driver01.find_element_by_xpath('//*[@id="loginIntroDefault"]/following-sibling::form/div[1]/input').send_keys(username)
    driver01.find_element_by_xpath('//*[@id="loginIntroDefault"]/following-sibling::form/div[2]/input').send_keys(password)
    driver01.find_element_by_xpath('//*[@id="loginIntroDefault"]/following-sibling::form/div[3]').click()
    driver01.implicitly_wait(5)
    driver01.maximize_window()
    # driver01.minimize_window()


def jenkins_package(package_name,tags_name):
    #输入工程名
    driver01.find_element_by_xpath('//*[@id="searchform"]/input').send_keys(package_name)
    #回车
    driver01.find_element_by_xpath('//*[@id="searchform"]/input').send_keys(Keys.ENTER)

    panduan=driver01.find_element_by_xpath('//*[@id="page-body"]//*[@id="main-panel"]/h1').text
    # print("获取页面提示：" +panduan)
    if "查找" in panduan:
        print("找不到该工程，请检查工程名是否存在或是否存在空格！")
        sleep(2)
        driver01.quit()
        sys.exit("脚本终止")
    else:
        print("---------进入" + package_name + "工程---------")


    #点击"Build with Parameters"
    sleep(2)
    driver01.find_element_by_xpath('//*[@id="page-body"]/div[1]/div[1]/div[4]/a[2]').click()
    sleep(2)
    # 定位分支
    tags=driver01.find_elements_by_xpath('//*[@class="parameters"]/tbody[1]//*[@class="setting-main"]/div[1]/select/option')
    sleep(2)
    # print(tags)
    # Select(tag).select_by_visible_text('origin/featrue-fc-20201211')
    #-------------------------------------------
    #选择分支
    origin="origin/"
    # print(origin + tags_name)
    for i in tags:
        try:
            if origin+tags_name  == i.text:
             i.click()
        except:
            print("找不到该分支，请检查！")
            driver01.quit()
            sys.exit()

    #获取列表所有版本号
    banbenhao=driver01.find_elements_by_xpath('//*[@class="pane stripped"]/tbody//*[@class="pane desc indent-multiline zws-inserted"]')
    list1 = []
    qwe=bbb()
    www=ssss()
    #判断当前是否存在该版本号
    for i in banbenhao:
        # print(qwe)
        # print(i.text)
        if qwe in i.text:
            list1.append(i.text)
    #如果没有该版本号，默认添加一个版本号
    if list1==[]:
        list1.append(www+str(0))
        # else:
        #     list1.append(www+str(0))
        #     break
    # print(list1)


    list2=[]
    for one in list1:
        #每获取一个版本号就切片一次
        test_fenzhi=one.split('.')[2:]
        # print(test_fenzhi)
        #list转成str
        zhuanhuan=(','.join(test_fenzhi))
        # print(zhuanhuan)
        list2.append(zhuanhuan)
    # print(list2)
    #str转换int
    results = (map(int, list2))
    # print(results)
    #版本递增+1
    max_num=max(results)+1
    #拼接选择的版本号
    new_fenzhi=ssss()+str(max_num)

    #输入版本号
    print("输入版本号为："+new_fenzhi)
    driver01.find_element_by_xpath('//*[@class="parameters"]/tbody[2]//*[@name="parameter"]/input[2]').send_keys(new_fenzhi)
    sleep(2)
    #选择环境
    banben=driver01.find_element_by_xpath('//*[@class="parameters"]/tbody[3]//select')
    Select(banben).select_by_value("prod")
    print("****************开始打包*****************")
    sleep(1)
    print(".")
    #点击开始构建
    driver01.find_element_by_xpath('//*[@class="parameters"]/tbody[4]//button').click()
    print("..")
    sleep(1)

    #获取当前工程的序号
    id=driver01.find_elements_by_xpath('//*[@class="pane stripped"]//*[@class="build-icon"]/following-sibling::a[1]')
    list_id=[]
    for i in id:
        nn=i.text
        #切片后半部分内容
        mm=nn.split('#')[1:]
        #list转str
        zhuanhuan01 = ','.join(mm)
        list_id.append(zhuanhuan01)
    #str转int
    results01=(map(int,list_id))
    max_num01=max(results01)
    # print(max_num01)
    #所有标签
    all_xuhao=driver01.find_elements_by_xpath('//*[@class="pane stripped"]//tr')
    #寻找当前编号
    for i in all_xuhao:
        if str(max_num01) in i.find_element_by_xpath('//*[@class="pane build-name"]/a').text:
            while True:
                print("---------------打包监控中----------------")
                table=i.find_elements_by_xpath('//*[@class="pane stripped"]//tr[2]//*[@class="pane build-details"]/table')
                if table==[] and "成功" in i.find_element_by_xpath('//*[@class="pane stripped"]//tr[2]//*[@class="build-status-link"]/img').get_attribute("title"):
                    print("***********打包成功***********OK，关闭Jenkins页面。")
                    sleep(2)
                    print("即将进入rancher平台部署")
                    break
                elif  table==[] and  "失败" in i.find_element_by_xpath('//*[@class="pane stripped"]//tr[2]//*[@class="build-status-link"]/img').get_attribute("title"):
                    print("***********打包失败***********请检查后重试！")
                    driver01.quit()
                    sys.exit("脚本终止")
        break
    return  new_fenzhi




def login_rancher(url,username,password,rancher_name):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("-----登录"+rancher_name+"rancher平台-----")
    print("----------------------------------------")
    #进入rancher平台发布
    driver02.get(url)
    sleep(3)
    driver02.maximize_window()
    #用户名、密码
    driver02.find_element_by_xpath('//*[@id="application"]//*[@class="row ember-view"]/form/div[1]/div[2]/input').send_keys(username)
    sleep(1)
    driver02.find_element_by_xpath('//*[@id="application"]//*[@class="row ember-view"]/form/div[2]/div/input').send_keys(password)
    sleep(1)
    #点击登录
    driver02.find_element_by_xpath('//*[@class="text-center"]/button').click()
    driver02.implicitly_wait(10)


def bushu(package_name,jenkins_package):
    #点击全局
    driver02.find_element_by_xpath('//*[@class="clip"]/span').click()
    sleep(2)
    #寻找版本项
    xunzhaoxiang=driver02.find_elements_by_xpath('//*[@class="list-unstyled no-hover-entry"]/li/a')
    a=0
    for i in xunzhaoxiang:
        # print(i.text)
        if a<len(xunzhaoxiang):
            if "api" in i.text:
                # 悬停test项
                ActionChains(driver02).move_to_element(i).perform()
                sleep(2)
            elif "hz-zs-demo" in i.text:
                # 悬停演示环境项
                ActionChains(driver02).move_to_element(i).perform()
                sleep(3)
        elif a == len(xunzhaoxiang):
            print("找不到环境选择项，请检查是否被更换")
            sleep(2)
            driver02.quit()
            sys.exit("找不到环境，异常")
        a=a+1


    #点击default选项
    sleep(1)
    driver02.find_element_by_xpath('//*[@class="projects"]//li[1]').click()
    sleep(2)
    #输入工程名
    driver02.find_element_by_xpath('//*[@class="pull-right search-group input-group"]/input').send_keys(package_name)
    sleep(2)
    #回车
    driver02.find_element_by_xpath('//*[@class="pull-right search-group input-group"]/input').send_keys(Keys.ENTER)
    print("----------进入"+package_name+"工程-----------")
    sleep(2)
    #获取当前搜索列表的工程名
    all_name=driver02.find_elements_by_xpath('//*[@class="group-row"]/following-sibling::tr[1]')
    #判断当前列表是否存在工程
    for i in all_name:
        if package_name in i.find_element_by_css_selector('[data-title="名称: "]').text:
            i.find_element_by_css_selector('[data-title="操作: "]').click()
            sleep(2)
    #点击操作栏编辑按钮
    driver02.find_element_by_xpath('//*[@id="ember-basic-dropdown-wormhole"]/div//li[2]/a/span').click()
    sleep(2)
    #文件名变量
    qianzui='harbor.yunyang.com.cn/standard/'+package_name+":"+jenkins_package
    print("更新后版本号为："+package_name+":"+jenkins_package)
    #输入文件名
    driver02.find_element_by_xpath('//*[@class="clearfix"]//*[@class="header clearfix"]/following-sibling::div[2]//input').clear()
    driver02.find_element_by_xpath('//*[@class="clearfix"]//*[@class="header clearfix"]/following-sibling::div[2]//input').send_keys(qianzui)
    sleep(3)
    #点击发布
    print("提交---------------发布中")
    driver02.find_element_by_xpath('//*[@class="clearfix"]/form/div[6]/button[1]').click()
    sleep(2)
    #判断是否部署成功
    while True:
        # print(i.text)
        if  "error" in  driver02.find_element_by_xpath('//*[@class="progress"]//div[1]').get_attribute("class"):
            print("正在初始化...")
            sleep(2)
            continue
        elif "info" in driver02.find_element_by_xpath('//*[@class="progress"]//div[1]').get_attribute("class"):
            print("正在部署中...")
            sleep(2)
        elif  "success" in  driver02.find_element_by_xpath('//*[@class="progress"]//div[1]').get_attribute("class"):
                print("服务部署完成")
                break
        elif  "error" in  driver02.find_element_by_xpath('//*[@class="progress"]//div[1]').get_attribute("class") and "100%" in  driver02.find_element_by_xpath('//*[@class="progress"]//div[1]').get_attribute("style"):
            print("部署失败")
            break

# git参数
git_url = 'https://gitlab2.cspiretech.com/users/sign_in'
git_username = 'zhouchengjie'
git_password = 'yunyang@zcj2021'


# 登录gitlab
def login_gitlab(url, username, password):
    print("即将进入gitlab发布tag!")
    sleep(2)
    driver03.get(url)
    print("登录gitlab")
    driver03.maximize_window()
    driver03.implicitly_wait(10)
    driver03.find_element_by_xpath('//*[@class="form-control top"]').send_keys(username)
    sleep(1)
    driver03.find_element_by_xpath('//*[@class="form-control bottom"]').send_keys(password)
    sleep(1)
    driver03.find_element_by_xpath('//*[@class="btn btn-success"]').click()
    sleep(2)

def git_liucheng(package_name,jenkins_package):
    # 点击"projects"
    driver03.find_element_by_xpath('//*[@class="list-unstyled navbar-sub-nav"]/li[1]/button').click()
    sleep(1)
    # 输入工程名
    driver03.find_element_by_xpath(
        '//*[@class="list-unstyled navbar-sub-nav"]//li[1]//*[@class="frequent-items-dropdown-container"]//input').send_keys(package_name)
    print("输入工程名为："+package_name)
    sleep(1)
    driver03.find_element_by_xpath('//*[@class="frequent-items-item-metadata-container"]').click()
    sleep(2)

    # 点击tags
    driver03.find_element_by_xpath(
        '//*[@class="limit-container-width"]//*[@class="project-stats"]//li[3]/a').click()
    print("进入"+package_name+"工程tag列表")
    sleep(2)
    # 点击"new tags"
    driver03.find_element_by_xpath('//*[@class="nav-controls"]//*[@class="btn btn-success new-tag-btn"]').click()
    sleep(2)
    # 输入tag name
    driver03.find_element_by_xpath('//*[@id="tag_name"]').send_keys(jenkins_package)
    print("输入发布的版本号为"+jenkins_package)
    sleep(2)
    # 点击发布
    driver03.find_element_by_xpath('//*[@class="form-actions"]/button').click()
    # 点击tags验证是否发布
    driver03.find_element_by_xpath('//*[@class="breadcrumbs-links js-title-container"]/ul/li[4]/a').click()
    tag_one_name = driver03.find_element_by_xpath('//*[@class="tags"]//li[1]/div[1]/a').text
    if tag_one_name == jenkins_package:
        print("tag 发布成功！")
        sleep(3)
    else:
        print("tag 发布失败，请查看！")
        sleep(3)



if __name__ == '__main__':

    #根据打包次数来持续循环
    for i in range(int(num)):
        new = list[i]
        new_fenzhi = fenzhi_list[i]
        jianchen=list005[i]
        # 工程名
        p_name = new
        # 输入分支
        t_name = new_fenzhi
        #工程名简称
        j_name=jianchen

        print(p_name)
        print(t_name)

        # 添加文件下载设置，"0"禁止弹窗
        option = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': '/Users/apple/Desktop'}
        # 证书
        option.add_argument('--ignore-certificate-errors')
        # 添加一个传递给Chrome的实验性选项,name, valueß
        option.add_experimental_option('prefs', prefs)

        # 初始化chrome_options
        driver01 = webdriver.Chrome(options=option)
        #登录Jenkins
        login_jenkins(jenkins_url,jenkins_username,jenkins_password)
        #打包步骤
        aaa = jenkins_package(p_name,t_name)
        sleep(2)
        #关闭浏览器
        driver01.quit()


        driver02 = webdriver.Chrome(options=option)
        #登录rancher
        login_rancher(mmmm()[0],mmmm()[1],mmmm()[2],mmmm()[3])
        #进行发布流程
        bushu(j_name,aaa)
        sleep(2)
        driver02.quit()

        #判断当前是否是演示环境
        if l_num==1:
            #gitlab发布tag
            # 初始化chrome_options
            driver03 = webdriver.Chrome(options=option)
            #登录gitlab
            login_gitlab(git_url,git_username,git_password)
            #进行发布流程
            git_liucheng(j_name,aaa)
            sleep(2)
            driver03.quit()
        else:
            print("当前不是演示环境，无须发布tag    "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))








