#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
operation=webdriver.Chrome()

operation.get("standard.cspiretech.com:30037")
operation.maximize_window()
sleep(2)
operation.find_element_by_id("username").send_keys("zhouwenfeng")
operation.find_element_by_id("password").send_keys("Aa123456")
sleep(2)