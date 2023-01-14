

import pytest
import allure
from config import *

from Customer_platform.API.xiaoxixietong.TopicZhuce import Topic_signin
from Customer_platform.API.xiaoxixietong.wodeTopic import My_Topic
from Customer_platform.API.xiaoxixietong.TopicShenqing import Topic_applyfor
from Customer_platform.API.yewuxietong.xitongjieru import System



url1 = jierufang_url
userid1 = userId_jierufang01
token1 = token_jierufang01
sy = System(url1,userid1,token1)
ts = Topic_signin(url1,userid1,token1)
mt = My_Topic(url1,userid1,token1)
ta = Topic_applyfor(url1,userid1,token1)

@allure.feature("消息协同")
@allure.story('Topic注册')
@pytest.mark.topiczhuce
class Test_topiczhuce:
    #@allure.story('角色管理')
    @allure.title('Topic注册接口')
    def test_addtopic(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        result = ts.add_topic(xitongid)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

@allure.feature("消息协同")
@allure.story('我的Topic')
@pytest.mark.wodetopic
class Test_wodetopic:

    @allure.title('Topic查询(注册)接口')
    def test_listzhucetopic(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        topicname = ts.add_topic(xitongid)[1]
        result = mt.list_topiczhuce(topicname)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('Topic查询(已授权)接口')
    def test_listshouquantopic(self):
        result = mt.list_topicshouquan('aaaaaa')
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('Topic查询(订阅中)接口')
    def test_listdingyuetopic(self):
        result = mt.list_topicdingyue('aaaaaa')
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('Topic编辑接口')
    def test_edittopic(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        topicname = ts.add_topic(xitongid)[1]
        result = mt.edit_topic(topicname)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

@allure.feature("消息协同")
@allure.story('Topic申请')
@pytest.mark.topicshengqing
class Test_topicshengqing:
    @allure.title('Topic上传文件接口')
    def test_shangchuantopic(self):
        datapath = ta.Top_shangchuanfujian()
        result = ta.Top_shangchuanfujian01(datapath)
        pytest.assume(result == 200)

    @allure.title('Topic申请授权接口')
    def test_topicshengqingshouquan(self):
        list1 = ta.list_suoyoutopic()['data']['records']
        list2 = [i for i in list1 if i['apply'] == True]
        topiccode = list2[0]['topicCode']
        datapath = ta.Top_shangchuanfujian()
        ta.Top_shangchuanfujian01(datapath)
        result = ta.Topic_shangchuanwenjian02(topiccode,datapath)
        pytest.assume(result['code'] == '200')



