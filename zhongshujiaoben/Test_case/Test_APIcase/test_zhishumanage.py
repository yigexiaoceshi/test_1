import pytest
import allure
from Customer_platform.API.zhishuguanli.zhishuzhuce_API import Index_signin
from Customer_platform.API.zhishuguanli.wodezhishu import My_Index
from Customer_platform.API.zhishuguanli.zhishushenqing import Index_applyfor
from Customer_platform.API.zhishuguanli.zhishuleimu import Index_leimu
from Customer_platform.API.zhishuguanli.zhishuweidu import Index_weidu
from Customer_platform.API.yewuxietong.xitongjieru import System
from Customer_platform.API.yewuxietong.zijianAPI import Api
from config import *

url1 = jierufang_url
userid1 = userId_jierufang01
token1 = token_jierufang01

in_s = Index_signin(url1,userid1,token1)
m_in = My_Index(url1,userid1,token1)
in_a = Index_applyfor(url1,userid1,token1)
in_l = Index_leimu(url1,userid1,token1)
in_w = Index_weidu(url1,userid1,token1)
sy = System(url1,userid1,token1)
ap = Api(url1,userid1,token1)






# @pytest.fixture()
# def test_wodezhishu():
#     xitongname = sy.add_xitong()[1]
#     rebody = sy.list_xitong(xitongname)['data']['list']
#     serverCode = rebody[0]['serverCode']
#     zhishuapicode = ap.add_zhishuAPI(serverCode)[0]['data']
#     xinxi = in_s.zhishujibenxinxi()
#     xiangxixinxi1 = in_s.xiangxixinxi(xinxi[0])
#     in_s.guanlian_api(zhishuapicode)
#     in_s.guanlian_num(xiangxixinxi1, zhishuapicode)
#     result2 = m_in.list_yizhucezhishu(xinxi[1])['data']['list']
#     return result2

@allure.feature("指数管理")
@allure.story('我的指数')
@pytest.mark.wodezhishu
class Test_I_zhishu:

    @pytest.mark.run(order=1)
    @allure.title('指数注册接口')
    def test_addzhishu(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        serverCode = rebody[0]['serverCode']
        zhishuapicode = ap.add_zhishuAPI(serverCode)[0]['data']
        xinxi = in_s.zhishujibenxinxi()[0]
        xiangxixinxi1 = in_s.xiangxixinxi(xinxi)
        in_s.guanlian_api(zhishuapicode)
        result = in_s.guanlian_num(xiangxixinxi1, zhishuapicode)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)



    @pytest.mark.run(order=2)
    @allure.title('我的指数查询（已注册）')
    def test_list_zhucezhishu(self):
        # xitongname = add_xitong()[1]
        # rebody = list_xitong(xitongname)['data']['list']
        # serverCode = rebody[0]['serverCode']
        # zhishuapicode = add_zhishuAPI(serverCode)[0]['data']
        # xinxi = zhishujibenxinxi()
        # xiangxixinxi1 = xiangxixinxi(xinxi[0])
        # guanlian_api(zhishuapicode)
        # guanlian_num(xiangxixinxi1,zhishuapicode)
        result = m_in.list_yizhucezhishu('指数')
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=3)
    @allure.title('我的指数查询（已授权）')
    def test_list_shouquanzhishu(self):
        result = m_in.list_yishouquanzhishu('指数')
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=4)
    @allure.title('指数停用')
    def test_stopzhishu(self):
        zhishu_list01 = m_in.list_yizhucezhishu()['data']['list']
        result3 = zhishu_list01[0]['id']
        result = m_in.stop_zhishu(result3)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=5)
    @allure.title('指数启用')
    def test_qiyongzhishu(self):
        zhishu_list01 = m_in.list_yizhucezhishu()['data']['list']
        result3 = zhishu_list01[0]['id']
        result = m_in.qiyong_zhishu(result3)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

@allure.feature("指数管理")
@allure.story('指数申请')
@pytest.mark.zhishushengqing
class Test_apply_for_zhishu:
    @allure.title('列出申请指数接口')
    def test_list_shengqingzhishu(self):
        result = in_a.list_zhishushengqing(zhishuname=None)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('指数申请上传附件接口')
    def test_shangchuanzhishuwenjian(self):
        dict1 = in_a.zhishushangchuanfujian()
        result = in_a.zhishushangchuanfujian01(dict1)
        pytest.assume(result == 200)

    @allure.title('指数申请授权接口')
    def test_zhishushengqingshouquan(self):
        dict1 = in_a.zhishushangchuanfujian()
        in_a.zhishushangchuanfujian01(dict1)
        zhishucode = in_a.list_zhishushengqing(zhishuname=None)["data"]["records"]
        result = in_a.zhishushangchuanwenjian02(zhishucode[0]["indicatorCode"],dict1)
        pytest.assume(result['code'] == '200')


@pytest.fixture(scope="class")
def test_zhishuleimu():
    in_l.add_zhishuzhidingyileimu()
    id1 = in_l.list_zhishuzidingyileimu()['data']['records']
    return id1

@allure.feature("指数管理")
@allure.story('指数类目')
@pytest.mark.zhishuleimu
class Test_zhishuleimu:
    # @pytest.mark.run(order=1)
    @allure.title('列出标准指数类目接口')
    def test_list_biaozhunzhishuleimu(self):
        result = in_l.list_biaozhunzhishuleimu()
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    # @pytest.mark.run(order=2)
    @allure.title('新增自定义指数类目接口')
    def test_add_zidingyizhishuleimu(self):
        result = in_l.add_zhishuzhidingyileimu()[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    # @pytest.mark.run(order=3)
    @allure.title('查询自定义指数类目接口')
    def test_list_zidingyizhishuleimu(self):
        result = in_l.list_zhishuzidingyileimu()
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    # @pytest.mark.run(order=4)
    @allure.title('编辑自定义指数类目接口')
    def test_edit_zidingyizhishuleimu(self,test_zhishuleimu):
        # add_zhishuzhidingyileimu()
        # id1 = list_zhishuzidingyileimu()['data']['records']
        result = in_l.edit_zhishuzidingyileimu(test_zhishuleimu[-1]['id'])
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    # @pytest.mark.run(order=5)
    @allure.title('删除自定义指数类目接口')
    def test_del_zidingyizhishuleimu(self,test_zhishuleimu):
        # add_zhishuzhidingyileimu()
        # id1 = list_zhishuzidingyileimu()['data']['records']
        result = in_l.del_zhishuzidingyileimu(test_zhishuleimu[-1]['id'])
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)


# @pytest.fixture(scope="class")
# def test_zidingyiweidu():
#     # add_zidingyiweidu()
#     # id1 = list_zidingyiweidu()['data'][0]
#     return add_zidingyiweidu()


@allure.feature("指数管理")
@allure.story('指数维度')
@pytest.mark.zhishuweidu
class Test_zhishuweidu:
    @pytest.mark.run(order=7)
    @allure.title('维度管理-标准维度查询')
    def test_list_biaozhunweidu(self):
        result = in_w.list_biaozhunweidu()
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=6)
    @allure.title('维度管理-新增自定义维度')
    def test_add_zidingyiweidu(self):
        result = in_w.add_zidingyiweidu()[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=8)
    @allure.title('维度管理-列出自定义维度')
    def test_list_zidingyiweidu(self):
        in_w.add_zidingyiweidu()
        result = in_w.list_zidingyiweidu()
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=9)
    @allure.title('维度管理-编辑自定义维度')
    def test_edit_zidingyiweidu(self):
        in_w.add_zidingyiweidu()
        id1 = in_w.list_zidingyiweidu()['data'][0]
        result = in_w.edit_zidingyiweidu(id1['id'])
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=10)
    @allure.title('维度管理-停用自定义维度')
    def test_stop_zidingyiweidu(self):
        in_w.add_zidingyiweidu()
        id1 = in_w.list_zidingyiweidu()['data'][0]
        result = in_w.stop_zidingyiweidu(id1['id'])
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=11)
    @allure.title('维度管理-启用自定义维度')
    def test_qiyong_zidingyiweidu(self):
        in_w.add_zidingyiweidu()
        id1 = in_w.list_zidingyiweidu()['data'][0]
        in_w.stop_zidingyiweidu(id1['id'])
        result = in_w.qiyong_zidingyiweidu(id1['id'])
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)






# result = m_in.list_yizhucezhishu()
# print(result)







