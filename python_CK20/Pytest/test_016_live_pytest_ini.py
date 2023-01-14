#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
通过pytest --help可看到，配置文件有pytest.ini，tox.ini，setup.cfg都可以
Python里pytest将Python底层的日志改写过，很多日志默认被禁用，所以配置文件可以定义这些日志的开关
配置文件里也可以写入常用的标签(markers)，重新定义方法/函数(python_function)，模块(python_files)、类(python_class)、变量等的命名规则等等
[pytest]开头就会自动识别为pytest的配置文件，最好放在项目的根目录下，做全局配置
前面加个英文分号;代表注释
"""

# 例子
# [pytest]
# python_files = test_*
# python_class = Test*
# python_function = test_* *_test
#
# addopts = -vs --alluredir ./result  #给命令行的命令加默认参数，执行pytest命令的时候就不需要再输入

"""日志相关：
Python有个logging模块，import logging之后，可以使用logging.info("")，
logging.warning("")等方法获取一些日志信息
"""

"""
[pytest]
;日志开关 true false
log_cli = true
;日志级别   #命令行输出时使用
log_cli_level = info
;打印详细日志，相当于命令行加 -vs
addopts = --capture=no
;日志格式  #命令行输出时使用
log_cli_format = %(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)
;日志时间格式   #命令行输出时使用
log_cli_date_format = %Y-%m-%d %H:%M:%S
;日志文件位置
log_file = ./log/test.log
;日志文件等级
log_file_level = info
;日志文件格式
log_file_format = %(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)
;日志文件日期格式
log_file_date_format = %Y-%m-%d %H:%M:%S
"""
