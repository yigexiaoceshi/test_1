import pytest
import allure
from Customer_platform.API.kongzhitai.zhanghaoquanxian.RoleManagement import Role
from Customer_platform.API.kongzhitai.zhanghaoquanxian.AccountManagement import Account
from Customer_platform.API.kongzhitai.anquanguanli.KeyManagement import Key
from Customer_platform.API.kongzhitai.woshenqingde.APIshouquan import api
from Customer_platform.API.kongzhitai.woshenqingde.shujvshouquan import shujv
from Customer_platform.API.kongzhitai.woshenqingde.zhishushouquan import zhishu
from Customer_platform.API.kongzhitai.woshenqingde.topicshouquan import topic
from Customer_platform.API.kongzhitai.ziyuan_guifan.category import category
# import json

from config import *

url1 = jierufang_url
userid1 = userId_jierufang01
token1 = token_jierufang01
ro = Role(url1, userid1, token1)
ac = Account(url1, userid1, token1)
ke = Key(url1, userid1, token1)
ap = api(url1, userid1, token1)
sj = shujv(url1, userid1, token1)
zs = zhishu(url1, userid1, token1)
to = topic(url1, userid1, token1)
zy = category(url1, userid1, username01, token1)


@pytest.fixture(scope='class')
def test_APIshouquan():
    danhao = ap.APIshouquan()
    return danhao


@allure.epic("控制台")
@allure.feature("审批流程")
@pytest.mark.shenpi
# @allure.story("我申请的")
@allure.story("API授权")
class Test_apishouquan:

    @allure.title("单号查询")
    # @pytest.mark.run(order=1)
    def test_apishouquan(self, test_APIshouquan):
        # print(test_APIshouquan)
        result = ap.APIshouquanchaxun(test_APIshouquan)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('授权详情')
    def test_apishouquanxiangqing(self, test_APIshouquan):
        result = ap.chakanxiangqing(test_APIshouquan)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('查看附件')
    def test_apifujian(self, test_APIshouquan):
        result1 = ap.chakanxiangqing(test_APIshouquan)[2]
        result = ap.see_fujian(result1)
        pytest.assume(result == 200)

    @allure.title('查看API详情')
    def test_apixiangqing(self, test_APIshouquan):
        result1 = ap.chakanxiangqing(test_APIshouquan)[1]
        result = ap.api_xiangqing(result1)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)


@pytest.fixture(scope='class')
def test_topic_Huoqudanhao():
    shujvdanhao = to.topichuoqu()
    return shujvdanhao


@allure.epic('控制台')
@allure.feature('审批流程')
@pytest.mark.shenpi
class Test_topic:
    @allure.story('消息协同')
    @allure.title('单号查询')
    def test_tochaxun(self, test_topic_Huoqudanhao):
        result = to.danhaochaxun(test_topic_Huoqudanhao)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('消息协同')
    @allure.title('查看详情')
    def test_toxiangqing(self, test_topic_Huoqudanhao):
        result = to.seexiangqing(test_topic_Huoqudanhao)[2]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('消息协同')
    @allure.title('topic详情')
    def test_topic_xiangq(self, test_topic_Huoqudanhao):
        result = to.seexiangqing(test_topic_Huoqudanhao)[0]
        result1 = to.topic_xiangqing(result)
        pytest.assume(str(result1['code']) == '200')
        pytest.assume(result1['success'] == True)

    @allure.story('消息协同')
    @allure.title('topic_附件')
    def test_topic_fujian(self, test_topic_Huoqudanhao):
        result = to.seexiangqing(test_topic_Huoqudanhao)[1]
        result1 = to.seefujian(result)
        pytest.assume(result1 == 200)


@pytest.fixture(scope='class')
def test_Huoqudanhao():
    danhao = sj.huoqudanhao()
    return danhao


@allure.epic('控制台')
@allure.feature('审批流程')
@pytest.mark.shenpi
class Test_shujvxietong:
    @allure.story('数据授权')
    @allure.title('单号查询')
    def test_sjchaxun(self, test_Huoqudanhao):
        result = sj.shujvdanhaochaxun(test_Huoqudanhao)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('数据授权')
    @allure.title('查看详情')
    def test_sjxiangqing(self, test_Huoqudanhao):
        result = sj.seexiangqing(test_Huoqudanhao)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('数据授权')
    @allure.title('查看附件')
    def test_sjfujian(self, test_Huoqudanhao):
        result = sj.seexiangqing(test_Huoqudanhao)[1]
        result1 = sj.seefujian(result)
        pytest.assume(result1 == 200)


@pytest.fixture(scope='class')
def test_Zhishudanaho():
    zsdanhao = zs.huoqudanhao()
    return zsdanhao


@allure.epic('控制台')
@allure.feature('审批流程')
class Test_zhishu:
    @allure.story('指数管理')
    @allure.title('单号查询')
    def test_zschaxun(self, test_Zhishudanaho):
        result = zs.zhishuchaxun(test_Zhishudanaho)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('指数管理')
    @allure.title('查看详情')
    def test_zsxiangq(self, test_Zhishudanaho):
        result = zs.chakanxiangqing(test_Zhishudanaho)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('指数管理')
    @allure.title('查看附件')
    def test_zsfujian(self, test_Zhishudanaho):
        result = zs.chakanxiangqing(test_Zhishudanaho)[1]
        fujian = zs.chakanfujian(result)
        pytest.assume(fujian == 200)


# @allure.feature('中枢系统控制台')
@pytest.fixture(scope='class')
def test_role():
    rolename = ro.add_role()
    return rolename


@allure.epic('控制台')
@allure.feature('账号权限')
class Test_RoleManage:
    # @allure.story('角色管理')
    @allure.story('角色管理')
    @pytest.mark.run(order=1)
    @allure.title('新增角色接口')
    def test_addrole(self, test_role):
        # print(test_role)
        # ro = Role(kaifa_jierufang_url, userId_jierufang01, token_jierufang)
        result = test_role[0]
        # print(result)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=2)
    @allure.story('角色管理')
    @allure.title('查询角色接口')
    def test_listrole(self, test_role):
        # rolename = add_role()[1]
        result = ro.list_role(test_role[1])
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=3)
    @allure.story('角色管理')
    @allure.title('编辑角色接口')
    def test_editrole(self, test_role):
        # rolename = add_role()[1]
        roleid = ro.list_role(test_role[1])['data']['items']
        roleid1 = roleid[0]['id']
        result = ro.edit_role(f'角色{requestTime}', roleid1)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=4)
    @allure.story('角色管理')
    @allure.title('删除角色接口')
    def test_delrole(self, test_role):
        # rolename = ro.add_role()[1]
        roleid = ro.list_role(test_role[1])['data']['items']
        roleid1 = roleid[0]['id']
        result = ro.del_role(roleid1)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)


@pytest.fixture(scope="class")
def test_account():
    loginname = ac.add_account()
    return loginname


@allure.epic('控制台')
@allure.feature('账号权限')
@pytest.mark.account
class Test_AccountManage:

    # @pytest.mark.run(order=1)
    @allure.story('账号管理')
    @allure.title('新增账号接口')
    def test_addaccount(self, test_account):
        result = test_account[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('账号管理')
    @allure.title('查询账号接口')
    def test_listaccount(self, test_account):
        # loginname = add_account()[1]
        result = ac.list_account(test_account[1])
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('账号管理')
    @allure.title('查看账号详情接口')
    def test_accountparticulars(self, test_account):
        # loginname = add_account()[1]
        accountid = ac.list_account(test_account[1])['data']['items']
        accountid1 = accountid[0]['id']
        result = ac.details_account(accountid1)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('账号管理')
    @allure.title('编辑账号接口')
    def test_edit_account(self, test_account):
        # loginname = add_account()[1]
        accountid = ac.list_account(test_account[1])
        result = ac.edit_account(accountid)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)


@allure.epic('控制台')
@allure.feature('安全管理')
@pytest.mark.miyao
class Test_MiyaoManage:

    # @allure.story('密钥管理')
    @allure.story('密钥管理')
    @allure.title('查询密钥接口')
    def test_listmiyao(self):
        result = ke.list_key()
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('密钥管理')
    @allure.title('密钥详情接口')
    def test_details_miyao(self):
        result = ke.details_key()
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('密钥管理')
    @allure.title('密钥申请授权接口')
    def test_miyaoshouquan(self):
        guanlian_id = ke.list_guanlianzhanghao()[0]
        result = ke.miyao_shengqingshouquan(guanlian_id, ke.list_suoyouapi(guanlian_id))
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)


@pytest.fixture(scope="class")
def test_gongyao():
    guanlian_id = ke.list_guanlianzhanghao()[1]
    gongyaoname = ke.add_gongyao(guanlian_id)[1]
    return gongyaoname, guanlian_id


@allure.epic('控制台')
@allure.feature('安全管理')
@pytest.mark.gongyao
class Test_GongyaoManage:

    # @allure.story('公钥管理')
    @allure.story('公钥管理')
    @allure.title('上传公钥接口')
    def test_addgongyao(self):
        guanlian_id = ke.list_guanlianzhanghao()[1]
        result = ke.add_gongyao(guanlian_id)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('公钥管理')
    @allure.title('查询公钥接口')
    def test_listgongyao(self, test_gongyao):
        # guanlian_id = list_guanlianzhanghao()[1]
        # gongyaoname = add_gongyao(guanlian_id)[1]
        result = ke.list_gongyao(test_gongyao[0])
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('公钥管理')
    @allure.title('公钥申请授权接口')
    def test_gongyaoshouquan(self, test_gongyao):
        # guanlian_id = list_guanlianzhanghao()[1]
        # gongyaoname = add_gongyao(guanlian_id)[1]
        gongyaoid1 = ke.list_gongyao(test_gongyao[0])['data']['items']
        gongyaoid2 = gongyaoid1[0]['id']
        apicode = ke.list_suoyouapi(test_gongyao[1])
        result = ke.gongyaoshengqingshouquan(gongyaoid2, apicode)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('公钥管理')
    @allure.title('公钥停用接口')
    def test_gongyaotingyong(self, test_gongyao):
        # guanlian_id = list_guanlianzhanghao()[1]
        # gongyaoname = add_gongyao(guanlian_id)[1]
        gongyaoid1 = ke.list_gongyao(test_gongyao[0])['data']['items']
        gongyaoid2 = gongyaoid1[0]['id']
        result = ke.stop_gongyao(gongyaoid2)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.story('公钥管理')
    @allure.title('公钥启用接口')
    def test_gongyaoqiyong(self, test_gongyao):
        # guanlian_id = list_guanlianzhanghao()[1]
        # gongyaoname = add_gongyao(guanlian_id)[1]
        gongyaoid1 = ke.list_gongyao(test_gongyao[0])['data']['items']
        gongyaoid2 = gongyaoid1[0]['id']
        ke.stop_gongyao(gongyaoid2)
        result2 = ke.qiyong_gongyao(gongyaoid2)
        pytest.assume(str(result2['code']) == '200')
        pytest.assume(result2['success'] == True)


@pytest.fixture(scope="class")
def test_cate():
    res = zy.add_category()
    res_cate = res[0]
    name = res[1]
    return res_cate, name


@allure.epic("控制台")
@allure.feature("资源规范")
class Test_category:
    @allure.story("类目规范")
    @allure.title("新增自定义类目")
    def test_add_category(self, test_cate):
        result = test_cate[0]
        pytest.assume(str(result["code"]) == "200")
        pytest.assume(result["success"] == True)

    @allure.story("类目规范")
    @allure.title("获取类目ID")
    def test_category_huoqu(self, test_cate):
        result = zy.cate_huoqu(test_cate[1])[0]
        pytest.assume(str(result["code"]) == "200")
        pytest.assume(result["success"] == True)

    @allure.story("类目规范")
    @allure.title("添加子类目")
    def test_cate_zileimu(self, test_cate):
        id = zy.cate_huoqu(test_cate[1])[1]
        result = zy.cate_zileimu(id)
        pytest.assume(str(result["code"]) == "200")
        pytest.assume(result["success"] == True)

    @allure.story("类目规范")
    @allure.title("编辑类目")
    @allure.description("编辑新增的数据")
    def test_cate_edit(self, test_cate):
        id = zy.cate_huoqu(test_cate[1])[1]
        name = test_cate[1]
        result = zy.cate_edit(name, id)
        pytest.assume(str(result["code"]) == "200")
        pytest.assume(result["success"] == True)

    @allure.story("类目规范")
    @allure.title("停用类目")
    @allure.description("停用新增的类目")
    def test_cate_state(self, test_cate):
        id = zy.cate_huoqu(test_cate[1])[1]
        result = zy.cate_state(id)
        pytest.assume(str(result["code"]) == "200")
        pytest.assume(result["success"] == True)

    @allure.story("类目规范")
    @allure.title("启用类目")
    def test_cate_state_off(self, test_cate):
        id = zy.cate_huoqu(test_cate[1])[1]
        result = zy.cate_state_off(id)
        pytest.assume(str(result["code"]) == "200")
        pytest.assume(result["success"] == True)

    @allure.story("类目规范")
    @allure.title("删除类目")
    def test_cate_delete(self, test_cate):
        id = zy.cate_huoqu(test_cate[1])[1]
        result = zy.cate_delete(id)
        pytest.assume(str(result["code"]) == '200')
        pytest.assume(result["success"] == True)
