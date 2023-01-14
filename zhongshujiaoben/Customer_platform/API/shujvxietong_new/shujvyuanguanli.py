#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-

import requests,json
from config import *
import xlrd     #导入第三方模块xlrd


#新增数据源
def add_data(dataSourceCode,dataSourceCnName,dataSourceName):
    url=f'{yanshi_customer_url}/api/v4/dc/metaData/addDataSource'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"757"}
    data={
        "dataSourceType": 1,
        "dataSourceCode": dataSourceCode,
        "dataSourceCnName": "2021政策"+dataSourceCnName,
        "dataSourceDesc": dataSourceCode,
        "dataSourceHost": "172.18.41.197",
        "dataSourcePort": "3306",
        "dataSourceName": dataSourceName,
        "dataSourceUserName": "deploy",
        "dataSourcePassWord": "9R5z43YubJ55"
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res


#获取源头数据
def mysql_dome(dataSourceCode,dataSourceName):
    url=f'{yanshi_customer_url}/api/v4/dc/taskManage/findTableNames'
    header={"userId":"757"}
    data={"dataSourceCode":dataSourceCode,
          "dataSourceName":dataSourceName}
    res=requests.post(url,headers=header,data=data).json()

    excel = xlrd.open_workbook(r'/Users/apple/Desktop/table.xlsx')  # 打开目标表格文件（填写路径）
    sheet = excel.sheets()[0]  # 打开表格文件中的第一张表格，索引从0开始
    nrows = sheet.nrows  # 获取第一张表格的行数赋值给nrows
    # print(nrows)
    table_list=[]
    j = 1
    for i in range(nrows - 1):  # 用一个for循环遍历所有的行数
        # print (sheet.row_values(i))     #打印所有遍历到的行数的内容
        table_name = sheet.cell_value(rowx=j, colx=0)
        j += 1
        # 打开第一张表格的第二列
        if table_name in res["data"]:
            table_list.append(table_name)
    return table_list
# print(mysql_dome("py_3311","centralsystem_service"))

#新增任务
def tongburenwu(taskCode,sourceTableName,dataSourceCode,effTime):
    url=f'{yanshi_customer_url}/api/v4/dc/taskManage/addTask'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"757"}
    data={
        "taskCode": taskCode,
        "executorFailRetryCount": 3,
        "executorTimeout": 30,
        "taskDes": "测试数据",
        "dataSourceType": 2,
        "taskType": 1,
        "syncRange": "0",
        "sourceTableName": sourceTableName,#表名
        "incrSyncCondition": "create_time",
        "primaryKeyConflictStrategy": 0,
        "cronPeriod": "min",
        "taskCron": "0 29/10 * * * ?",
        "planTime":effTime ,
        "dataSourceCode": dataSourceCode,
        "columnMapDTOList": [{
            "sourceColumnName": "apply_name",
            "sourceDataType": "String",
            "targetColumnName": "name",
            "targetDataType": "string"
        }],
        "targetTableName": "数据协同030902",
        "targetTableCode": "20210309679905527"
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    return res
# print(tongburenwu())

excel = xlrd.open_workbook(r'/Users/apple/Desktop/接入方API列表 (1).xlsx')       #打开目标表格文件（填写路径）
sheet = excel.sheets()[0]       #打开表格文件中的第一张表格，索引从0开始
nrows = sheet.nrows     #获取第一张表格的行数赋值给nrows
# print(nrows)
j=1
bbb = 0
for i in range (nrows-1):     #用一个for循环遍历所有的行数
    # print (sheet.row_values(i))     #打印所有遍历到的行数的内容
    data_name=sheet.cell_value(rowx=j, colx=0)
    dataSourceCnName=sheet.cell_value(rowx=j,colx=2)
    # ip=sheet.cell_value(rowx=j, colx=1)
    mysql_name=sheet.cell_value(rowx=j, colx=1)
    # username=sheet.cell_value(rowx=j, colx=3)
    # pard=sheet.cell_value(rowx=j, colx=4)

    aaa = int(time.time()+bbb)
    timeArray = time.localtime(aaa)
    # print(timeArray)
    effTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
    print(effTime)

    add_data(data_name,dataSourceCnName,mysql_name)
    # for i in mysql_dome(data_name,mysql_name):
    #     tongburenwu(data_name,i,data_name,effTime)
    j+=1
    bbb+=120



