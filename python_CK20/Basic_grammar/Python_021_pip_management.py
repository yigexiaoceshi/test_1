#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
pip：Python中的标准库管理器。它允许你安装和管理不属于Python标准库的其他软件包
www.pypi.org：托管了大量非常流行的库
pip常用语法：
pip help：查看常用用法
pip install 包名：安装包
pip install 包名==版本：安装指定版本的包
pip install -U 包名：升级包
pip uninstall：卸载包
pip list：查看已经安装的包的列表
pip download：下载包到本地，手动安装
pip search requests：搜索包
"""

"""
虚拟环境管理：和本地环境互不冲突
1、使用命令行：
使用python3 -m venv tutorial-env创建虚拟环境，在当前用户Users/liyong目录下创建了个tutorial-env的目录
cd tutorial_env进入虚拟环境，就能看到已经初始化好了几个目录
在tutorial_env目录下执行：source bin/activate激活这个虚拟环境，deactivate命令退出虚拟环境
rm -rf tutorial-env 删除该目录，就删除了该虚拟环境

2、在pycharm里直接创建
创建一个新的项目时，选择好虚拟环境所在的目录，可以看到New Virtualenv environment
可选择任意一种虚拟环境类型：Virtualenv,Pipenv,Conda都可以，在选择虚拟环境的管理路径（一般选择默认的）
Base interpreter:选择Python解释器的版本
勾选项1：Inherit global site-packages，继承全局的包，勾选了则可以使用本地环境上所有的依赖包，不勾选则会创建一个全新的env环境
勾选项2：Make available to all projects，应用于所有项目，一般不勾选
勾选项：Existing interpreter，使用已经存在的Python环境，不创建全新的虚拟环境
"""
