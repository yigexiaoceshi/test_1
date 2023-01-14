import json

import pytest
import allure
import requests

from Customer_platform.API.yewuxietong.xitongjieru import System
from Customer_platform.API.yewuxietong.zijianAPI import Api
from Customer_platform.API.yewuxietong.quanbuAPI import All_API
from Customer_platform.API.kongzhitai.woshenpide.shenpiliucheng import Approval_process
# from Operation_Magage.APIlib.shenpi import ApprovalProcess
from Customer_platform.API.zhishuguanli.zhishuzhuce_API import Index_signin
from Customer_platform.API.zhishuguanli.zhishushenqing import Index_applyfor
from Customer_platform.API.zhishuguanli.wodezhishu import My_Index
from Customer_platform.API.xiaoxixietong.TopicZhuce import Topic_signin
from Customer_platform.API.xiaoxixietong.TopicShenqing import Topic_applyfor
from Customer_platform.API.xiaoxixietong.wodeTopic import My_Topic
from Customer_platform.API.shujvxietong.shujvzhuce import Data_signin
from Customer_platform.API.shujvxietong.shujvshenqing import Data_applyfor
from Customer_platform.API.shujvxietong.wodeshujv import My_Data

from config import *
url1 = jierufang_url
userid1 = userId_jierufang01
token1 = token_jierufang01
userid2 = userId_jierufang02
token2 = token_jierufang02

url_yunying = yunying_url
userid_yunying = userId_yunying
token_yunying = token_yunying

sy = System(url1,userid1,token1)
ap = Api(url1,userid1,token1)
aa = All_API(url1,userid2,token2)
ap1 = Approval_process(url1,userid2,token2)
ap2 = Approval_process(url1,userid1,token1)

app = ApprovalProcess(url_yunying,userid_yunying,token_yunying)

in_s = Index_signin(url1,userid1,token1)
in_a = Index_applyfor(url1,userid2,token2)
m_in = My_Index(url1,userid2,token2)

ts = Topic_signin(url1,userid1,token1)
ta = Topic_applyfor(url1,userid2,token2)
mt = My_Topic(url1,userid2,token2)

ds = Data_signin(url1,userid1,token1)
da = Data_applyfor(url1,userid2,token2)
md = My_Data(url1,userid1,token1)
md1 = My_Data(url1,userid2,token2)
#API授权审批流程
@allure.title('API授权审批流程')
def test_apishenpi():
    # 用户1创建API
    xitongname = sy.add_xitong()[1]
    rebody = sy.list_xitong(xitongname)['data']['list']
    serverCode = rebody[0]['serverCode']
    result = ap.fabu(serverCode)
    #断言API是否创建成功
    pytest.assume(result[0]['code'] == '200')
    pytest.assume(result[0]['success'] == True)
    #用户2申请该API
    result_1 = ap.list_zijianAPI(result[2])['data']['records']
    apicode1 = result_1[0]['apiCode']
    result1 = aa.list_quanbuAPI(apiCode=apicode1)['data']['records']
    apicode = result1[0]['apiCode']
    path = aa.shangchuanfujian()
    aa.shangchuanfujian01(path)
    result2 = aa.shangchuanwenjian02(apicode, path)
    #判断用户2申请授权是否成功
    pytest.assume(result2['code'] == '200')
    #判断用户2我申请页面是否有此API
    shenqingdanhao = result2['data']['applyBillCode']
    res3 = ap1.shenqing_API(shenqingdanhao)['data']['list']
    pytest.assume(str(res3[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res3[0]['approveStatus'] == 'ING')
    #判断用户1的我审批-待审批页面是否存在API
    res4 = ap2.shenpi_daishenpi(shenqingdanhao)['data']['list']
    # print(res4)
    pytest.assume(str(res4[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res4[0]['approveStatus'] == 'ING')
    # 用户1审批该API通过
    res5 = ap2.jieru_shenpi_yes(shenqingdanhao)
    pytest.assume(res5['code'] == '200')
    #用户1的我审批-已审批页面是否存在API
    res6 = ap2.shenpi_yishenpi(shenqingdanhao)['data']['list']
    pytest.assume(str(res6[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res6[0]['cusApprovalState'] == 'PASS')
    #运营方审批通过
    res7 = app.shenpi_yes(shenqingdanhao)
    pytest.assume(res7['code'] == '200')
    #用户2的已授权页面是否存在API
    res8 = aa.list_yishouquanAPI(apiCode=apicode1)['data']["records"]
    pytest.assume(res8[0]["apiCode"] == apicode1)

# time.sleep(5)
#指数授权审批流程
@allure.title('指数授权审批流程')
def test_zhishushenpi():
    # 用户1创建指数
    xitongname = sy.add_xitong()[1]
    rebody = sy.list_xitong(xitongname)['data']['list']
    serverCode = rebody[0]['serverCode']
    zhishuapicode = ap.add_zhishuAPI(serverCode)[0]['data']
    xinxi = in_s.zhishujibenxinxi()
    xiangxixinxi1 = in_s.xiangxixinxi(xinxi[0])
    in_s.guanlian_api(zhishuapicode)
    result = in_s.guanlian_num(xiangxixinxi1, zhishuapicode)
    pytest.assume(str(result['code']) == '200')
    pytest.assume(result['success'] == True)
    #用户2申请该指数
    dict1 = in_a.zhishushangchuanfujian()
    in_a.zhishushangchuanfujian01(dict1)
    # print(in_a.list_zhishushengqing(zhishuname=xinxi[1]))
    zhishucode = in_a.list_zhishushengqing(zhishuname=xinxi[1])["data"]["records"]
    result01 = in_a.zhishushangchuanwenjian02(zhishucode[0]["indicatorCode"], dict1)

    #判断用户2申请授权是否成功
    pytest.assume(result01['code'] == '200')
    #判断用户2我申请页面是否有此指数
    shenqingdanhao = result01['data']['applyBillCode']
    res3 = ap1.shenqing_zhishu(shenqingdanhao)['data']['list']
    pytest.assume(str(res3[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res3[0]['approveStatus'] == 'ING')
    #判断用户1的我审批-待审批页面是否存在指数
    res4 = ap2.shenpi_daishenpi(shenqingdanhao)['data']['list']
    # print(res4)
    pytest.assume(str(res4[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res4[0]['approveStatus'] == 'ING')
    # 用户1审批该A指数通过
    res5 = ap2.jieru_shenpi_yes(shenqingdanhao)
    pytest.assume(res5['code'] == '200')
    #用户1的我审批-已审批页面是否存在A指数
    res6 = ap2.shenpi_yishenpi(shenqingdanhao)['data']['list']
    pytest.assume(str(res6[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res6[0]['cusApprovalState'] == 'PASS')
    #运营方审批通过
    res7 = app.shenpi_yes(shenqingdanhao)
    pytest.assume(res7['code'] == '200')
    #用户2的已授权页面是否存在指数
    res8 = m_in.list_yishouquanzhishu(xinxi[1])['data']["list"]
    pytest.assume(res8[0]["indicatorName"] == xinxi[1])


#Topic授权审批流程
@allure.title('Topic授权审批流程')
def test_Topicshenpi():
    # 用户1创建Topic
    xitongname = sy.add_xitong()[1]
    rebody = sy.list_xitong(xitongname)['data']['list']
    xitongid = rebody[0]['id']
    topicname = ts.add_topic(xitongid)[1]
    #用户2申请该Topic
    # list1 = ta.list_suoyoutopic(topicname)['data']['records']
    # # list2 = [i for i in list1 if i['apply'] == True]
    # topiccode = list1[0]['topicCode']
    datapath = ta.Top_shangchuanfujian()
    ta.Top_shangchuanfujian01(datapath)
    result01 = ta.Topic_shangchuanwenjian02(topicname, datapath)
    #判断用户2申请授权是否成功
    pytest.assume(result01['code'] == '200')
    #判断用户2我申请页面是否有此Topic
    # shenqingdanhao = result01['data']['applyBillCode']
    res3 = ap1.shenqing_Topic(topicname)['data']['records']
    shenqingdanhao = res3[0]['applyBillCode']
    pytest.assume(str(res3[0]['topicCode']) == topicname)
    pytest.assume(res3[0]['auditStatus'] == 'ING')
    #判断用户1的我审批-待审批页面是否存在Topic
    res4 = ap2.shenpi_daishenpi(shenqingdanhao,pageNumber=2)['data']['list']
    # print(res4)
    pytest.assume(str(res4[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res4[0]['approveStatus'] == 'ING')
    # 用户1审批该Topic通过
    res5 = ap2.jieru_shenpi_yes(shenqingdanhao)
    pytest.assume(res5['code'] == '200')
    #用户1的我审批-已审批页面是否存在Topic
    res6 = ap2.shenpi_yishenpi(shenqingdanhao)['data']['list']
    pytest.assume(str(res6[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res6[0]['cusApprovalState'] == 'PASS')
    #运营方审批通过
    res7 = app.shenpi_yes_topic(shenqingdanhao)
    pytest.assume(res7['code'] == '200')
    #用户2的已授权页面是否存在Topic
    res8 = mt.list_topicshouquan(topicname)['data']["records"]
    pytest.assume(res8[0]["topicCode"] == topicname)


#数据授权审批流程
@allure.title('数据授权审批流程')
def test_datashenpi():
    # 用户1创建数据
    xitongname = sy.add_xitong()[1]
    rebody = sy.list_xitong(xitongname)['data']['list']
    xitongid = rebody[0]['id']
    dataname = ds.shujvjiegou(xitongname, xitongid)[1]
    result = md.list_shujvzhuce(dataname)
    data_bianma = result[1]
    result_1 = result[0]['data']['list']
    result_2 = result_1[0]['dataCode']
    pytest.assume(result_2 == data_bianma)

    #用户2申请该数据
    result1 = da.shujvshenqing_list(tableName=data_bianma)['data']["list"]
    apicode = result1[0]["metaTableCode"]
    path = da.shangchuanfujian_shujvxietong()
    da.shangchuanfujian01_shujvxietong(path)
    result01 = da.shangchuanwenjian02_shujvxietong(apicode, path)
    #判断用户2申请授权是否成功
    pytest.assume(result01['code'] == '200')
    #判断用户2我申请页面是否有此数据
    shenqingdanhao = result01['data']['applyBillCode']
    res3 = ap1.shenqing_shujv(shenqingdanhao)['data']['list']
    pytest.assume(str(res3[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res3[0]['approveStatus'] == 'ING')
    #判断用户1的我审批-待审批页面是否存在数据
    res4 = ap2.shenpi_daishenpi(shenqingdanhao)['data']['list']
    # print(res4)
    pytest.assume(str(res4[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res4[0]['approveStatus'] == 'ING')
    # 用户1审批该A数据通过
    res5 = ap2.jieru_shenpi_yes(shenqingdanhao)
    pytest.assume(res5['code'] == '200')
    #用户1的我审批-已审批页面是否存在A数据
    res6 = ap2.shenpi_yishenpi(shenqingdanhao)['data']['list']
    pytest.assume(str(res6[0]['applyBillCode']) == str(shenqingdanhao))
    pytest.assume(res6[0]['cusApprovalState'] == 'PASS')
    #运营方审批通过
    res7 = app.shenpi_yes(shenqingdanhao)
    pytest.assume(res7['code'] == '200')
    #用户2的已授权页面是否存在数据
    res8 = md1.list_shujvshouquan(data_bianma)['data']["list"]
    pytest.assume(res8[0]["dataCode"] == data_bianma)




# 用户1创建API
xitongname = sy.add_xitong()[1]
rebody = sy.list_xitong(xitongname)['data']['list']
serverCode = rebody[0]['serverCode']
result = ap.fabu(serverCode)
print('1...')
print(result)
#断言API是否创建成功
# pytest.assume(result[0]['code'] == '200')
# pytest.assume(result[0]['success'] == True)
#用户2申请该API
result_1 = ap.list_zijianAPI(result[2])['data']['records']
print(result_1)
apicode1 = result_1[0]['apiCode']
print(apicode1)
result1 = aa.list_quanbuAPI(apiCode=apicode1)['data']['records']
apicode = result1[0]['apiCode']
path = aa.shangchuanfujian()
aa.shangchuanfujian01(path)
result2 = aa.shangchuanwenjian02(apicode, path)
#判断用户2申请授权是否成功
print('2...')
print(result2)
# pytest.assume(result2['code'] == '200')
#判断用户2我申请页面是否有此API
shenqingdanhao = result2['data']['applyBillCode']
res3 = ap1.shenqing_API(shenqingdanhao)['data']['list']
print('3...')
print(res3)
# pytest.assume(str(res3[0]['applyBillCode']) == str(shenqingdanhao))
# pytest.assume(res3[0]['approveStatus'] == 'ING')
#判断用户1的我审批-待审批页面是否存在API
res4 = ap2.shenpi_daishenpi(shenqingdanhao)['data']['list']
# print(res4)
print('4...')
print(res4)
# pytest.assume(str(res4[0]['applyBillCode']) == str(shenqingdanhao))
# pytest.assume(res4[0]['approveStatus'] == 'ING')
# 用户1审批该API通过
res5 = ap2.jieru_shenpi_yes(shenqingdanhao)
print('5...')
print(res5)
# pytest.assume(res5['code'] == '200')
#用户1的我审批-已审批页面是否存在API
res6 = ap2.shenpi_yishenpi(shenqingdanhao)['data']['list']
print('6...')
print(res6)
# pytest.assume(str(res6[0]['applyBillCode']) == str(shenqingdanhao))
# pytest.assume(res6[0]['cusApprovalState'] == 'PASS')
#运营方审批通过
res7 = app.shenpi_yes(shenqingdanhao)
print('7...')
print(res7)
# pytest.assume(res7['code'] == '200')
#用户2的已授权页面是否存在API
res8 = aa.list_yishouquanAPI(apiCode=apicode1)['data']["records"]
print('8...')
print(res8)
# pytest.assume(res8[0]["apiCode"] == apicode1)


