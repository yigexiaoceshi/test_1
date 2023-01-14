import datetime
import socket
from tkinter.ttk import Combobox

import socks

# socks.set_default_proxy(socks.SOCKS5, "121.199.40.154", 8092)
# socket.socket = socks.socksocket


#杭州生产环境
from wx.lib.masked import combobox
hangzhou_prod_customer_url='http://172.18.110.124'
hangzhou_prod_operation_url='http://172.18.110.124:8080/access-platform/daily-access'
#杭州预发环境
hangzhou_pro_customer_url='http://172.18.110.124:10080'
hangzhou_pro_operation_url='http://172.18.110.60:36209'
#标准演示环境
yanshi_customer_url='http://standard.cspiretech.com:8080'
yanshi_operation_url='http://standard.cspiretech.com:30037'
#标准开发环境
develop_customer_url='http://172.18.111.84:8080'
develop_operation_url='http://172.18.111.66:30037'
#标准测试环境
test_customer_url='http://172.18.109.59:8080'
test_operation_url='http://172.18.109.59:8081'
#部署环境
XXX_customer_url='http://192.156.217.137:18080'
XXX_operation_url='http://192.156.217.137:18081'

# XXX_customer_url='http://192.156.217.141:18080'
# XXX_operation_url='http://192.156.217.141:18081'

#接入方
jierufang_url = yanshi_customer_url
username01 = '周一'
userId_jierufang01=756
token_jierufang01 = 'mockToken'
username02 = '科比'
userId_jierufang02=763
token_jierufang02 = 'mockToken'
#运营
yunying_url = yanshi_operation_url
userId_yunying=72
token_yunying = 'mockToken'
username_yunying='超级管理员'



import time
a = int(time.time()*10)




# print(a)
access_username = 'chenyun'+str(a)
access_quancheng = '我的接入方'+str(a)
access_jiancheng = '接入方'+str(a)

#新密码
newpassword = 'Aa123456'
#技术负责人姓名
techname = '技术大佬001'
#技术负责人手机
techmobile = 18965478596
#技术负责人邮箱
techemail = '18965478596@139.com'
#业务负责人姓名
username = '周文峰'
#业务负责人手机
mobile = 17700000010
#业务负责人电话
telephone = '0571-8446466'


requestTime = int(round(time.time() * 1000))

aaa = int(time.time()/100)

timeArray=time.localtime(aaa)
effectiveTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)




#接入方角色权限表
quanxian_list = [28088,28059,28060,28061,28062,28113,28063,28064,28065,28066,28067,28068,28069,28070,28071,28072,28073,
                 28074,28075,28086,28076,28077,28078,28079,28080,28081,28082,28083,28084,28085,28058,28087,28042,28144,
                 28039,28040,28038,28037,28041,28051,28052,28053,28054,28050,28057,28056,28055,28047,28044,28049,28043,
                 28048,28045,28046,28140]
#运营平台角色权限表
operation_quanxiandian=[25077, 25078, 25079, 25080, 25081, 25082, 25083, 25084, 25085, 25086,
                    25087, 25088, 25089, 25091, 25092, 25093, 25094, 25095, 25096, 25097,
                    25098, 25099, 25100, 25101, 25102, 25103]

#指数API新建POST的JSON格式
json01 = "{\"APIRequestStructure\":{\"post\":{\"json\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"set\":true,\"required\":false},\"properties\":{\"indicatorCycleRange\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"onlyStd\":true},\"properties\":{\"start\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true},\"title\":\"开始时间\"},\"end\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true},\"title\":\"结束时间\"}},\"required\":[\"start\",\"end\"],\"description\":\"可一次获取一个时间段内的指数值，对应值 start、end\",\"title\":\"时间维度范围\",\"dimensions\":[\"1000072;月;1;time\"]},\"indicatorCycle\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":false},\"title\":\"时间维度\",\"description\":\"如果为空，默认返回最新值\"},\"indicatorCycles\":{\"type\":\"array\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"items\":{\"type\":\"string\"},\"description\":\"可一次获取多个时刻指数值\",\"title\":\"时间维度集合\"},\"areaCode\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"title\":\"区域\",\"dimensions\":[\"1000080;市;1;area\"]},\"areaCodes\":{\"type\":\"array\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"items\":{\"type\":\"string\"},\"description\":\"\",\"title\":\"区域范围\"}},\"required\":[\"indicatorCycleRange\",\"areaCode\"]},\"type\":\"json\"}},\"APIResponseStructure\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true},\"defaultData\":{\"data\":{\"object\":{\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}}},\"required\":[\"indicatorCycle\",\"areaCode\"]},\"array\":{\"items\":{\"type\":\"object\",\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}}},\"disabled\":{\"name\":true,\"type\":true,\"del\":true,\"set\":true,\"required\":true},\"required\":[\"indicatorCycle\",\"areaCode\"]}}}},\"properties\":{\"code\":{\"type\":\"string\",\"title\":\"状态码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true}},\"message\":{\"type\":\"string\",\"title\":\"错误信息\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true}},\"success\":{\"type\":\"boolean\",\"title\":\"是否成功\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true}},\"data\":{\"type\":\"object\",\"title\":\"返回数据\",\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true},\"dimensions\":[\"1000074;日;1;time\"]},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true},\"dimensions\":[\"1000080;市;1;area\"]},\"field_2\":{\"type\":\"number\",\"title\":\"asda\",\"dimensions\":[\"1000071;季;1;time\"]}},\"required\":[\"indicatorCycle\",\"areaCode\",\"field_2\"],\"disabled\":{\"name\":true,\"type\":false,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true},\"types\":[\"array\",\"object\"]}},\"required\":[\"code\",\"message\",\"success\",\"data\"]}}"
json03 = "{\"APIRequestStructure\":{\"post\":{\"json\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"set\":true,\"required\":false},\"properties\":{\"indicatorCycleRange\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"onlyStd\":true},\"properties\":{\"start\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true},\"title\":\"开始时间\"},\"end\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true},\"title\":\"结束时间\"}},\"required\":[\"start\",\"end\"],\"description\":\"可一次获取一个时间段内的指数值，对应值 start、end\",\"title\":\"时间维度范围\",\"dimensions\":[\"1000072;月;1;time\"]},\"indicatorCycle\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":false},\"title\":\"时间维度\",\"description\":\"如果为空，默认返回最新值\"},\"indicatorCycles\":{\"type\":\"array\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"items\":{\"type\":\"string\"},\"description\":\"可一次获取多个时刻指数值\",\"title\":\"时间维度集合\"},\"areaCode\":{\"type\":\"string\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"title\":\"区域\",\"dimensions\":[\"1000080;市;1;area\"]},\"areaCodes\":{\"type\":\"array\",\"disabled\":{\"name\":true,\"type\":true,\"title\":true,\"add\":true,\"addChild\":true,\"del\":true,\"set\":true,\"required\":false,\"onlyStd\":true},\"items\":{\"type\":\"string\"},\"description\":\"\",\"title\":\"区域范围\"}},\"required\":[\"indicatorCycleRange\",\"areaCode\"]},\"type\":\"json\"}},\"APIResponseStructure\":{\"type\":\"object\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true},\"defaultData\":{\"data\":{\"object\":{\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}}},\"required\":[\"indicatorCycle\",\"areaCode\"]},\"array\":{\"items\":{\"type\":\"object\",\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true}}},\"disabled\":{\"name\":true,\"type\":true,\"del\":true,\"set\":true,\"required\":true},\"required\":[\"indicatorCycle\",\"areaCode\"]}}}},\"properties\":{\"code\":{\"type\":\"string\",\"title\":\"状态码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true}},\"message\":{\"type\":\"string\",\"title\":\"错误信息\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true}},\"success\":{\"type\":\"boolean\",\"title\":\"是否成功\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true}},\"data\":{\"type\":\"object\",\"title\":\"返回数据\",\"properties\":{\"indicatorCycle\":{\"type\":\"string\",\"title\":\"数据统计周期\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true},\"dimensions\":[\"1000074;日;1;time\"]},\"areaCode\":{\"type\":\"string\",\"title\":\"地区编码\",\"disabled\":{\"name\":true,\"type\":true,\"add\":true,\"del\":true,\"set\":true,\"required\":true},\"dimensions\":[\"1000080;市;1;area\"]},\"field_2\":{\"type\":\"number\",\"title\":\"asda\",\"dimensions\":[\"1000071;季;1;time\"]}},\"required\":[\"indicatorCycle\",\"areaCode\",\"field_2\"],\"disabled\":{\"name\":true,\"type\":false,\"add\":true,\"del\":true,\"set\":true,\"dimension\":true},\"types\":[\"array\",\"object\"]}},\"required\":[\"code\",\"message\",\"success\",\"data\"]}}"

#print(json01)
#业务API新建get的JSON格式
json02 = {"APIResponseStructure":{"type":"object","disabled":{"name":True,"type":True,"del":True,"set":True},"properties":{"code":{"type":"string","disabled":{"name":True,"type":True,"add":True,"del":True,"set":True,"dimension":True}},"messge":{"type":"string","disabled":{"name":True,"type":True,"add":True,"del":True,"set":True,"dimension":True}},"success":{"type":"boolean","disabled":{"name":True,"type":True,"add":True,"del":True,"set":True,"dimension":True}},"data":{"type":"object","properties":{},"disabled":{"name":True,"type":False,"add":True,"del":True,"set":True,"dimension":True}}},"required":["code","messge","success","data"]}}



from faker import  Factory

fake=Factory.create("zh_CN")
# print(fake.phone_number())
# print(fake.file_name(category="image", extension="pdf"))