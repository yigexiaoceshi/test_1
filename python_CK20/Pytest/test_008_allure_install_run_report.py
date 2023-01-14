#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、安装allure：依赖于Java环境
安装方法1、下载allure2.7.zip包，解压，将bin目录配置到环境变量即可（Windows和Mac通用）
    下载地址：https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/
安装方法2：brew install allure
    官网地址：http://allure.qatoos.ru/
    文档：https://docs.qameta.io/allure/#
安装成功：命令行直接输入"allure"显示帮助文档就OK了

2、安装allure-pytest：安装好该插件才可以使用装饰器
    命令行：pip install allure-pytest
    pycharm安装，注意安装allure-pytest，而不是pytest-allure
"""
import pytest
import allure

# @allure.feature("搜索模块")
# class TestSearch():
#     def test_case1(self):
#         print("case1")
#     def test_case2(self):
#         print("case2")
#
# @allure.feature("登录模块")  #大功能描述
# class TestLogin():
#     @allure.story("登录成功")   #小功能描述
#     def test_login_success(self):
#         with allure.step("步骤1：打开应用"):
#             print("打开应用")
#         with allure.step("步骤二：进入登录页面"):
#             print("进入登录页面")
#         with allure.step("步骤三：输入用户名和密码"):
#             print("输入用户名和密码")
#         print("这是登录：测试用例，登录成功")
#         pass
#     @allure.story("登录失败")
#     def test_login_success_a(self):
#         print("这是登录：测试用例，登录成功")
#         pass
#     @allure.story("用户名缺失")
#     def test_login_failure_a(self):
#         print("用户名缺失")
#         pass
#     @allure.story("密码缺失")
#     def test_login_failure_b(self):
#         with allure.step("点击用户名"):
#             print("请输入用户名")
#         with allure.step("点击密码"):
#             print("请输入密码")
#         print("点击登录")
#         with allure.step("点击登录之后登录失败"):
#             assert "1" == 1
#             print("登录失败")
#         pass
#     @allure.story("登录失败")
#     def test_login_failure_c(self):
#         print("这是登录：测试用例，登录失败")
#         pass
#
#     # allure关联手工测试用例，透出手工测试用例的链接地址，透出到测试报告
#     TEST_CASE_LINK = "http://www.baidu.com"
#     @allure.testcase(TEST_CASE_LINK, "测试链接")
#     def test_with_testcase_link():
#         pass
# if __name__ == "__main__":
#     pytest.main()


"""
执行方式1、无需入口，命令行使用"pytest"
1、pytest test_008_allure_install_run_report.py --allure-features="搜索模块" -vs
2、pytest test_008_allure_install_run_report.py --allure-features="登录模块" -vs --allure-stories="登录失败" (优先执行features，在执行stories)
3、pytest test_008_allure_install_run_report.py --allure-stories="登录成功"
4、搜集测试结果：pytest test_008_allure_install_run_report.py --allure-features="搜索模块" -vs --alluredir=./result，当前目录下生成result目录，等号好像可以使用空格代替
5、将搜集的测试结果生成在线测试报告(目录一定要对应，不能填写不存在的目录)：allure serve ./result/
6、生成HTML格式测试报告：allure generate ./result2，意思是将result2文件夹里收集的测试结果，生成一分HTML格式的测试报告，并放在默认创建一个allure-report的文件夹里面，如果指定目录：allure generate ./resule2 -o my_my_repot.如果my_report目录不存在时会自动创建，如果指定目录不为空，可以使用--clean清空
7、生成的HTML报告让别人访问，可以使用"allure open -h 本机IP地址 -p 指定端口 ./my_report"启动一个Tomcat服务，别人可以使用"IP:端口"的方式访问
"""

"""
执行方式2、添加入口，命令行使用"python"
执行方式3、无需入口，命令行使用"python -m pytest"
这两种方式参考文件"test_007_Python_execute.py"
"""

# allure关联手工测试用例，透出手工测试用例的链接地址，透出到测试报告
# TEST_CASE_LINK  = "http://www.baidu.com"
# @allure.testcase(TEST_CASE_LINK,"测试链接")
# def test_with_testcase_link():
#     pass

"""
给测试用例划分范围/模块/优先级，按照范围执行目前接触到的有四种方式
1、执行的时候添加参数-k，模糊或者完全匹配ClassName和defname
2、添加pytest的mark标签标记或跳过，执行的时候添加—m参数，参考文件test_003_run_testcase.py
3、通过本文件上方pytest的allure.feature/stories按照业务模块分类执行
4、下面是第三种方式：通过allure.severity对测试用例的优先级别进行标记
    用法：在类/方法/函数上方添加装饰器"@pytest.severity(allure.severity_level.TRIVIAL)"，严重等级单词必须大写
        Blocker（阻塞）：中断缺陷（客户端程序无响应，无法执行下一步操作）
        Critical（严重）：临界缺陷（功能点确实）
        Normal（一般严重）：普通缺陷（数值计算错误等）
        Minor（轻微）：次要缺陷（界面错误与UI需求不符）
        Trivial（优化）：轻微缺陷（必输项无提示文案，或者提示文案不规范等）
    执行命令：pytest test_*.py -vs --allure-severities normal,critical，注：严重等级单词必须小写
"""


def test_with_no_severity_label():
    pass


@allure.title("用例标题：测试严重级别为阻塞的用例")
@allure.severity(allure.severity_level.BLOCKER)
def test_with_severity_Blocker1():
    pass


@allure.severity(allure.severity_level.BLOCKER)
def test_with_severity_Blocker2():
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_with_severity_Critical():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_severity_Normal():
    pass


@allure.severity(allure.severity_level.MINOR)
def test_with_severity_Minor():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_severity_Trivial():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_severity_normal_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_severity_normal_test_class_with_overriding_critical_severity(self):
        pass


if __name__ == "__main__":
    pytest.main()

"""
1、执行：pytest test_008_allure_install_run_report.py --allure-severities="normal" -vs
结果：加了NORMAL等级的函数会被执行，加了NORMAL等级的类里的定义了NORMAL等级的方法和没有定义等级的方法
注意：加了NORMAL等级的类里，定义了其他等级的方法不会被执行，当类和类里的方法都定义了等级时，方法等级优先;

pycharm参数设置：右上角运行历史记录下拉点击"Edit Configurations..."进入当前文件运行设置页面，
左侧可选择运行的历史记录的py文件，选中某个文件，右侧会自动显示当前文件的路径(Target里的Script path),
在"Python interpreter"里显示的是关联的Python版本，在"Working directory"里显示的事当前工作目录(pwd),
在"Additional Arguments"里设置当前文件在当前工作目录下使用当前版本Python运行时的默认参数，然后命令行
只需要输入"pytest test_*.py"文件就会自动带上默认参数

命令行运行多个文件：pytest test_*.py test_**.py --allure-severity="normal" -vs
"""
