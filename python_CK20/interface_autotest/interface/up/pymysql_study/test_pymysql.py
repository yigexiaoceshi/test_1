#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
数据库操作可封装成一个类
增删改查可分别封装成四个独立方法
"""
import pymysql
import requests

from interface_autotest.interface.utils.log_utils import logger


def query_db(sql):
    # 建立与数据库的连接
    conn = pymysql.connect(
        host="", port=3306, database="", user="", password="", charset="utf8"
    )
    # 创建游标
    cursor = conn.cursor()
    # 使用游标执行sql语句
    cursor.execute(sql)
    # 获取返回的所有数据，存入datas
    datas = cursor.fetchall()
    # 打印日志，得到获取到的数据的总行数
    logger.info(f"获取数据的行数{cursor.rowcount}")
    # 关闭游标
    cursor.close()
    # 断开数据库连接
    conn.close()
    # 返回获取到的数据
    return datas


def test_register():
    phone = "13888888888"
    json_data = {
        "phone": phone,
        "password": "123456",
        "name": "张三1"
    }
    # 启动demo_server的服务，获取服务器地址，拼接注册接口资源路径
    r = requests.post(url="http://127.0.0.1:5000/register", json=json_data)
    print(r.text)
    assert r.json().get["errcode"] == 0
    # 定义一条sql（当前sql语句使用了字面量替换，不符合pycharm的规范，本身并无问题）
    sql = f"select * from user_info where user_info.phone='{phone}'"
    # 调用上面的query_db方法，传入sql获取执行完sql后得到的数据
    dat = query_db(sql)
    # 添加打印日志，并断言
    logger.info(f"获取数据为：{dat}")
    assert len(dat) == 1  # 获取的数据长度为1
