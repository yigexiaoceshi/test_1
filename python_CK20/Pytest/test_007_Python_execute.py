#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
用例执行方式1、命令行使用pytest执行用例：
命令行：点击当前文件test_007_Python_execute.py右键，选择open/Terminal，在当前文件目录打开Terminal命令行
pytest test_007_Python_execute.py -vs -x：遇到失败的用例立即停止执行
pytest test_007_Python_execute.py -vs --maxfail=3：失败的用例达到3条(包含3条)，立即停止执行
pytest test_007_Python_execute.py -v：显示执行的详细日志情况
pytest test_007_Python_execute.py -s：打印日志的输出信息
pytest test_007_Python_execute.py -vs -m="标签名"：仅执行装饰器里定义的标签名完全匹配的测试用例
pytest test_007_Python_execute.py -vs -lf：仅支持上一次运行失败的测试用例，如已修复或无失败用例则执行所有用例
pytest test_007_Python_execute.py -vs -ff：优先执行上一次失败的用例，然后执行剩下的成功的用例
"""
import pytest


def test_aaa():
    print("test_aaa被执行")


def test_bbb():
    print("test_bbb被执行")


class TestDemo1:
    def test_ccc(self):
        print("test_ccc被执行")

    def test_ddd(self):
        print("test_ddd被执行")


class TestDemo2:
    @pytest.mark.biaoqian
    def test_eee(self):
        print("test_eee被执行")

    def test_fff(self):
        print("test_fff被执行")


if __name__ == "__main__":
    # 执行当前目录下所有符合规则的用例，包括子目录的模块(模块匹配规则：以"test_"开头，或以"_test"结尾)
    # pytest.main()   #入口模块这么写，执行"python test_*.py"相当于命令行执行了"pytest"
    # 执行某个模块下面的某个类：pytest.main(["test_*.py::class_name",],"-v","-s","-k,"包含Classname或defname")
    # pytest.main(["test_007_Python_execute.py::TestDemo1","-vs"])
    # #执行某个模块下，某个类中的某个方法：pytest.main(["test_*.py::class_name::def_name","-vs","-m","完全匹配的标签名"])
    # pytest.main(["test_007_Python_execute.py::TestDemo2::test_eee","-vs","-m","biaoqian"])
    # #执行某个模块下的某个函数:pytest.main(["test_*.py::test_aaa","-vs"])
    pytest.main(["test_007_Python_execute.py::test_aaa", "-vs"])

"""
用例执行方式2：使用Python解释器执行
函数被调用才能执行，所以要给出执行的入口
有了入口(if __name__ == "__main__"),在命令行可以使用"python test_*.py"直接执行
"""

"""
用例执行方式3、使用"python -m pytest test_*.py"
无需入口，直接在命令行执行，执行单个模块、单个类、类里的方法、类外的函数写法和方式1是一样的，只是前面加了个"python -m"
这种写法其实就是使用"python -m"调用pytest来执行，这种写法后续会在Jenkins中使用较多
"""
