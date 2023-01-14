#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from Customer_platform.UI.Topic_together.New_topic import *
from Customer_platform.UI.Business_together.New_api import *
from Customer_platform.UI.User_login import login

if __name__ == '__main__':
    aaa = str(round(time.time() / 10))
    # topic名称
    topic_name = "UI自动化" + aaa
    #参数名称
    beizhu_name="UI参数" + aaa
    print(topic_name)
    try:
        login("zhouwenfeng","Aa123456")
        topic_menu()
        new_topic(topic_name,beizhu_name)
        code=my_topic(topic_name,beizhu_name)
        logout()
        login("Kobe","Aa123456")
        topic_menu()
        topic_apply(code)
    finally:
        driver.quit()