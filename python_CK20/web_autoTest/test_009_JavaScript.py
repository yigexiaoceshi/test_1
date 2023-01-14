#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
使用方法调用js的好处：
1、直接使用过js操作页面，能解决很多click()不生效问题
2、页面滚动到底部，顶部
3、处理副文本，时间控件的输入

调用js的方法：
execute_script：执行js
return：可以返回js的返回结果
execute_scrept：arguments传参
"""
import time

"""常见的js语法使用，在开发者工具中的Console里输入:
document.title：获取页面title
window.alert('这是一个警告框')：模拟生成一个警告框
JSON.stringify(performance.timing)：可以获取当前页面一些性能指标数据
document.documentElement.scrollTop=10000：从顶部往下滚动，后面的数字是偏移量，0表示顶部
document.getElementByID("su")：通过ID定位元素
"""
from base import BaseSelenium
from selenium.webdriver.common.by import By
from time import sleep


# 案例1：
# 1、打开百度首页，输入搜索关键字，点击"百度一下"
# 2、搜索结果页面，滑动到底部点击"下一页"
class TestJs(BaseSelenium):
    # 案例1：使用js方法里的点击和滚动，并获取结果页的title和一些性能数据
    # @pytest.mark.skip
    def test_js_scroll(self):
        self.brower.get("https://www.baidu.com")
        # 定位到输入框，输入test_selenium
        self.brower.find_element(By.ID, "kw").send_keys("test_selenium")
        # 常规定位方法：定位到【百度一下】按钮，点击
        # self.brower.find_element(By.ID,"su").click()
        # 使用js语法定位：定位到【百度一下】按钮，点击，如果需要返回定位到的元素值，则需要加return，不需要则不加
        element = self.brower.execute_script("return document.getElementById('su')")
        print(element)  # 如果上一步不return的话，这里就是None，就没有办法执行下一步的click()方法
        element.click()
        sleep(1)
        # 在搜索页滑动到最底端
        self.brower.execute_script("return document.documentElement.scrollTop=10000")
        sleep(1)
        # 点击下一页
        self.brower.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()
        sleep(1)
        # 列表里多个js方法，使用for循环依次读取执行，并获取返回结果
        for code in ["return document.title", "return JSON.stringify(performance.timing)"]:
            print(self.brower.execute_script(code))
        # 执行多个js方法，如下，可以把多个方法以分号隔开一起写入一个execute_script里，但是只会返回第一个方法的值
        # print(self.brower.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    # 案例2：时间控件，修改12306上的出发日期，并打印修改后的触发日期，关闭网站
    # 1.取消日期的readonly属性
    # 2.给value赋值
    # 或者可以写js代码来实现如上两点，在使用webdriver对js进行处理
    # a = document.getElementById('train_date')
    # a.removeAttribute('readonly')

    def test_datetime(self):
        self.brower.get("https://www.12306.cn/index/")
        # 第一种写法
        # print(self.brower.execute_script("return document.getElementById('train_date').value"))
        # self.brower.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        # self.brower.execute_script("document.getElementById('train_date').value='2021-11-11'")
        # sleep(2)
        # print(self.brower.execute_script("return document.getElementById('train_date').value"))
        # 老师录播的写法
        # self.brower.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        # self.brower.execute_script("document.getElementById('train_date').value='2021-11-11'")
        # time.sleep(3)
        # print(self.brower.execute_script("reutrn document.getElementById('train_date').value"))
        # 第三种写法
        js1 = "document.getElementById('train_date').removeAttribute('readonly')"
        self.brower.execute_script(js1)
        sleep(2)
        js2 = "document.getElementById('train_date').value=('2021-11-11')"
        self.brower.execute_script(js2)
        sleep(2)
        print(f"当前日期为：{self.brower.find_element(By.ID, 'train_date').get_attribute('value')}")
