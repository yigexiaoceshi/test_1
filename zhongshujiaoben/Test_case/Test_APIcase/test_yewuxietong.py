

import pytest
import allure
from Customer_platform.API.yewuxietong.xitongjieru import System
from Customer_platform.API.yewuxietong.zijianAPI import Api
from Customer_platform.API.yewuxietong.quanbuAPI import All_API
from Customer_platform.API.yewuxietong.APIleimu import API_Leimu
from config import *
url1 = jierufang_url
userid1 = userId_jierufang01
token1 = token_jierufang01

sy = System(url1,userid1,token1)
ap = Api(url1,userid1,token1)
aa = All_API(url1,userid1,token1)
al = API_Leimu(url1,userid1,token1)
@pytest.fixture(scope="class")
def test_xitong():
    xitong_tuple = sy.add_xitong()
    return xitong_tuple

@allure.epic('业务协同')
@allure.feature('系统接入')
@pytest.mark.system
class Test_SystemManage:
    @pytest.mark.run(order=1)
    @allure.title('新增系统接口')
    def test_addxitong(self,test_xitong):
        result = test_xitong[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=2)
    @allure.title('查询系统接口')
    def test_listxitong(self,test_xitong):
        xitongname = test_xitong[1]
        result = sy.list_xitong(xitongname)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=3)
    @allure.title('编辑系统接口')
    def test_editxitong(self,test_xitong):
        xitongname = test_xitong[1]
        rebody = sy.list_xitong(xitongname)
        result = sy.edit_xitong(rebody)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=4)
    @allure.title('系统停用接口')
    def test_stopxitong(self,test_xitong):
        xitongname = test_xitong[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        code = rebody[0]['serverCode']
        result = sy.stop_xitong(code)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=5)
    @allure.title('系统启用接口')
    def test_qiyongxitong(self,test_xitong):
        xitongname = test_xitong[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        code = rebody[0]['serverCode']
        # result1 = stop_xitong(code)
        result = sy.resume_xitong(code)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)


@allure.epic('业务协同')
@pytest.fixture(scope="class")
def test_zijianAPI():
    xitongname = sy.add_xitong()[1]
    rebody = sy.list_xitong(xitongname)['data']['list']
    serverCode = rebody[0]['serverCode']
    zijianAPI_tuple = ap.fabu(serverCode)
    return zijianAPI_tuple

@allure.epic('业务协同')
@allure.feature('自建API')
@pytest.mark.creationAPI
class Test_CreationAPIManage:
    @pytest.mark.run(order=1)
    @allure.title('创建指数API接口')
    def test_addzhishuapi(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        serverCode = rebody[0]['serverCode']
        result = ap.add_zhishuAPI(serverCode)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=2)
    @allure.title('创建业务API接口')
    def test_addyewuapi(self,test_zijianAPI):
        # xitongname = add_xitong()[1]
        # rebody = list_xitong(xitongname)['data']['list']
        # serverCode = rebody[0]['serverCode']
        result = test_zijianAPI[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=3)
    @allure.title('查询API接口')
    def test_listzhishuapi(self,test_zijianAPI):
        # xitongname = add_xitong()[1]
        # rebody = list_xitong(xitongname)['data']['list']
        # serverCode = rebody[0]['serverCode']
        apicode = test_zijianAPI[2]
        result = ap.list_zijianAPI(apicode)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=4)
    @allure.title('查看API详情接口')
    def test_xiangqingzhishuapi(self,test_zijianAPI):
        # xitongname = add_xitong()[1]
        # rebody = list_xitong(xitongname)['data']['list']
        # serverCode = rebody[0]['serverCode']
        apicode = test_zijianAPI[2]
        result1 = ap.list_zijianAPI(apicode)['data']['records']
        apicode1 = result1[0]['id']
        result = ap.xiangqing_API(apicode1)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=5)
    @allure.title('API停用接口')
    def test_stopzhishuapi(self,test_zijianAPI):
        # xitongname = add_xitong()[1]
        # rebody = list_xitong(xitongname)['data']['list']
        # serverCode = rebody[0]['serverCode']
        apicode = test_zijianAPI[2]
        result1 = ap.list_zijianAPI(apicode)['data']['records']
        apiid = result1[0]['id']
        result = ap.stop_API(apiid)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @pytest.mark.run(order=6)
    @allure.title('API启用接口')
    def test_qiyongzhishuapi(self,test_zijianAPI):
        # xitongname = add_xitong()[1]
        # rebody = list_xitong(xitongname)['data']['list']
        # serverCode = rebody[0]['serverCode']
        apicode = test_zijianAPI[2]
        result1 = ap.list_zijianAPI(apicode)['data']['records']
        apiid = result1[0]['id']
        # result2 = stop_API(apiid)
        result = ap.state_API(apiid)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

@allure.epic('业务协同')
@allure.feature('全部API')
@pytest.mark.allAPI
class Test_AllAPIManage:
    @allure.title('列出API接口')
    def test_listallAPI(self):
        result = aa.list_quanbuAPI(apiCode=None)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('申请授权上传附件接口')
    def test_Fileupload(self):
        path = aa.shangchuanfujian()
        result = aa.shangchuanfujian01(path)
        pytest.assume(result == 200)

    @allure.title('申请授权接口')
    def test_AuthorizationAPI(self):
        result1 = aa.list_quanbuAPI(apiCode=None)['data']['records']
        apicode = result1[0]['apiCode']
        path = aa.shangchuanfujian()
        aa.shangchuanfujian01(path)
        result = aa.shangchuanwenjian02(apicode, path)
        pytest.assume(result['code'] == '200')


@pytest.fixture()
def test_quanbuAPI():
    result1 = al.add_zidingyileimu()[1]
    result3 = al.list_zidingyileimu()["data"]["records"]
    leimuid = result3[-1]["id"]
    return leimuid
# print(test_quanbuAPI())

@allure.epic('业务协同')
@allure.feature('API类目')
@pytest.mark.APIleimu
class Test_APIleimuManage:
    # @pytest.mark.run(order=11)
    @allure.title('列出标准类目接口')
    def test_listbiaozhunAPI(self):
        result = al.list_biaozhunleimu(categoryName=None)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    # @pytest.mark.run(order=7)
    @allure.title('新增自定义类目接口')

    def test_addzidingyiAPI(self):
        result = al.add_zidingyileimu()[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    # @pytest.mark.run(order=8)
    @allure.title('查询自定义类目接口')

    def test_listzidingyiAPI(self):
        result1 = al.add_zidingyileimu()[1]
        result = al.list_zidingyileimu(result1)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    # @pytest.mark.run(order=9)
    @allure.title('编辑自定义类目接口')
    def test_editzidingyiAPI(self,test_quanbuAPI):
        # result1 = add_zidingyileimu()[1]
        result = al.edit_zidingyileimu(test_quanbuAPI)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    # @pytest.mark.run(order=10)
    @allure.title('删除自定义类目接口')
    def test_delzidingyiAPI(self,test_quanbuAPI):
        # result1 = add_zidingyileimu()[1]

        result = al.del_zidingyileimu(test_quanbuAPI)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)







