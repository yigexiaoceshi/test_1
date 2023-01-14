#!/usr/bin/python3
# -*- coding:utf-8 -*-
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


# 定义一个公共类，封装其他页面共用的一些方法，和具体的业务不相关
class BasePage:
    # 每次进行类的实例化的时候，每个类就会寻找构造函数，如果没有就会找有继承的父类的构造函数，写在这个父类里，相当于每个子类都可以传递brower
    def __init__(self, a: WebDriver = None):  # 类型注解
        if a == None:
            # 继承，子类可以拿到父类的实例属性的，所以变量brower前面加self.变为实例变量，子类就可以直接使用
            self.brower = webdriver.Chrome()
            self.brower.get("https://work.weixin.qq.com/wework_admin/frame")
            self.brower.maximize_window()
            self.brower.implicitly_wait(5)
            cookies = yaml.safe_load(open("../conf/cookies.yaml"))
            for i in cookies:
                self.brower.add_cookie(i)
            self.brower.get("https://work.weixin.qq.com/wework_admin/frame")
            sleep(2)
        else:
            self.brower = a
