#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests

from interface_autotest.interface.utils.log_utils import logger


class BaseApi:
    def __init__(self):
        pass

    def send(self, method, url, tool, **kwargs):
        # 如果使用requests框架，走if分支，使用request是发送接口请求，如果是其他框架，走else分支
        if tool == "requests":
            data = {
                "method": method,
                "url": url
            }
            # 更新参数操作，data里只表明了method和url，如果有字典参数传入，则会解析字典参数**kwargs并更新到data（tool也会解析进来？）
            data.update(kwargs)
            # 打印日志，输出参数
            logger.info(kwargs)
            # 所以下方的data传入时需要进行解包操作，**data，注：此处可以尝试打印data以及**data看看结果
            # return requests.request(**data)  # 调用底层request是的接口发起请求，并且传入参数
            res = requests.request(**data)
            logger.info(res.text)
            return res
        else:
            return True
