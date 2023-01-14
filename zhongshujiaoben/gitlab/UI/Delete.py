#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import sys
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep
option=webdriver.ChromeOptions()
option.add_argument('headless') # 设置option
driver = webdriver.Chrome(options=option)  # 调用带参数的谷歌浏览器

#删除权限
class Delete_authority:
    # 登录gitlab
    def login_gitlab(self,url,username,password):
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath('//*[@class="form-control gl-form-input top"]').send_keys(username)
        sleep(0.3)
        driver.find_element_by_xpath('//*[@class="form-control gl-form-input bottom"]').send_keys(password)
        sleep(0.3)
        driver.find_element_by_xpath('//*[@class="submit-container move-submit-down"]/input').click()
        sleep(0.3)


    def code(self,code):
        #输入验证码code
        driver.find_element_by_xpath('//*[@class="Customer-body"]/form/div/input').send_keys(code)
        sleep(0.3)
        driver.find_element_by_xpath('//*[@class="prepend-top-20"]/input').click()
        sleep(0.8)

    def git_shouye(self):
        # 点击"projects"
        driver.find_element_by_xpath('//*[@class="list-unstyled navbar-sub-nav"]/li[1]/button').click()
        sleep(0.5)
        for j in range(3):
            # 输入工程名
            lab_name = input("请输入工程名（回车结束）：")
            input_box=driver.find_element_by_xpath('//*[@class="list-unstyled navbar-sub-nav"]//li[1]//*[@class="gl-search-box-by-type"]//input')
            input_box.clear()
            driver.find_element_by_xpath('//*[@class="list-unstyled navbar-sub-nav"]//li[1]//*[@class="gl-search-box-by-type"]//input').send_keys(lab_name)
            sleep(0.5)
            #判断工程是否存在
            if "Sorry" in driver.find_element_by_xpath('//*[@id="nav-projects-dropdown"]//*[@class="list-unstyled"]/li').text :
                print("找不到该工程，请重新输入工程名！")
                if j ==2:
                    sys.exit("以重试三次，程序终止！")
                continue

            else:
                driver.find_element_by_xpath('//*[@class="frequent-items-item-metadata-container"]').click()
                sleep(0.5)
                #滑动位置
                moo = driver.find_element_by_xpath('//*[@class="sidebar-top-level-items qa-project-sidebar"]/li[11]')
                driver.execute_script("arguments[0].scrollIntoView();", moo)
                sleep(0.5)
                driver.set_page_load_timeout(1)
                try:
                    # 点击权限按钮menbers
                    driver.find_element_by_xpath('//*[@class="sidebar-top-level-items qa-project-sidebar"]/li[11]').click()
                except TimeoutException:
                    driver.execute_script('window.stop ? window.stop() : document.execCommand("Stop");')
                #获取所有人员信息
                renyuan = driver.find_elements_by_xpath('//*[@class="table b-table gl-table members-table b-table-stacked-lg"]/tbody/tr')
                for q in range(3):
                    name = input("请输入需要删除的人员姓名：")
                    # 寻找需要删除的人员
                    for i in renyuan:
                        name01=i.find_element_by_xpath('./td[1]/div/a/div/div/div/span').text
                        # print(name01)
                        if name == name01:
                            #删除
                            print("删除中")
                            i.find_element_by_xpath('./td[7]/div//button').click()
                            sleep(0.5)
                            #停止加载页面
                            driver.set_page_load_timeout(1)
                            try:
                                # 点击删除确认按钮
                                driver.find_element_by_xpath('//*[@class="modal-footer"]/button[2]').click()
                            except TimeoutException:
                                driver.execute_script('window.stop ? window.stop() : document.execCommand("Stop");')
                            sleep(0.5)
                            print(name + "大佬  " + lab_name + "  权限删除成功！")
                            break
                        else:
                            if q==2:
                                print("输入超过三次，程序终止！")
                                sys.exit("程序终止！")
                            continue
                    else:
                        print("人员姓名输入错误！")
                        continue
                    break
            break

if __name__ == '__main__':
    print("***删除授权操作***")
    #工程数量
    number=input("需删除几个工程权限(输入int类型)？：")
    # 输入二次验证code
    code_name = input("登录gitlab，输入二次验证code码：")
    # 登录gitlab
    Delete_authority().login_gitlab("https://gitlab2.cspiretech.com/users/sign_in", "zhouchengjie", 'yunyang@zcj2021')
    # 程序执行时间：
    start = time.time()
    # 输入code验证
    Delete_authority().code(code_name)

    num=1
    try:
        for i in range(int(number)):
            print("\n第"+str(num)+"个工程")
            #添加权限
            Delete_authority().git_shouye()
            num=num+1
    finally:
        sleep(0.5)
        driver.quit()
    # 结束时间
    end = time.time()
    #round保留小数
    print("\n总耗时：" + str(round((end - start), 2)) + "s")