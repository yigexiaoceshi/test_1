#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、需要Python环境
2、安装selenium，使用pycharm或者命令行(pip install selenium=版本号)
3、下载和浏览器版本对应的Driver，淘宝镜像下载地址：https://npm.taobao.org/mirrors/chromedriver；解压命令"unzip"，剪切/重命名"mv"，配置环境变量"vim ~/.zshrc"，执行"source ~/.zshrc"让配置生效，
配置前使用"./chromedriver"启动，配置好环境变量之后，直接输入Chromedriver可以直接启动，查看环境变量"echo $PATH"
4、selenium IDE暂不了解
5、Chrome的版本设置不自动更新方法：？？？？？？？？？
6、火狐浏览器淘宝镜像下载地址：http://npm.taobao.org/mirrors/geckodriver
"""

from selenium import webdriver


def test_selenium():
    brower = webdriver.Chrome()
    brower.get("https://www.baidu.com")
    brower.close()
