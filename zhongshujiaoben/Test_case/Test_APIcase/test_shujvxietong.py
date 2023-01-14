

import pytest
import allure
from Customer_platform.API.shujvxietong.shujvzhuce import Data_signin
from Customer_platform.API.shujvxietong.wodeshujv import My_Data
from Customer_platform.API.shujvxietong.shujvyuanmanage import Data_source
from Customer_platform.API.shujvxietong.renwumanage import Data_task
from Customer_platform.API.yewuxietong.xitongjieru import System
from Customer_platform.API.yewuxietong.zijianAPI import Api
from Customer_platform.API.shujvxietong.shujvshenqing import Data_applyfor
from config import *

url1 = jierufang_url
userid1 = userId_jierufang01
token1 = token_jierufang01
ds = Data_signin(url1,userid1,token1)
md = My_Data(url1,userid1,token1)
ds_y = Data_source(url1,userid1,token1)
dt = Data_task(url1,userid1,token1)
sy = System(url1,userid1,token1)
ap = Api(url1,userid1,token1)
da = Data_applyfor(url1,userid1,token1)





@allure.feature("数据协同")
@allure.story('数据注册')
@pytest.mark.datazhuce
class Test_datazhuce:
    #@allure.story('角色管理')
    @allure.title('数据注册接口')
    def test_adddata(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        result = ds.shujvjiegou(xitongname,xitongid)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

@allure.feature("数据协同")
@allure.story('我的数据')
@pytest.mark.wodedata
class Test_I_data:

    @allure.title('查询已注册数据接口')
    def test_listzhucedata(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        dataname = ds.shujvjiegou(xitongname, xitongid)[1]
        result = md.list_shujvzhuce(dataname)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('查询已授权数据接口')
    def test_listshouquandata(self):
        result = md.list_shujvshouquan('11111')
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

@allure.feature("数据协同")
@allure.story('数据源管理')
@pytest.mark.shujvyuanmanage
class Test_shujvyuan_manage:
    @allure.title('新增数据源接口')
    def test_addshujvyuan(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        result = ds_y.add_shujvyuan(xitongid,xitongname)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('查询数据源接口')
    def test_listshujvyuan(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        shujvyuanname = ds_y.add_shujvyuan(xitongid, xitongname)[1]
        result = ds_y.list_shujvyuan(dataSourceName=shujvyuanname)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('编辑数据源接口')
    def test_editshujvyuan(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        shujvyuanname = ds_y.add_shujvyuan(xitongid, xitongname)[1]
        result1 = ds_y.list_shujvyuan(dataSourceName=shujvyuanname)
        result = ds_y.edit_shujvyuan(result1)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('测试数据源接口')
    def test_testcaseshujvyuan(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        shujvyuanname = ds_y.add_shujvyuan(xitongid, xitongname)[1]
        result1 = ds_y.list_shujvyuan(dataSourceName=shujvyuanname)
        result = ds_y.tc_shujvyuan(result1)
        pytest.assume(result == 200)

@allure.feature("数据协同")
@allure.story('任务管理')
@pytest.mark.renwumanage
class Test_renwu_manage:
    @allure.title('新增任务接口')
    def test_addrenwu(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        dataname = ds.shujvjiegou(xitongname, xitongid)[1]
        databianhao1 = md.list_shujvzhuce(dataname)[0]['data']['list']
        databianhao = databianhao1[0]['metaTableCode']

        serverCode = rebody[0]['serverCode']
        apibianmacode = ap.fabu(serverCode)[2]
        result1 = ap.list_zijianAPI(apibianmacode)['data']['records']
        apicode = result1[0]['apiCode']

        result = dt.add_renwu(apicode,dataname,databianhao)[0]
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('查询任务接口')
    def test_listrenwu(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        dataname = ds.shujvjiegou(xitongname, xitongid)[1]
        databianhao1 = md.list_shujvzhuce(dataname)[0]['data']['list']
        databianhao = databianhao1[0]['metaTableCode']

        serverCode = rebody[0]['serverCode']
        apibianmacode = ap.fabu(serverCode)[2]
        result1 = ap.list_zijianAPI(apibianmacode)['data']['records']
        apicode = result1[0]['apiCode']

        taskname = dt.add_renwu(apicode, dataname, databianhao)[1]
        result = dt.list_renwu(taskname)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('停用任务接口')
    def test_stoprenwu(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        dataname = ds.shujvjiegou(xitongname, xitongid)[1]
        databianhao1 = md.list_shujvzhuce(dataname)[0]['data']['list']
        databianhao = databianhao1[0]['metaTableCode']

        serverCode = rebody[0]['serverCode']
        apibianmacode = ap.fabu(serverCode)[2]
        result1 = ap.list_zijianAPI(apibianmacode)['data']['records']
        apicode = result1[0]['apiCode']

        taskname = dt.add_renwu(apicode, dataname, databianhao)[1]
        xvyaoid = dt.list_renwu(taskname)['data']['taskList']
        id = xvyaoid[0]['id']
        taskid = xvyaoid[0]['jobId']
        result = dt.tingyong_renwu(id,taskid)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('启用任务接口')
    def test_qiyongrenwu(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        dataname = ds.shujvjiegou(xitongname, xitongid)[1]
        databianhao1 = md.list_shujvzhuce(dataname)[0]['data']['list']
        databianhao = databianhao1[0]['metaTableCode']

        serverCode = rebody[0]['serverCode']
        apibianmacode = ap.fabu(serverCode)[2]
        result1 = ap.list_zijianAPI(apibianmacode)['data']['records']
        apicode = result1[0]['apiCode']

        taskname = dt.add_renwu(apicode, dataname, databianhao)[1]
        xvyaoid = dt.list_renwu(taskname)['data']['taskList']
        id = xvyaoid[0]['id']
        taskid = xvyaoid[0]['jobId']
        dt.tingyong_renwu(id, taskid)
        result = dt.qiyong_renwu(id, taskid)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('任务执行接口')
    def test_renwuzhixing(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        dataname = ds.shujvjiegou(xitongname, xitongid)[1]
        databianhao1 = md.list_shujvzhuce(dataname)[0]['data']['list']
        databianhao = databianhao1[0]['metaTableCode']

        serverCode = rebody[0]['serverCode']
        apibianmacode = ap.fabu(serverCode)[2]
        result1 = ap.list_zijianAPI(apibianmacode)['data']['records']
        apicode = result1[0]['apiCode']

        taskname = dt.add_renwu(apicode, dataname, databianhao)[1]
        xvyaoid = dt.list_renwu(taskname)['data']['taskList']
        id = xvyaoid[0]['id']
        taskid = xvyaoid[0]['jobId']
        result = dt.zhixing_renwu(id,taskid)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('执行记录查看接口')
    def test_list_renwuzhixing(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        dataname = ds.shujvjiegou(xitongname, xitongid)[1]
        databianhao1 = md.list_shujvzhuce(dataname)[0]['data']['list']
        databianhao = databianhao1[0]['metaTableCode']

        serverCode = rebody[0]['serverCode']
        apibianmacode = ap.fabu(serverCode)[2]
        result1 = ap.list_zijianAPI(apibianmacode)['data']['records']
        apicode = result1[0]['apiCode']

        taskname = dt.add_renwu(apicode, dataname, databianhao)[1]
        xvyaoid = dt.list_renwu(taskname)['data']['taskList']
        id = xvyaoid[0]['id']
        taskid = xvyaoid[0]['jobId']
        dt.zhixing_renwu(id, taskid)

        result = dt.list_zhixingjilu(taskname)
        pytest.assume(str(result['code']) == '200')
        pytest.assume(result['success'] == True)

    @allure.title('停止执行任务接口')
    def test_stop_renwuzhixing(self):
        xitongname = sy.add_xitong()[1]
        rebody = sy.list_xitong(xitongname)['data']['list']
        xitongid = rebody[0]['id']
        dataname = ds.shujvjiegou(xitongname, xitongid)[1]
        databianhao1 = md.list_shujvzhuce(dataname)[0]['data']['list']
        databianhao = databianhao1[0]['metaTableCode']

        serverCode = rebody[0]['serverCode']
        apibianmacode = ap.fabu(serverCode)[2]
        result1 = ap.list_zijianAPI(apibianmacode)['data']['records']
        apicode = result1[0]['apiCode']

        taskname = dt.add_renwu(apicode, dataname, databianhao)[1]
        xvyaoid = dt.list_renwu(taskname)['data']['taskList']
        id = xvyaoid[0]['id']
        taskid = xvyaoid[0]['jobId']
        dt.zhixing_renwu(id, taskid)

        result = dt.stop_zhixing(id)
        pytest.assume(result == 200)

@allure.feature("数据协同")
@allure.story('数据申请')
@pytest.mark.shujvshenqing
class Test_shujvshenqing:
    @allure.title('数据申请授权上传附件接口')
    def test_Fileupload(self):
        path = da.shangchuanfujian_shujvxietong()
        result = da.shangchuanfujian01_shujvxietong(path)
        pytest.assume(result == 200)

    @allure.title('申请授权接口')
    def test_AuthorizationAPI(self):
        result1 = da.shujvshenqing_list(tableName=None)['data']["list"]
        apicode = result1[0]["metaTableCode"]
        path = da.shangchuanfujian_shujvxietong()
        da.shangchuanfujian01_shujvxietong(path)
        result = da.shangchuanwenjian02_shujvxietong(apicode, path)
        pytest.assume(result['code'] == '200')
        # pytest.assume(result['success'] == True)


# result1 = da.shujvshenqing_list(tableName=None)['data']["list"]
# apicode = result1[0]["metaTableCode"]
# path = da.shangchuanfujian_shujvxietong()
# da.shangchuanfujian01_shujvxietong(path)
# result = da.shangchuanwenjian02_shujvxietong(apicode, path)
# print(result)





