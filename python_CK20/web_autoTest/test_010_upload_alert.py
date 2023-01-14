#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
input标签可以直接使用send_keys(文件地址)来上传文件
用法：
ele = brower.find_element(By.ID,"上传按钮ID")
或：ele = brower.find_element_by_id('上传按钮ID')
ele.send_keys("文件路径+文件名")
"""
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base import BaseSelenium


class TestUpload(BaseSelenium):
    # 上传控件
    def test_upload(self):
        """
        打开百度，点击上传图标，点击上传按钮，上传一张图片
        :return:
        """
        self.brower.get("https://www.baidu.com")
        sleep(1)
        self.brower.find_element(By.XPATH, '//*[@id="form"]/span[1]/span[2]').click()
        sleep(1)
        self.brower.find_element(By.XPATH, '//*[@id="form"]/div/div[2]/div[2]/input').send_keys(
            '/Users/liyong/Downloads/图片.jpg')
        sleep(1)

    # 警告框，弹窗，测试URL：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
    def test_alert(self):
        """
        switch_to_alert()：获取当前页面的警告框，并切入该警告框，无法通过定位获取alert的元素
        text：返回alert/confirm/prompt中的文本信息
        accept()；接收现有警告框，相当于点击确定
        dismiss()：解散现有警告框，相当于点击取消
        send_keys(keysToSend)：发送文本到警告框，keysToSend：将文本发送到警告框
        :return:
        """
        self.brower.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切入嵌套
        self.brower.switch_to_frame("iframeResult")
        sleep(1)
        # 起始位置元素
        start_ele = self.brower.find_element(By.ID, "draggable")
        # 目标位置元素
        end_ele = self.brower.find_element(By.ID, "droppable")
        # 创建动作容器对象
        actions = ActionChains(self.brower)
        # 往容器对象中添加动作队列，并调用perform()方法依次执行
        actions.drag_and_drop(start_ele, end_ele).perform()
        sleep(1)
        # 切换至警告框
        self.brower.switch_to_alert()
        sleep(1)
        # 警告框上点击【确定】
        self.brower.switch_to_alert().accept()
        # 切出嵌套
        self.brower.switch_to.parent_frame()
        sleep(1)
        # 点击页面的【点击运行】按钮，起始位置元素和目标位置元素回到初始位置
        self.brower.find_element(By.ID, 'submitBTN').click()
        sleep(1)
