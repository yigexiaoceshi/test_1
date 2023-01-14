#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
allure提供的测试报告里，可以为每条用例插入文案描述，HTML代码块，图片及视频：
用法：定义在每个函数或方法内
语法：allure.attach()方法，括号内传入插入的内容，别名，还须指定内容的类型
allure.attach("文本文件内容","重命名/别名",attachment_type=allure.attachment_type=TEXT)
allure.attach("HTML代码块内容","重命名/别名",attachment_type=allure.attachment_type=HTML)
allure.attach.file("路径及图片文件名","重命名/别名",attachment_type=allure.attachment_type=JPG)
allure.attach.file("路径及视频文件名","重命名/别名",attachment_type=allure.attachment_type=MP4)
"""
import allure


def test_attach_text():
    allure.attach("这是个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段HTMLbody代码块", "html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("/Users/liyong/Download/1.jpg", name="这是一个图片", attachment_type=allure.attachment_type.JPG)


def test_attach_videl():
    allure.attach.file("/Users/liyong/Download/2.MP4", name="这是一个视频", attachment_type=allure.attachment_type.MP4)


"""
1、执行：pytest test_009_allure_jpg_video.py --alluredir=./result3 --clear-alluredir
    注：参数"--clean-alluredir"，如果当前目录存在并且已经有过执行结果，先清除再写入，相当于覆盖操作
2、执行：allure serve ./result3
3、执行：allure generate ./result3 -o 指定目录
"""
