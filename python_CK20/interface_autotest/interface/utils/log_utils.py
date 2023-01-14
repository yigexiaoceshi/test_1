#!/usr/bin/python3
# -*- coding:utf-8 -*-


import logging
import os

from interface_autotest.interface.utils.file_tools import FileTools

# 绑定logging的句柄
logger = logging.getLogger(__name__)  # 理解：被那个py文件调用，就使用哪个py文件的句柄
file_path = os.sep.join([FileTools.get_interface_dir(), "logs"])  # 拼接出logs文件文件夹的路径
# 判断file_path是否存在，不存在则创建
if not os.path.exists(file_path):
    os.mkdir(file_path)
# 拼接log文件夹的路径和句柄
fileHandler = logging.FileHandler(filename=file_path + "/apitest.log", encoding="utf-8")
# 定义日志的格式:当前时间，当前文件名，方法名，第几行，日志级别，具体的日志消息
formatter = logging.Formatter("[%(asctime)s] %(filename)s - %(funcName)s line:%(lineno)d [%(levelname)s]: %(message)s")
# 文件句柄绑定格式：将定义好格式的日志信息绑定到句柄
fileHandler.setFormatter(formatter)
# 如果需要控制台输出日志的话，再定义控制台的句柄
streamHandler = logging.StreamHandler()
# 控制台句柄绑定定义好的日志格式
streamHandler.setFormatter(formatter)
# 设置生效
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
# 设置显示日志的级别，当前设置为INFO则只会输出INFO及以上级别的日志（注意和打印日志的logger.info()不一样）
logger.setLevel(logging.INFO)
