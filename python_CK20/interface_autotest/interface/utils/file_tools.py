#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os.path

import yaml


class FileTools:
    # 类方法装饰器，类方法无需实例化，直接"类名.方法名()"可以调用类里面的方法，类方法不可使用普通方法，只可以使用类属性，参数cls不是一个对象，而是这个类本身
    @classmethod
    def get_interface_dir(cls):
        # 获取当前文件所在目录的父级目录的父级目录，即interface_autotest目录
        # _path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # print("目录为：", _path)
        # 返回当前文件所在目录的父级目录的父级目录，即interface_autotest目录
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def read_yaml(cls, file_name):
        # 获取interface所在的目录
        _path = cls.get_interface_dir()
        # 拼接路径，得到当前yaml文件所在的路径，os.path.json()和os.sep.json()的区别，讲师推荐使用os.sep.json()
        yaml_path = os.sep.join([_path, "datas", file_name + ".yaml"])
        # print(yaml_path)
        # 打开yaml文件
        with open(yaml_path) as yaml_file:
            # 返回yaml文件流对象
            return yaml.safe_load(yaml_file)


if __name__ == '__main__':
    # 类方法不需要实例化，直接使用"类名.方法名()"即可，测试获取interface地址是否正确
    # print(FileTools.get_interface_dir())
    # 测试获取yaml文件路径是否拼接正确
    print(FileTools.read_yaml("secrets"))
