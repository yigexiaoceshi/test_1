#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
句柄操作：
多窗口切换：
1、获取当前窗口句柄：driver.current_window_handle
2、获取所有窗口句柄：driver.window_handles
3、判断当前窗口是否是想要操作的窗口，如果是，直接操作，如果不是则切换到目标窗口：driver.switch_to_window
"""
from time import sleep
from selenium.webdriver.common.by import By
from base import BaseSelenium  # 导入基础类，封装了统一的setup和teardown

"""案例1：
1.打开百度，点击登录，弹框中点击"立即注册"，
2.注册页面，输入用户名、手机号码、密码
3、返回登录页，点击"用户名登录"按钮，输入用户名和密码，点击登录
"""


# 句柄（handle ）练习，定义一个类，继承基础类
class TestHandle(BaseSelenium):
    def test_handle(self):
        # get方法获取目标URL
        self.brower.get("https://www.baidu.com")
        # 获取当前页面的句柄：
        baidu_handle = self.brower.current_window_handle
        print(baidu_handle)
        # 首页【登录】按钮
        login_buttom = self.brower.find_element(By.ID, "s-top-loginbtn")
        # 点击首页【登录】，跳到弹窗页
        login_buttom.click()
        # 登录弹窗页面【立即注册】按钮
        register_now_buttom = self.brower.find_element(By.CSS_SELECTOR,
                                                       '#passport-login-pop-dialog>div>div>div>div:nth-child(3)>a')
        # register_now_buttom = self.brower.find_element(By.LINK_TEXT,"立即注册")
        # 点击【立即注册】按钮，跳转到注册页面（打开新的标签页）
        register_now_buttom.click()
        sleep(1)
        # 再次获取当前页面句柄，可以看到当前操作窗口句柄仍然是点击【立即注册】之前的窗口
        register_handle = self.brower.current_window_handle
        print(register_handle)
        # 获取所有标签页句柄，得到一个列表
        all_handles = self.brower.window_handles
        print(all_handles)
        # 获取注册页面的句柄，并赋值给register_handle
        # for right_handle in all_handles:
        #     if right_handle != baidu_handle:
        #         register_handle = right_handle
        #     else:
        #         pass
        # print(register_handle)
        # 切换到注册页句柄，切换到首个句柄all_handles[0],上个页面的句柄all_handles[-1],
        self.brower.switch_to_window(all_handles[-1])
        # 注册页面依次输入用户名、手机号、密码，并获取输入值
        self.brower.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("username_zhangsan")
        user_name = self.brower.find_element(By.ID, "TANGRAM__PSP_4__userName").get_property("value")
        self.brower.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("phone_number")
        user_phone = self.brower.find_element(By.ID, "TANGRAM__PSP_4__phone").get_property("value")
        self.brower.find_element(By.ID, "TANGRAM__PSP_4__password").send_keys("userpassword_password")
        user_passwd = self.brower.find_element(By.ID, "TANGRAM__PSP_4__password").get_property("value")
        # 切换回百度首页句柄baidu_handle
        self.brower.switch_to_window(baidu_handle)
        # 点击【用户名登录】，跳转登录页面
        self.brower.find_element(By.ID, "TANGRAM__PSP_11__footerULoginBtn").click()
        # 输入用户名，密码，点击登录
        self.brower.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys(user_name)
        self.brower.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys(user_passwd)
        self.brower.find_element(By.ID, "TANGRAM__PSP_11__submit").click()
        sleep(2)


"""
注：查找页面元素时，一定要确保代码运行到了当前页面，比如上面test_touchaction()方法按照下面这么写就会报找不到该元素：
self.brower.get("https://www.baidu.com")
login_buttom = self.brower.find_element(By.ID,"s-top-loginbtn")
register_now_buttom = self.brower.find_element(By.CSS_SELECTOR,'#passport-login-pop-dialog>div>div>div>div:nth-child(3)>a')
login_buttom.click()
register_now_buttom.click()
这一段，是分别先找到2个页面的元素（其实是一个页面），因为第二个元素"立即注册"在第一个页面就已经有，只是被隐藏了，点击百度首页的【登录】按钮
之后才被显示出来，所以这样写，程序认为login_buttom和register_now_buttom都在当前页面找
"""

"""
frame：一种嵌套，一种未嵌套
切换frame：
driver.switch_to.frame() : 根据元素id或者index切换frame
driver.swaitch_to.default_contest() : 切换到默认frame
driver.switch_to.parent_frame() : 切换到父级frame
"""


# frame练习，定义一个类，继承基础类base，测试URL：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable

class TestFrame(BaseSelenium):
    def test_frame(self):
        self.brower.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切近frame，打印"请拖拽我"
        self.brower.switch_to.frame("iframeResult")
        print(self.brower.find_element(By.ID, "draggable").text)
        # 切回外层，打印【点击运行】按钮的文案
        # self.brower.switch_to.parent_frame()  #切换到父级frame
        self.brower.switch_to.default_content()  # 切换到默认的frame，和上面效果相同
        sleep(1)
        print(self.brower.find_element(By.ID, "submitBTN"))
