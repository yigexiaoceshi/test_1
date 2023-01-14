#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
配置步骤：
1、配置前，退出所有谷歌浏览器（Windows系统还需要将进程杀干净）
2、输入启动命令，通过命令启动谷歌浏览器
    a、进入chrome的启动路径输入命令启动
    b、或者配置环境变量之后直接启动:/Applications/Google\ Chrome.app/Contents/MacOS，vim ~/.zshrc中，
        一定要加反斜杠\，然后source ~/.zshrc或者重启命令行，输入Google\ Chrome能启动就OK，输入Goog也会自动联想
        表明配置成功
    2-1、Mac命令：Google\ Chrome --remote-debugging-port=9222，设置Chrome使用9222端口远程模式启动
    2-2、windows命令：chrome --remote-debugging-port=9222
3、验证是否启动成功：输入localhost:9222有数据展示，表明启动成功
4、代码配置：
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#定义配置的实例对象option
option = Options()
#修改实例属性为debug模式的：IP+端口
option.debugger_address = "localhost:9222"
#实例化driver对象的时候，添加option配置
brower = webdriver.Chrome(options=option)  #到这一行，配置完成，可以在当前浏览器直接使用，只要页面不关闭，无需重复登录
brower.get("https://work.weixin.qq.com/wework_admin/frame")
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""
使用场景：
1、跳过登录：只要当前网页不关闭，session有效期内就一直可以是登录状态（第一次登录还是需要人工扫码的）
2、代码调试：常规的调试必须在问题行代码之前的代码全部执行完成才可以调试，现在可以注释前面所有的代码直接对问题行代码进行调试
"""

# 定义配置的实例对象option
option = Options()
# 修改实例属性为debug模式的：IP+端口
option.debugger_address = "localhost:9222"
# 实例化driver对象的时候，添加option配置
brower = webdriver.Chrome(options=option)
# 打开企业微信登录页面
# brower.get("https://work.weixin.qq.com/wework_admin/frame")
# #点击"添加成员"的操作
# brower.find_element(By.CSS_SELECTOR,'.index_service_cnt_item_title').click()
# #添加员工步骤：输入姓名
# brower.find_element(By.ID,'username').send_keys('username_张三')
# 添加员工步骤：输入账号
brower.find_element(By.ID, 'memberAdd_acctid').send_keys('zhanghao')  # 前面的代码都注释掉了，依然可以执行这一行
