#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-

import allure
import pytest
import datetime
from config import *
from tools.logs import logger_config
log2 = logger_config(log_path=f'/Users/apple/PycharmProjects/zhongshujiaoben/logs/{datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")} '+__name__+' .txt')#调用自定义封装的log函数

from Customer_platform.API.proxy.add_proxy import Add_proxy
from Customer_platform.API.proxy.my_proxy import My_proxy
from Customer_platform.API.proxy.proxy_shenqing import Shenqing_proxy

ad=Add_proxy(jierufang_url,userId_jierufang01,username01,token_jierufang01)
mp=My_proxy(jierufang_url,userId_jierufang01,username01,token_jierufang01)
sp=Shenqing_proxy(jierufang_url,userId_jierufang02,username02,token_jierufang02)

@pytest.fixture(scope="module")
def test_myproxy():
    res_add=ad.add_newproxy()
    name=res_add[1]
    res=res_add[0]
    res_mp=mp.my_proxy_list(name)
    id=res_mp[1]
    zscode=res_mp[2]
    xxxxx=res_mp[0]
    return name,id,zscode,res,xxxxx

@allure.epic("代理服务")
@allure.feature("服务创建")
class Test_newproxy:
    @allure.title("服务创建成功")
    def test_proxy(self,test_myproxy):
        result=test_myproxy[3]
        # print(result)
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log2.error(err)
            raise  err

@allure.epic("代理服务")
@allure.feature("我的服务")
class Test_my_proxy:
    @allure.title("我的服务-列表查询")
    def test_my_proxy_list(self,test_myproxy):
        result=test_myproxy[4]
        # print(result)
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log2.error(err)
            raise  err
    @allure.title("我的服务-详情")
    def test_my_proxy_xiangqing(self,test_myproxy):
        result=mp.my_proxy_xiangqing(test_myproxy[1])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log2.error(err)
            raise  err

    @allure.title("我的服务-区块链入链")
    def test_my_proxy_qukuailian(self,test_myproxy):
        result=mp.my_proxy_qukuailian(test_myproxy[2])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log2.error(err)
            log2.error(err)
            raise  err


    @allure.title("我的服务-编辑")
    def test_my_proxy_edit(self,test_myproxy):
        time.sleep(2)
        result=mp.my_proxy_edit(test_myproxy[2],test_myproxy[1])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log2.error(err)
            raise  err

    @allure.title("我的服务-停用")
    def test_my_proxy_disable(self,test_myproxy):
        result=mp.my_proxy_disable(test_myproxy[1])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log2.error(err)
            raise err

    @allure.title("我的服务-启用")
    def test_my_proxy_enable(self,test_myproxy):
        result=mp.my_proxy_enable(test_myproxy[1])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log2.error(err)
            raise  err

@allure.epic("代理服务")
@allure.feature("申请服务")
class Test_shenqing_proxy:
    @allure.title("文件上传")
    def test_file_proxy(self):
        result=sp.proxy_file()[0]
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log2.error(err)
            raise  err

    @allure.title("服务申请-提交")
    def test_proxy_tijiao(self,test_myproxy):
        res = sp.proxy_file()
        filePath=res[1]
        fileName=res[2]
        result=sp.proxy_tijiao(test_myproxy[2],fileName,filePath)
        # print(result)
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log2.error(err)
            raise  err
