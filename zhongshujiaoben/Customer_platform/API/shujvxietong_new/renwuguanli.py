#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests,json
from config import *
from faker import Factory
fake=Factory.create()

#新增任务
def addtask():
    taskCode="api+"+fake.first_name()
    url=f'{test_customer_url}/api/v4/dc/taskManage/addTask'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"41"}
    data={
        "taskCode":taskCode ,
        "taskName": "接口自动化数据",
        "dataFaultTolerance": 3,
        "executorFailRetryCount": 3,
        "executorTimeout": 30,
        "taskDes": "测试",
        "dataSourceType": 2,
        "taskType": 0,
        "syncRange": "0",
        "maxPageSize": 0,
        "sourceTableName": "py_330108_015_apply_form",
        "incrSyncCondition": "form_code",
        "whereParams": "",
        "primaryKeyConflictStrategy": 0,
        "dataSourceCode": "py_330108_015",
        "columnMapDTOList": [{
            "sourceColumnName": "id",
            "sourceDataType": "int",
            "targetColumnName": "id",
            "targetDataType": "integer"
        }, {
            "sourceColumnName": "policy_code",
            "sourceDataType": "String",
            "targetColumnName": "name",
            "targetDataType": "string"
        }],
        "targetTableName": "测试多线程1",
        "targetTableCode": "20201124992271245"
    }
    res=requests.post(url,headers=header,data=json.dumps(data))
    print(taskCode)
    return  res.json(),taskCode
# print(addtask())


#任务查询
def chaxun_task():
    url=f'{test_customer_url}/api/v4/dc/taskManage/taskList'
    header={"Content-Type":"application/json;charset=UTF-8","userId":"41"}
    data={
        "taskCode": None,
        "size": 100,
        "page": 1
    }
    res=requests.post(url,headers=header,data=json.dumps(data)).json()
    res01=res["data"]["taskList"]
    list1=[]
    for i in res01:
        id=i["id"]
        taskID=i["jobId"]
        tuple1=(id,taskID)
        list1.append(tuple1)
    # print(list1)
    return list1,res
# print(chaxun_task())

#执行任务
def zhixing_task(chaxun_task):
    url=f'{test_customer_url}/api/v4/dc/taskManage/executeTask?'
    header={"userId":"41"}
    data={"id":chaxun_task[0],
          "taskID":chaxun_task[1]}
    res=requests.post(url,headers=header,data=data)
    return res.json()
# print(zhixing_task(chaxun_task()))


for i in chaxun_task()[0]:
    print(zhixing_task(i))
