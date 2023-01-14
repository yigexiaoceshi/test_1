#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import  pytest
import allure
from config import *
from tools import logs
from Customer_platform.API.device.device_zhuce import device_zhuce
from Customer_platform.API.device.my_device import my_device
from Customer_platform.API.device.device_shenqing import device_shenqing

# log1=LogTools.logger()

#视频源注册
dz=device_zhuce(XXX_customer_url,userId_jierufang01,username01,token_jierufang01)
#视频源申请
ds=device_shenqing(XXX_customer_url,userId_jierufang02,username02,token_jierufang02)
#我的视频源
md=my_device(XXX_customer_url,userId_jierufang01,username01,token_jierufang01)

@pytest.fixture(scope="module")#模块级别
def test_huoqu_deviceCode():
    device=dz.device_zhucee()
    json1=device[0]
    devicecode=device[1]
    id=device[2]
    return json1,devicecode,id


@allure.epic("视频源接入")
@allure.feature("视频源注册")
# @pytest.mark.devcie_zhuce
class Test_device_zhuce:
    @allure.title("视频源单个注册")
    def test_device_zc(self,test_huoqu_deviceCode):
        result=test_huoqu_deviceCode[0]
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

    @allure.title("视频源批量注册")
    def test_device_piliangzc(self):
        result=dz.device_piliang_zhuce()
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

@allure.epic("视频源接入")
@allure.feature("我的视频源")
# @pytest.mark.my_devi
class Test_my_device:
    @allure.title("我的视频源-列表查询")
    def test_device_list(self,test_huoqu_deviceCode):
        result=md.device_list(test_huoqu_deviceCode[1])[0]
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

    @allure.title("我的视频源-详情-基本信息")
    def test_device_xiangqing_jiben(self,test_huoqu_deviceCode):
        result=md.device_xiangqing_jibenxinxi(test_huoqu_deviceCode[2])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

    @allure.title("我的视频源-详情-推流记录")
    def test_device_xiangqing_tuiliu(self,test_huoqu_deviceCode):
        result=md.device_xiangqing_tuiliu(test_huoqu_deviceCode[2])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err
    @allure.title("我的视频源-详情-授权记录")
    def test_device_xiangqing_shouquan(self,test_huoqu_deviceCode):
        result=md.device_xiangqing_shouquan(test_huoqu_deviceCode[2])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log1.error(err)
            raise  err


    @allure.title("我的视频源-详情-区块链")
    def test_device_xiangqing_qukuailian(self,test_huoqu_deviceCode):
        result=md.device_xiangqing_qukuai(test_huoqu_deviceCode[1])[0]
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            log1.error(err)
            raise  err
    @allure.title("我的视频源-详情-区块详情")
    def test_device_xiangqing_qukuaixq(self,test_huoqu_deviceCode):
        txid=md.device_xiangqing_qukuai(test_huoqu_deviceCode[1])[1]
        result=md.device_xiangqing_qukuaixiangqing(txid)
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

    @allure.title("我的视频源-编辑")
    def test_device_update(self,test_huoqu_deviceCode):
        result=md.device_upadte(test_huoqu_deviceCode[1],test_huoqu_deviceCode[2])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

@allure.epic("视频源接入")
@allure.feature("视频源申请")
class Test_device_shenqing:
    @allure.title("视频源申请-列表查询")
    def test_device_shenqinglist(self,test_huoqu_deviceCode):
        result=ds.device_shenqing_list(test_huoqu_deviceCode[1])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

    @allure.title("视频源申请-详情-基本信息")
    def test_device_shenqing_jibenxinxi(self,test_huoqu_deviceCode):
        result=ds.device_shenqing_xiangqing(test_huoqu_deviceCode[2])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

    @allure.title("视频源申请-详情-推流记录")
    def test_device_shenqing_tuiliujilu(self,test_huoqu_deviceCode):
        result=ds.device_shenqing_tuiliu(test_huoqu_deviceCode[2])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

    @allure.title("视频源申请-上传附件")
    def test_device_fujian(self):
        result=ds.device_file()[0]
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err

    @allure.title("视频源申请-提交申请")
    def test_device_tijiaoshenqing(self,test_huoqu_deviceCode):
        filekey=ds.device_file()[1]
        result=ds.device_tijiaoshenqing(str(filekey),test_huoqu_deviceCode[1])
        try:
            pytest.assume(str(result["code"])=="200","失败原因：%s" %result["message"])
            pytest.assume(result["success"]==True)
        except Exception as err:
            # log1.error(err)
            raise  err
