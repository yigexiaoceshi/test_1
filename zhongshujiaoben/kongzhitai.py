

from selenium import webdriver
from time import sleep
import os
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\Users\\84006\\Desktop\\xiazai'}
options.add_experimental_option('prefs', prefs)
#
# driver = webdriver.Chrome()
#
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(10)
sleep(2)
# url = 'http://172.18.111.66:30039/#/'
#登录接入方
def loginjierufang(url,username,password):
    driver.get(url)
    sleep(2)
    driver.find_element_by_css_selector('[id="username"]').send_keys(username)
    driver.find_element_by_css_selector('[id="password"]').send_keys(password)
    driver.find_element_by_tag_name('button').click()
    sleep(5)
#api授权-我申请的
def APIwoshenqing(shengqingdanhao):
    #点击我申请的
    driver.find_element_by_xpath('//*[@class="cbd-page-side-bar-wrapper"]/ul/li[2]/ul/li[1]').click()
    #点击API授权
    driver.find_element_by_xpath('//*[@class="ant-tabs-nav-scroll"]/div/div/div[1]').click()
    #输入申请单号
    driver.find_element_by_css_selector('[class="ant-tabs-tabpane ant-tabs-tabpane-active"] [id="applyBillCode"]').send_keys(shengqingdanhao)
    #点击查询
    driver.find_element_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div[2]//button[1]').click()
    sleep(2)
    #获取审批备注
    ele = driver.find_element_by_xpath('//*[@class="ant-table-content"]/div[1]//tbody/tr/td[8]').text
    print(ele)
    #点击详情
    driver.find_element_by_xpath('//*[@class="ant-table-content"]/div[2]//tbody/tr/td/a').click()
    sleep(1)
    #点击查看附件
    driver.find_element_by_link_text('查看附件').click()
    sleep(2)
    eles1 = driver.find_elements_by_css_selector('[class="ant-modal-mask"]')
    if eles1 != []:
        print('附件显示成功')
    #点击返回按钮
    driver.find_element_by_xpath('//*[@class="ant-modal-mask"]/following-sibling::div[1]//*[@class="ant-modal-content"]/div[2]//button').click()
    sleep(2)
    #点击下载附件按钮
    driver.find_element_by_link_text('下载附件').click()
    sleep(10)
    #查看API详情
    driver.find_element_by_link_text('查看详情').click()
    sleep(2)
    #获取API名称
    ele1 = driver.find_element_by_xpath('//*[@class="ant-descriptions-view"]//tr[2]/td[1]/span[2]').text
    print(ele1)
    sleep(2)
    #返回审批页面
    driver.find_element_by_tag_name('button').click()
    sleep(2)
    #回到我申请页面
    driver.find_element_by_link_text('我申请的').click()
    sleep(1)

#我申请的-指数授权
def zhishuwoshenqing(shenqingdanhao):
    #点击我申请的
    driver.find_element_by_css_selector('[class="cbd-page-side-bar-layout"] .cbd-page-side-bar-wrapper>ul>li:nth-child(2)>ul>li:nth-child(1)').click()
    #点击指数授权
    driver.find_element_by_xpath('//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div[1]/div[2]').click()
    #输入申请单号
    driver.find_element_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]//*[@id="applyBillCode"]').send_keys(shenqingdanhao)
    #点击查询
    driver.find_element_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]//button[1]').click()
    #点击详情
    driver.find_element_by_link_text('详情').click()
    sleep(1)
    #查看附件
    driver.find_element_by_link_text('查看附件').click()
    sleep(1)
    eles3 = driver.find_elements_by_xpath('//*[@class="ant-modal-mask"]/following-sibling::div[1]//canvas')
    if eles3!=[]:
        print('附件显示成功')
    #点击返回
    driver.find_element_by_xpath('//*[@class="ant-modal-mask"]/following-sibling::div[1]//button').click()
    #点击下载
    driver.find_element_by_link_text('下载附件').click()
    sleep(10)
    #点击查看接口详情
    driver.find_element_by_xpath('//*[@class="ant-spin-container"]/div[2]//a').click()
    #返回审批详情
    driver.find_element_by_tag_name('button').click()
    sleep(1)
    #进入我申请的
    driver.find_element_by_link_text('我申请的').click()
    sleep(1)









#API重新提交
def APIchongxintijiao(shengqingdanhao):
    # 点击我申请的
    driver.find_element_by_xpath('//*[@class="cbd-page-side-bar-wrapper"]/ul/li[2]/ul/li[1]').click()
    # 点击API授权
    driver.find_element_by_xpath('//*[@class="ant-tabs-nav-scroll"]/div/div/div[1]').click()
    # 输入申请单号
    driver.find_element_by_css_selector('[id="applyBillCode"]').send_keys(shengqingdanhao)
    # 点击查询
    driver.find_element_by_xpath('//*[@class="ant-row"]/div[2]//button[1]').click()
    sleep(2)
    # 获取审批备注
    ele = driver.find_element_by_xpath('//*[@class="ant-table-content"]/div[1]//tbody/tr/td[8]').text
    print(ele)
    sleep(1)
    #点击重新提交
    driver.find_element_by_partial_link_text('重新提交').click()
    sleep(2)
    #点击提交
    driver.find_element_by_xpath('//*[@class="submit-action-layout"]/button[1]').click()
    sleep(2)
    # 点击API授权
    driver.find_element_by_xpath('//*[@class="ant-tabs-nav-scroll"]/div/div/div[1]').click()
    # 输入申请单号
    driver.find_element_by_css_selector(
        '[class="ant-tabs-tabpane ant-tabs-tabpane-active"] [id="applyBillCode"]').send_keys(shengqingdanhao)
    # 点击查询
    driver.find_element_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div[2]//button[1]').click()
    sleep(2)
    # 获取审批备注
    ele = driver.find_element_by_xpath('//*[@class="ant-table-content"]/div[1]//tbody/tr/td[8]').text
    print(ele)


#指数重新提交
def zhishuchongxintijiao(shenqingdanhao):
    # 点击我申请的
    driver.find_element_by_css_selector(
        '[class="cbd-page-side-bar-layout"] .cbd-page-side-bar-wrapper>ul>li:nth-child(2)>ul>li:nth-child(1)').click()
    # 点击指数授权
    driver.find_element_by_xpath('//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div[1]/div[2]').click()
    # 输入申请单号
    driver.find_element_by_xpath(
        '//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]//*[@id="applyBillCode"]').send_keys(shenqingdanhao)
    # 点击查询
    driver.find_element_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]//button[1]').click()
    #点击重新提交
    driver.find_element_by_partial_link_text('重新提交').click()
    sleep(1)
    #点击提交
    driver.find_element_by_xpath('//*[@class="reapply-auth-layout"]//*[@class="submit-action-layout"]/button[1]').click()
    sleep(1)
    # 点击指数授权
    driver.find_element_by_xpath('//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div[1]/div[2]').click()
    # 输入申请单号
    driver.find_element_by_xpath(
        '//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]//*[@id="applyBillCode"]').send_keys(shenqingdanhao)
    # 点击查询
    driver.find_element_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]//button[1]').click()
    sleep(1)
    #获取审批备注
    ele3 = driver.find_element_by_css_selector('[class="ant-tabs-tabpane ant-tabs-tabpane-active"] .ant-table-scroll tbody>tr>td:nth-child(9)').text
    print(ele3)




#我审批的
def shenpi(shengqingdanhao,shenpiname):
    #点击我审批的
    driver.find_element_by_xpath('//*[@class="cbd-page-side-bar-wrapper"]/ul/li[2]/ul/li[2]').click()
    #点击待审批
    driver.find_element_by_xpath('//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[2]').click()
    # 输入申请单号
    driver.find_element_by_css_selector('[class="ant-tabs-tabpane ant-tabs-tabpane-active"] [id="applyBillCode"]').send_keys(shengqingdanhao)
    # 点击查询
    driver.find_element_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div[2]//button[1]').click()
    #点击审批
    driver.find_element_by_link_text('审批').click()
    sleep(2)
    # 点击查看附件
    driver.find_element_by_link_text('查看附件').click()
    sleep(2)
    eles1 = driver.find_elements_by_css_selector('[class="ant-modal-mask"]')
    if eles1 != []:
        print('附件显示成功')
    else:
        driver.get_screenshot_as_file("../../jietu/error2_png.png")
    # 点击返回按钮
    driver.find_element_by_xpath(
        '//*[@class="ant-modal-mask"]/following-sibling::div[1]//*[@class="ant-modal-content"]/div[2]//button').click()
    sleep(2)
    # 点击下载附件按钮
    driver.find_element_by_link_text('下载附件').click()
    sleep(10)
    # 查看API详情
    driver.find_element_by_link_text('查看详情').click()
    sleep(2)
    # 获取API名称
    ele1 = driver.find_element_by_xpath('//*[@class="ant-descriptions-view"]//tr[2]/td[1]/span[2]').text
    print(ele1)
    sleep(2)
    # 返回审批页面
    driver.find_element_by_tag_name('button').click()
    sleep(2)
    if shenpiname == '通过':
        driver.find_element_by_xpath('//*[@class="simplebar-content-wrapper"]//button[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@class="ant-modal-content"]/div//button[2]').click()
        sleep(1)
    elif shenpiname == '不通过':
        driver.find_element_by_xpath('//*[@class="simplebar-content-wrapper"]//button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="refuseReason"]').send_keys('不想通过')
        driver.find_element_by_xpath('//*[@class="ant-modal-confirm-body-wrapper"]/div[2]/button[2]').click()

    # 回到我审批页面
    driver.find_element_by_link_text('我审批的').click()
    sleep(1)
    #点击已审批页面
    driver.find_element_by_xpath('//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[3]').click()
    # 输入申请单号
    driver.find_element_by_css_selector(
        '[class="ant-tabs-tabpane ant-tabs-tabpane-active"] [id="applyBillCode"]').send_keys(shengqingdanhao)
    # 点击查询
    driver.find_element_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div[2]//button[1]').click()
    sleep(2)
    #获取审批备注
    eles2 = driver.find_elements_by_xpath('//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div[2]//*[@class="ant-table-body"]//tbody/tr/td[5]')
    if eles2 != []:
        return eles2[0].text
    else:
        driver.get_screenshot_as_file("../../jietu/error1_png.png")



loginjierufang('http://172.18.111.66:30039/#/','zhouyi','Aa123456')
# APIchongxintijiao()
# APIwoshenqing()
driver.quit()


