#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
将字典格式的请求参数转换为yaml格式请求参数，生成yaml文件
"""
import yaml


# 将字典格式转换为yaml数据
def test_yaml():
    # env为数据格式为字典的变量
    env = {
        'default': 'dev',
        'testing-studio': {'dev': '127.0.0.1',
                           'test': '127.0.0.2'}
    }
    # 使用w方式打开一个yaml文件，存在就打开，不存在则创建，用来存放数据
    with open('test_008_yaml', 'w') as file:
        # 往yaml文件里写入数据，该函数传入2个参数，第一个参数data是需要写入的数据，第二个参数stream是写入的目标文件
        # yaml.safe_dump(env, file)
        yaml.safe_dump(data=env, stream=file)
