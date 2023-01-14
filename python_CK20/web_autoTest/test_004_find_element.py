#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
元素查找：
注意：
开发者工具console里调试XPATH，写法：$x('XPATH')
开发者工具console调试CSS，写法：$('CSS-SELECTOR')
1、ID：self.brower.find_element(By.ID,'值').send_keys('username')
2、name：self.brower.find_element(By.NAME,'值').click()
3、Xpath：appium，selenium都能使用
写法：self.brower.find_element(By.XPATH,'//*[@属性="属性值"]'),//表示根节点 下面所有所有级别，/表示下一级，*表示所有标签
    nodename:选取该节点的所有子节点
    /：从根节点选取
    //：从匹配当前节点的节点开始，不考虑位置
    .：选取当前节点
    ..：选取当前节点的父节点
    @：选取属性
例子：
定位百度搜索结果页面的tab标题"网页"，因为s_tab这个id下只有一个b了，所以可以写//b，[1]也可以不加
//*[@id="s_tab"]/div/b ：//*代表查找所有元素，[]表示括号里添加属性条件，@后面写属性="属性值"，中间的/表示当前元素的下级元素，//表示下面所有级别所有元素
//*[@id="s_tab"]/div/b[1]  ：解读同上，一个标签下的标签如果有很多相同的标签名，则使用索引读取，索引从1开始，第一个b标签用b[1]表示，最后一个用b[last()]，倒数第二个是b[last()-1]
//*[@id="s_tab"]/div//b ：这种写法，也是因为s_tab标签下，下级以及下面所有级别的所有元素中只有一个b标签，所以可以用//查找下面所有级别所有元素
定位百度搜索结果页面的tab标题"资讯"：('//*[@id="s_tab"]/div/a[1]')，div下的第一个标签是b，之后是8个a标签并列，资讯是第一个a标签a[1]
定位百度首页右上角的"百度首页"：'//*[@id="u"]/a[1]'
4、CSS-SELECTOR：appium，selenium都能使用，但是appium里的原生页面是不能使用的，APP里嵌套里的网页可以使用
写法：self.brower.find_element(By.CSS-SELECTOR,"CSS地址")
    .class ：例 ".intro"，表示选择class="intro"的所有元素 （."" 相当于XPATH里的 class=""）
    #id ： 例 "#firestname"，表示id="firstname"的所有元素 （#"" 相当于XPATH里的 id=""）
    * ： 选择所有元素
    element ： 例 p，选择所有<p>元素
    element,element ： 例 div,p 选择所有<div>元素和所有<p>元素
    element element ： 例 div p 选择所有<div>内部所有的<p>元素
    element>element ： 例 div>p 选择父元素为<div>的所有<p>元素
    element+element ： 例 div+p 选择紧接在<div>元素之后的所有<p>元素
    [attribute] ： 例 [target] 选择带有target属性的所有元素
    [attribute=vlue] ： 例 [target=_blank] 选择target="blank"的所有元素
    :nth-child(n) ： 例 p:nth-child(2) 选择属于其父元素的第二个子元素的每个<p>元素
    element1~element2 ： 例 p~ul 选择前面有<p>元素的每个<ul>元素
定位百度搜索结果页的搜索框：
#kw
#[id=kw]
定位百度搜索结果页面的tab标题"网页"：
#s_tab b：中间加个空格，相当于XPATH里的//,指的是寻找拥有值等于s_tab的id属性的标签的所有下级，因为b标签已经是下级的下级
定位百度搜索结果页面的tab标题"资讯"
#s_tab a:nth-child(2)：索引为1是b标签，其他9个a标签和b是兄弟标签关系，索引依次从2-10，注意，此处取索引是小括号()
定位百度搜索结果页面的最后一个以及倒数第二个tab标题"更多"和"采购"
#s_tab a:nth-last-child(1)：中间加个last表明倒着数第几个标签
#s_tab a:nth-last-child(2)：倒数第二个a标签
如果想要按照层级找，还是定位到"资讯"：
#s_tab>div>a:nth-child(2)：>相当于XPATH里的/，表示只寻找当前级的下级
也可以结合来写：
[id=s_tab]>div>a:nth-child(2)
[name=???]>ppp>yyy(6)
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestWait:
    def setup(self):
        self.brower = webdriver.Chrome()
        self.brower.get("https://www.baidu.com")
        self.brower.maximize_window()

    def teardown(self):
        self.brower.quit()

    def test_wait(self):
        # 以下四种写法都是正确的
        # self.brower.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
        # self.brower.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院试学院")
        # self.brower.find_element(By.CSS_SELECTOR,'[id=kw]').send_keys("霍格沃兹测试学院试学院")
        self.brower.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")
        sleep(1)
