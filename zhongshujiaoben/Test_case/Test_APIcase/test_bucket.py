#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import pytest
import allure
from config import *
from Customer_platform.API.bucket.bucket_zhuce import bucket_zc
from Customer_platform.API.bucket.my_bucket import my_bucket
from Customer_platform.API.bucket.bucket_shenqing import buckek_shenqing

#bucket注册
bz=bucket_zc(XXX_customer_url,userId_jierufang01,username01,token_jierufang01)
#我的bucket
mb=my_bucket(XXX_customer_url,userId_jierufang01,username01,token_jierufang01)
#bucket申请
bs=buckek_shenqing(XXX_customer_url,userId_jierufang02,username02,token_jierufang02)

@pytest.fixture(scope="module")
def test_bucketcode():
    bucketcode_zcjk=bz.bucket_chuanjian()
    json=bucketcode_zcjk[0]
    bucketcode=bucketcode_zcjk[1]
    bucketname=bucketcode_zcjk[2]
    return json,bucketcode,bucketname

@allure.epic("文件管理")
@allure.feature("bucket创建")
class Test_bucket_zc:
    @allure.title("bucket注册")
    def test_bucket_zc(self,test_bucketcode):
        result=test_bucketcode[0]
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

@allure.epic("文件管理")
@allure.feature("我的bucket")
class Test_bucket_my:
    @allure.title("我的bucket-列表code查询")
    def test_bucket_listcode(self,test_bucketcode):
        result=mb.bucket_list_code(test_bucketcode[1])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("我的bucket-列表name查询")
    def test_bucket_listname(self,test_bucketcode):
        result=mb.bucket_list_name(test_bucketcode[2])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("我的bucket-编辑")
    def test_bucket_edit(self,test_bucketcode):
        result=mb.bucket_edit(test_bucketcode[1],test_bucketcode[1])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("我的bucket-详情-基本信息")
    def test_bucket_xiangqing_jibenxinxi(self,test_bucketcode):
        result=mb.bucket_xiangqing(test_bucketcode[1])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("我的bucket-详情-文件信息")
    def test_bucket_xiangqing_file(self,test_bucketcode):
        result=mb.bucket_xiangqing_file(test_bucketcode[1])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("我的bucket-详情-文件信息-上传文件")
    def test_bucket_xiangqing_file_upload(self,test_bucketcode):
        result=mb.upload_file(test_bucketcode[1])[0]
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("我的bucket-详情-文件信息-预览")
    def test_bucket_xiangqing_file_preview(self,test_bucketcode):
        filecode=mb.upload_file(test_bucketcode[1])[1]
        result=mb.bucket_preview(filecode)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("我的bucket-详情-文件信息-重命名")
    def test_bucket_xiangqing_file_raname(self,test_bucketcode):
        filecode=mb.upload_file(test_bucketcode[1])[1]
        result=mb.bucket_file_rename(filecode)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("我的bucket-详情-文件信息-删除")
    def test_bucket_xiangqing_file_delete(self,test_bucketcode):
        filecode=mb.upload_file(test_bucketcode[1])[1]
        result=mb.bucket_file_delete(filecode)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

@allure.epic("文件管理")
@allure.feature("bucket申请")
class Test_bucket_shenqing:
    @allure.title("bucket申请-列表查询")
    def test_bucket_shenqing_list(self,test_bucketcode):
        result=bs.bucket_shenqing_list(test_bucketcode[1])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("bucket申请-详情-基本信息")
    def test_bucket_shenqing_xiangqing(self,test_bucketcode):
        result=bs.bucket_shenqing_xiangqing(test_bucketcode[1])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("bucket申请-详情-文件信息")
    def test_bucket_shenqing_file(self,test_bucketcode):
        result=bs.bucket_shenqing_xiangqing_file(test_bucketcode[1])
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("bucket申请-上传附件")
    def test_bucket_file(self):
        result=bs.bucket_file()[0]
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("bucket申请-提交")
    def test_bucket_shenqing(self,test_bucketcode):
        file_key=bs.bucket_file()[1]
        result=bs.bucket_shenqing(test_bucketcode[1],file_key)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)