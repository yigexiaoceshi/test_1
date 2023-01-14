#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
一、Python安装：下载直接安装
注：
1、macOS系统，默认安装Python2.7，安装目录在/usr/bin，直接下载安装的Python3.8默认安装在/usr/local/bin
2、python命令文件在/usr/bin，包含python和python3，命令行输入python默认指向python2解释器，python3指向Python3的解释器，一般不做修改（如果改动python指向Python3，会有很多依赖包无法使用，Python2里的一些语法在Python3里已经去掉）
3、一般通过文件包解压安装，绝大多数都会自动添加path到环境变量，如果需要手动添加，则先查看echo $SHELL，查看shell类型，不同类型shell指向不同的配置文件，比如我的Mac的shell类型是zsh，所以我的path配置：vim ~/.zshrc，配置完成source ~/.zshrc使之生效，然后echo $PATH查看
4、命令行输入python查看是否安装成功，环境变量是否添加好，输入 python -V 或 python3 -V 查看版本

二、Pycharm安装：安装破解参考网络教程
1、启动pycharm，必须新建或者选择一个项目
2、在项目新增页面，location里填写项目地址（路径可默认），默认选择虚拟环境Virtualenv（也可选择本地环境），会默认填充venv创建的虚拟环境路径，base interpreter解释器下拉选择Python3
3、打开preferences，依次打开Editor / Code Templates / Python Script，配置新增的py文件的模板（#!/usr/bin/python3 #-*-coding:utf-8-*-)

三、pip依赖管理（Python标准库管理器）：
1、一般跟随Python一起安装，命令行输入 pip -V 查看当前pip版本
2、提示当前版本过低时，python3命令：python -m install --upgrade pip 或 pip install --upgrade pip（Python2版本去掉3就是了）
3、pypi托管了大量非常流行的库（www.pypi.org）
4、pip help：查看帮助，pip list：查看已安装的所有包以及版本号
5、安装命令：pip install selenium（默认安装最新版，uninstall为卸载命令），pip install selenium=3.8.0（安装指定版本）
6、国内pip镜像源安装示例：pip3 install jupyter -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com（-i参数是指定镜像源）
    阿里云：https://mirrors.aliyun.com/pypi/simple
    清华：https://pypi.tuna.tsinghua.edu.cn/simple
    豆瓣：http://pypi/douban.com/simple
"""

print("hello python!")
print("Hello Pycharm！！")

print(dict({(1, (4, 5, 6)), ((1, 2, 3), "abc")}))
