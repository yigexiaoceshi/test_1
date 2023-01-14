#!/usr/bin/python3
# -*- coding:utf-8 -*-
import json
from genson import SchemaBuilder
from jsonschema import validate, ValidationError, SchemaError

from interface_autotest.interface.utils.log_utils import logger

"""
JSON数据体结构的验证
"""
def test_genson():
    # 实例化SchemaBuilder
    builder = SchemaBuilder()
    # 添加符合的JSON数据
    builder.add_object({"a": 1, "b": "aaaa", "c": "", "d": None})
    builder.add_object({"a": 1, "b": "bbb", "c": 1})
    # 将对已添加的JSON做过格式校验的schema模板dump到JSON文件里
    json.dump(builder.to_schema(), open("demo_json_schema.json", "w", encoding="utf-8"))


def test_schema_valid():
    # 将schema校验模板load出来，赋值给变量
    _schema = json.load(open("demo_json_schema.json", encoding="utf-8"))
    # 用schema选择的校验模板，校验instance的JSON数据体
    assert schema_validate(obj={"a": 1, "b": "bbb", "c": 1}, schema=_schema)


def schema_validate(obj, schema):
    try:
        # 进行jsonschema的校验尝试
        validate(instance=obj, schema=schema)
    # JSON数据类型校验失败的错误类型
    except ValidationError as e:
        # 从错误堆栈里取出需要的信息，拼接成错误的位置信息
        path = "-->".join(i for i in e.path)
        # 当前错误类型ValidationError详细封装了错误的路径path和详细信息message等
        logger.error(f"验证出错，出错的位置为{path},出错的信息是{e.message}")
        return False
    # schema错误
    except SchemaError as e:
        # 从错误堆栈里取出需要的信息，拼接成错误的位置信息
        path = "-->".join(i for i in e.path)
        # 当前错误类型ValidationError详细封装了错误的路径path和详细信息message等
        logger.error(f"验证出错，出错的位置为{path},出错的信息是{e.message}")
        return False
    # 其他错误类型
    except Exception as e:
        # 当前错误类型Exception没有封装详细的错误路径和信息，没法获取具体的path和message
        logger.error(f"验证出错，出错的信息是{e}")
        return False
    # 未出现错误
    else:
        logger.info(f"校验成功")
        return True
