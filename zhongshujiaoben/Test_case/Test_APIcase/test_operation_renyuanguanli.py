#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import pytest
import allure
from config import  *
from Operation_platform.yunying_API.renyuanguanli.newuser_customer import new_customer
from Operation_platform.yunying_API.renyuanguanli.new_operation_role import new_role
from Operation_platform.yunying_API.renyuanguanli.newuser_operation import new_operation

opertion_url=yunying_url
opertion_userid=userId_yunying
opertion_token=token_yunying
opertion_username=username_yunying

yy_c=new_customer(opertion_url,opertion_userid,opertion_token,opertion_username)
yy_r=new_role(opertion_url,opertion_userid,opertion_token,opertion_username)
yy_o=new_operation(opertion_url,opertion_userid,opertion_token,opertion_username)


@pytest.fixture(scope="class")
def test_appShortName():
    appShortName=yy_c.add_jierufang()[1]
    return  appShortName


@allure.epic("运营平台")
@allure.feature("人员管理")
@allure.story("接入方管理")
#接入方管理
class Test_renyuanguanli:
    # @pytest.mark.run(order=1)
    # @allure.title("运营用户详情")
    # def test_user_xiangqing(self):
    #     result=yy_c.user_info()
    #     pytest.assume(str(result["code"])=="200")
    #     pytest.assume(result["success"]==True)

    @pytest.mark.run(order=2)
    @allure.title("创建接入方账号")
    def test_new_customer(self):
        result=yy_c.add_jierufang()[0]
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @pytest.mark.run(order=3)
    @allure.title("接入方列表简称查询")
    def test_jiancheng_chaxun(self,test_appShortName):
        result=yy_c.user_chaxun(test_appShortName[1])[2]
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @pytest.mark.run(order=4)
    @allure.title("接入方用户编辑")
    def test_bianji(self,test_appShortName):
        userid=yy_c.user_chaxun(test_appShortName)[1]
        appInfoId=yy_c.user_chaxun(test_appShortName)[0]
        result=yy_c.user_detail(userid,appInfoId)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @pytest.mark.run(order=5)
    @allure.title("接入方用户停用")
    def test_userout(self,test_appShortName):
        userid=yy_c.user_chaxun(test_appShortName[1])[0]
        result=yy_c.user_out(userid)
        pytest.assume(str(result["code"]=="200"))
        pytest.assume(result["success"]==True)

    @pytest.mark.run(order=6)
    @allure.title("接入方用户启用")
    def test_useropen(self,test_appShortName):
        userid=yy_c.user_chaxun(test_appShortName[1])[0]
        yy_c.user_out(userid)
        result=yy_c.user_open(userid)
        pytest.assume(str(result["code"]=="200"))
        pytest.assume(result["success"]==True)


@pytest.fixture(scope="class")
def test_loginname():
    loginname=yy_o.add_operationuser()
    aa=loginname[1]
    bb=loginname[2]
    return aa,bb
# print(test_loginname())

#运营人员
@allure.epic("运营平台")
@allure.feature("人员管理")
@allure.story("运营人员")
class Test_new_operation:

    @pytest.mark.run(order=1)
    @allure.title("创建运营账号")
    def test_add_operationuser(self):
        """
        用例描述：
        """
        assert 0 == 0
        result=yy_o.add_operationuser()[0]
        pytest.assume(str(result["code"]=="200"))
        pytest.assume(result["success"]==True)

    @allure.title("运营列表用户名查询")
    def test_operation_list_chaxun01(self,test_loginname):
        result=yy_o.operation_list_chaxun01(test_loginname[0])[0]
        pytest.assume(str(result["code"]=="200"))
        pytest.assume(result["success"]==True)

    @allure.title("运营列表负责人查询")
    def test_operation_list_chaxun02(self,test_loginname):
        # result01=yy_o.operation_list_chaxun01(test_loginname)[2]
        result=yy_o.operation_list_chaxun02(test_loginname[1])
        # print(result)
        pytest.assume(str(result["code"]=="200"))
        pytest.assume(result['success']==True)

    @allure.title("运营列表状态查询")
    def test_operation_list_chaxun03(self):
        result=yy_o.operation_list_chaxun03()[0]
        pytest.assume(str(result["code"]=="200"))
        pytest.assume(result["success"]==True)

    @allure.title("授权用户角色")
    def test_shouquan_role(self,test_loginname):
        userid=yy_o.operation_list_chaxun01(test_loginname[0])[1]
        roleId=yy_o.user_role()[1]
        result=yy_o.shouquan_role(userid,roleId)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("编辑运营用户")
    def test_edit_user(self,test_loginname):
        userid=yy_o.operation_list_chaxun01(test_loginname[0])[1]
        result=yy_o.edit_user(userid)
        pytest.assume(str(result["code"]=="200"))
        pytest.assume(result["success"]==True)

    @allure.title("停用运营用户")
    def test_out_user(self,test_loginname):
        userid=yy_o.operation_list_chaxun01(test_loginname[0])[1]
        result=yy_o.out_user(userid)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)

    @allure.title("启用运营用户")
    def test_open_user(self,test_loginname):
        userid=yy_o.operation_list_chaxun01(test_loginname[0])[1]
        yy_o.out_user(userid)
        result=yy_o.open_user(userid)
        pytest.assume(str(result["code"])=="200")
        pytest.assume(result["success"]==True)


# pytest.fixture(scope="class")
# #获取角色名称
# def test_roleName():
#     roleName=yy_r.add_role()[1]
#     return roleName