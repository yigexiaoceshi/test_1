#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
控件交互：
官方文档：https://selenium-python.readthedocs.io/api.html
ActionChains：执行PC端鼠标点击、双击、右键、拖拽等事件
TouchActions：模拟PC端和移动端的点击、滑动、拖拽、多点触控等多种手势操作
执行原理：
调用ActionChains方法时，不会立即执行，而是将所有的操作按照顺序放入一个队列，调用perform()方法时，事件按顺序依次执行

基本用法：
找到元素：
生成一个动作：action = ActionChains(driver)
给元素添加方法1：action.方法1
给元素添加方法2：action.方法2
调用perform()方法执行：action.perform()

具体写法1，链式写法：ActionChains(driver).move_to_element(element).click(element).perform()
具体写法2，分布写法：
actions = ActionChains(driver)
actions.move_to_element(element)
actions.click(element)
actions.perform()
"""
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""ActionChains的用法"""


class TestActionChains():
    def setup(self):
        self.brower = webdriver.Chrome()
        self.brower.implicitly_wait(3)
        self.brower.maximize_window()

    def teardown(self):
        self.brower.quit()

    # 测试用例1：模拟点击、双击、右键点击方法，测试URL：http://sahitest.com/demo/clicks.htm
    @pytest.mark.skip
    def test_case_click(self):
        self.brower.get("http://sahitest.com/demo/clicks.htm")
        # element_click = self.brower.find_element(By.XPATH,'/html/body/form/input[3]')
        # 第一步，找到元素
        element_click = self.brower.find_element(By.XPATH, '//input[@value="click me"]')
        element_double_click = self.brower.find_element(By.XPATH, '//input[@value="dbl click me"]')
        element_right_click = self.brower.find_element(By.XPATH, '//input[@value="right click me"]')
        # 第二步，为元素生成动作，将动作对应的元素传入
        actions = ActionChains(self.brower)
        actions.click(element_click)  # 点击方法.click
        actions.double_click(element_double_click)  # 双击方法.double_click
        actions.context_click(element_right_click)  # 右击方法.context.click
        # 第三步，调用perform()方法执行上面的动作
        actions.perform()
        sleep(1)

    # 测试用例2：将鼠标移动到百度首页的"设置"按钮
    @pytest.mark.skip
    def test_move_to_baidu(self):
        self.brower.get("https://www.baidu.com")
        ele = self.brower.find_element(By.ID, "s-usersetting-top")
        actions = ActionChains(self.brower)
        actions.move_to_element(ele)
        actions.perform()
        sleep(1)

    # 测试用例3：模拟鼠标拖拽，测试URL：http://sahitest.com/demo/dragDropMooTools.htm
    @pytest.mark.skip
    def test_drag_drop(self):
        self.brower.get("http://sahitest.com/demo/dragDropMooTools.htm")
        start_ele = self.brower.find_element(By.ID, "dragger")  # 拖拽起始元素
        end_ele = self.brower.find_element(By.XPATH, "/html/body/div[2]")  # 拖拽的目标元素
        actions = ActionChains(self.brower)
        # 拖拽方法1：使用drag_and_drop(start_ele,end_ele)，从起始元素拖动到目标元素
        # actions.drag_and_drop(start_ele,end_ele).perform() #传入两个值，效果等同于下面2个方法
        # 拖拽方法2：这个方法相当于点击起始元素，hold表示不松开，release在目标元素松开，效果一样
        # actions.click_and_hold(start_ele).release(end_ele).perform()
        # 拖拽方法3：点击起始元素不松开(start_ele)，移动到目标元素(start_ele)，然后release松开(end_ele)
        actions.click_and_hold(start_ele).move_to_element(end_ele).release(end_ele).perform()
        sleep(1)

    # 测试用例4：模拟键盘操作，测试URL：http://sahitest.com/demo/label.htm
    """
    用法：
    1、action = ActionsChains(driver)
    2、action.send_keys(Keys.BACK_SPACE)
    或者：action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONNTROL)
    3、action.perform()
    """

    @pytest.mark.skip
    def test_keys(self):
        """
        1、用户名输入框输入username
        2、使用键盘的空格键输入一个空格
        3、继续输入tom
        3、调用键盘的删除键，删除m字母
        :return:
        """
        self.brower.get("http://sahitest.com/demo/label.htm")
        ele_input = self.brower.find_element(By.XPATH, "/html/body/label[1]/input")
        actions_keys = ActionChains(self.brower)
        # 输入之前先要点击一下输入框，让光标定位在输入框内
        actions_keys.click(ele_input)
        # 先调动send_keys输入username
        actions_keys.send_keys("username")
        # 在调用Keys.SPACE键盘方法里使用一次空格键
        actions_keys.send_keys(Keys.SPACE)
        # 再输入一个tom
        actions_keys.send_keys("tom")
        # 再调用键盘的删除方法Keys.BACK_SPACE删除tom里的m
        actions_keys.send_keys(Keys.BACKSPACE).perform()
        sleep(2)
