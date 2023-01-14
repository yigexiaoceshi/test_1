#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-

import pytest
import allure
from config import  *
from Operation_platform.yunying_API.ziyuanzhongxing.ziyuan_zhongxin import ziyuan_zx
from Customer_platform.API.zhishuguanli.zhishuzhuce_API import Index_signin
from Customer_platform.API.yewuxietong.zijianAPI import Api
from Customer_platform.API.yewuxietong.xitongjieru import System

#接入方-指数注册
zs=Index_signin(XXX_customer_url,userId_jierufang01,token_jierufang01)
#接入方-API注册
api=Api(XXX_customer_url,userId_jierufang01,token_jierufang01)
#接入方-系统接入
system=System(XXX_customer_url,userId_jierufang01,token_jierufang01)
#运营-全部指数
zyzx=ziyuan_zx(XXX_operation_url,userId_yunying,username_yunying,token_yunying)

@pytest.fixture(scope="module")
def system_name():
    xitong=system.add_xitong()[1]
    service_code=system.list_xitong(xitong)[1]
    return service_code,xitong

@allure.epic("资源中心")
@allure.feature("全部指数")
class Test_indicator:
    @allure.title("全部指数-查询")
    def test_ind_chaxun(self):
        zhishu_code=zs.zhishujibenxinxi()[2]
        result=zyzx.indicator_chaxun(zhishu_code)
        pytest.assume(str(result["code"]=="200"))
        pytest.assume(result["success"]==True)

    @allure.title("全部指数-区块链详情")
    def test_ind_current(self):
        zhishu_code = zs.zhishujibenxinxi()[2]
        result=zyzx.current_indicator(zhishu_code)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

@pytest.fixture(scope="module")
def apicode(system_name):
    uuid=api.jibenxinxi(system_name[0])[0]
    sourceApiCode=api.jibenxinxi(system_name[0])[2]
    api.APIpeizhi(uuid)
    api.fangwenxianzhi(uuid)
    api.fabu(uuid)
    api_code=api.list_zijianAPI(sourceApiCode)[1]
    # print(api_code)
    return api_code

@allure.epic("资源中心")
@allure.feature("全部API")
class Test_api:
    @allure.title("全部API-查询")
    def test_api_chaxun(self,apicode):
        result=zyzx.apilist(apicode)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("全部api-详情")
    def test_api_xiangq(self,apicode):
        result=zyzx.api_xiangqing(apicode)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("全部api-区块链详情")
    def test_api_current(self,apicode):
        result=zyzx.current_api(apicode)
        # print(result)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

@allure.epic("资源中心")
@allure.feature("系统接入")
class Test_system:
    @allure.title("系统接入-查询")
    def test_system_chaxun(self,system_name):
        result=zyzx.system(system_name[1])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("系统接入-区块链详情")
    def test_system_current(self,system_name):
        result=zyzx.current_system(system_name[0])
        # print(result)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)







