#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
为什么要使用cookie登录
1、首次需要人工介入，且浏览器不能关闭，不然需要频繁人工介入，新打开的浏览器不能记录登录信息，不适用于经常需要关闭打开且需要反复执行的场景
2、而cookie只要在时效性内，就可反复使用，且时效性一般都很长
使用思路：
1、打开浏览器，首次扫码登录
2、确保登录成功之后，通过get_cookies获取cookie
3、检查本地文件是否已经获取cookie成功
4、再次打开浏览器，就可以通过cookie直接进入主页
注意事项：
1、大部分登录场景cookie都有互踢机制，获取到的cookie在新的cookie生成后会失效
2、使用方法get_cookies()时，一定要确保已经登录成功
3、植入cookie之后需要进入登录页面，刷新验证是否自动登录成功
方法：
获取cookie：brower.get_cookies()
添加cookie：brower.add_cookie(cookie)
"""
from time import sleep
import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup(self):
        self.brower = webdriver.Chrome()

    def teardown(self):
        self.brower.quit()

    def test_get_cookies(self):
        # 1.进入企业微信扫码登录页面
        self.brower.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # 2.设置等待时间10秒，等待人工扫码
        sleep(10)
        # 3.等待成功登录之后，再去获取cookie信息
        cookie = self.brower.get_cookies()
        print(cookie)
        # 4.将获取到的cookie存入一个可持续存储的地方（比如文件，或者数据库），添加写入权限w
        with open("cookie.yaml", "w") as file:
            # yaml.safe_dump()函数传入2个参数，第一个是需要写入的数据，第二个是指定的文件，把什么数据写入哪个文件
            yaml.safe_dump(cookie, file)

    def test_add_cookie(self):
        # 1.访问企业微信主页面
        self.brower.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # 2.定义cookie，从yaml文件里读取
        cookie = yaml.safe_load(open("cookie.yaml"))
        print(cookie)
        # 3.植入cookie
        for c in cookie:
            self.brower.add_cookie(c)
        # 4.直接访问已经登录的企业微信首页，发现无需扫码，能够自动进入登录状态的首页
        self.brower.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(1)
