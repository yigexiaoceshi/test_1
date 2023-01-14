#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、运行测试用例：
界面化的方式：
运行单个方法/函数/类：在方法左侧的绿色箭头点击右键运行
运行单个文件：在.py文件上点击右键，选择'run'，或者IDE右上角的绿色三角形图标
运行多个文件：选择多个，右键点击，选择'run'
运行一个目录或多个目录：同理选中，右键点击，选择'run'

命令行的方式：
pytest：收集当前目录及其子目录下的所有.py文件中符合pytest命名规范的类、方法/函数，并执行
pytest test.py：当前目录多个py文件，或者子目录下也有符合规范的类、方法/函数，而只需要执行test.py时，使用pytest test.py
pytest test.py::Class_name：运行某个.py文件里的某个类下面所有符合规范的用例
pytest test.py::Class_name::def_name：运行某个.py文件里某个类下面某个符合规范的用例(注：ClassName如果不符合规范，defname符合规范，无法识别)
pytest/py.test 目录名：执行某个指定目录及其子目录下所有.py文件里符合条件的def

2、常用命令行参数：
--help：常用参数列表
-x：用例一旦失败（fail或error），立刻停止执行(示例：pytest test.py -x)
--maxfail=num：用例达到某个值就立刻停止执行(示例：pytest test.py --maxfail=3)
-m(mark)：在用例前加标签，对测试用例进行分类，可按照标签选择性执行
    1、标签加在测试用例前面：@pytest.mark.英文开头标签名
    2、执行语句：pytest -s test_mark_01.py -m=标签名(-m 标签名；-m "标签名"；-m '标签名')
    注：使用"-m=标签名"时，标签名必须和定义的标签名完全匹配，不支持模糊匹配
    3、配置pytest.ini文件，提前注册系统能识别的标签，不然系统识别不到是否内置标签会报警报warning
    4、内置标签：skip(始终跳过不执行)，skipif(特定情况跳过不执行)，xfail(特定情况，产生一个"预期失败"的输出)
        4-1、使用场景1：用例前添加装饰器(@pytest.mark.skip(reason="");@pytest.mark.skipif)
        4-2、使用场景2：代码中添加跳过代码(pytest.skip(reason="备注文案"))，使用pytest里的.skip方法
-k "关键字"：执行"方法或者函数名"里包含某个关键字的测试用(示例：pytest test.py -k 'str' 或 pytest test.py -k "not str")
-v：输出更详细的日志，与 --collect-only 一起使用时，还会打印注释
-s：打印输出日志（一般"-vs"一起使用)
--collect-only：仅收集用例（可展示，带-v会连注释一起收集，带-s会收集print信息），不运行。测试平台，pytest 自动导入功能
使用缓存状态的参数：
--lf：--last-failed，只重新运行故障，所有故障修复之后或者无故障用例，会把所有用例执行一遍
--ff：--failed-first，先运行故障，然后再运行其余的测试

3、 常见运行结果分析：
常用的：fail、error、pass
特殊的：warning、deselect（未被命中，一般按照标签有选择性的执行用例时，就会有命中和未被命中）
"""
# 定义一个基础函数
import sys

import pytest

"""Python里不支持循环导入，即不支持相互导入"""

# def double(a):
#     return a*2
#
# #注：当pycharm默认解释器配置了pytest后，默认只收集test_开头的方法/函数，及Test开头的类，其他的语句块不会执行，如要执行得添加参数(-s)
# print(double("你好"))
# @pytest.mark.int
# def test_double_int():       #整数比较
#     assert 4.0 == double(2)
# @pytest.mark.float
# def test_double_float():     #浮点数比较
#     assert 0.4 == double(0.2)
# @pytest.mark.minus
# def test_double_minus1():    #负数比较
#     assert -4 == double(-2)
# @pytest.mark.minus
# def test_double_minus2():    #负数比较
#     assert -0.4 == double(-0.2)
# def test_double_0():     #比较整数0
#     assert 0 == double(0)
# def test_double_bignum():    #较大数字比较
#     assert 2000 == double(1000)
# @pytest.mark.str
# def test_double_str1():    #字符串比较
#     print("此为第七条用例的打印信息，添加-s参数才会执行print")
#     assert "@#$%@#$%" == double("@#$%")
# @pytest.mark.str
# def test_double_str2():   #字符串比较
#     assert "abcabc" == double("abc")
"""
命令行：点击当前文件test_003_run_testcase.py右键，选择open/Terminal，在当前文件目录打开Terminal命令行
pytest test_003_run_testcase.py -vs -x：遇到失败的用例立即停止执行
pytest test_003_run_testcase.py -vs --maxfail=3：失败的用例达到3条(包含3条)，立即停止执行
pytest test_003_run_testcase.py -v：显示执行的详细日志情况
pytest test_003_run_testcase.py -s：打印日志的输出信息
pytest test_003_run_testcase.py -vs -m="标签名"：仅执行装饰器里定义的标签名完全匹配的测试用例
pytest test_003_run_testcase.py -vs -lf：仅支持上一次运行失败的测试用例，如已修复或无失败用例则执行所有用例
pytest test_003_run_testcase.py -vs -ff：优先执行上一次失败的用例，然后执行剩下的成功的用例
"""


# 添加装饰器使用skip跳过当前用例:
# @pytest.mark.skip
# def test_aaa():
#     print("代码开发未完成，跳过不执行")
#     assert True
# @pytest.mark.skip(reason="自动化代码还未写完，完善后执行，当前跳过不执行")  #跳过的reason会被打印出来
# def test_bbb():
#     print("测试代码未完成，跳过不执行")
#     assert False

# 代码块中添加pytest.skip方法跳过当前用例
# def check_login(): #定义一个方法：检查是否登录，返回True
#     return False
# def test_function():
#     print("start")
#     #添加if条件判断，如果条件成立，则跳过后续步骤，2个print都不会执行
#     if not check_login(): #如果check_login()方法返回True,则if not True返回False，则不会执行下面的跳过语句
#         pytest.skip("当前未登录，跳过后续代码不执行！")
#         print("123")
#     print("end")

# skipif用法：@pytest.mark.skipif(表达式,reason="字符串")
# 解释：如果表达式返回True，则跳过当前用例，打印reason，反之执行
# @pytest.mark.skipif(sys.platform == "darwin",reason="当前平台为Mac，跳过不执行")#表达式返回True
# def test_case1():
#     print("test_case1执行了")
#     assert True
# @pytest.mark.skipif(sys.platform == "win",reason="当前平台为Windows，跳过不执行")#表达式返回False
# def test_case2():
#     print("test_case2执行了")
#     assert True
# @pytest.mark.skipif(sys.version_info<(3,6),reason="当前Python版本小于3.6，跳过不执行")#表达式返回False，当前版本3.8.2
# def test_case3():
#     print("test_case3执行了")
#     assert True

# xfail用法：
# 使用解释器@pytest.mark.xfail(reason="原因说明")，如果用例执行失败，则标记为xfail，意思是早知道你会失败
@pytest.mark.xfail
def test_xxx():
    print("xfail1,test_xxx方法执行了")
    assert 1 == 3  # 断言失败，该用例执行了，但未执行通过，标记为xfail


result = pytest.mark.xfail


@result(reason="该bug开发还未解决，执行一定会不通过，标记为xfail")
def test_yyy():
    print("xfail，test_yyy方法执行了")
    assert 0  # 断言表达式返回False，断言失败，该用例执行了，未执行通过，标记为xfail


# 代码里调用pytest.xfail(reason="原因说明")
def test_mmm():
    print("start testing...")
    pytest.xfail(reason="这个bug还未解决")
    print("end testing...")  # 该语句不会执行了
    assert 1 == 2


def test_nnn():
    print("start testing......")
    pytest.xfail(reason="这个bug也还没有解决")
    print("end testing......")
    assert False
