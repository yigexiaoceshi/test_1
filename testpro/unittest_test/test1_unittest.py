# -*- coding:utf-8 -*-
"""
unittest框架结构：
1、setUp用来为每个测试方法准备测试环境，tearDown用来为每个测试方法清理测试环境
2、如果想要所有case执行之前准备一次环境，在所有case执行结束之后再清理环境，可以使用setUpClass()和tearDownClass()，比如数据库的连接及销毁
3、某些方法此次不想执行，可以使用@unittest.skip
4、测试方法必须以"test_"开头
5、执行方式多变：可以执行单一用例，也可以执行全部用例
"""
import unittest


class TestClass(unittest.TestCase):

    @classmethod  # 类级别的方法，所以需要这个装饰器
    def setUpClass(cls):
        print("这是测试整个类前要执行的方法。")

    def setUp(self):
        print("这是每个测试方法执行前运行的方法。")

    def tearDown(self):
        print("这是每个测试方法执行之后运行的方法。")

    def test_first(self):
        print("这是测试方法1，即测试用例。")

    # @unittest.skip("这次不想执行这个测试方法")
    def test_second(self):
        print("这是测试方法2.")

    @classmethod  # 类级别的方法，所以需要这个装饰器
    def tearDownClass(cls):
        print("这是测试整个类之后要执行的方法。")


if __name__ == "__main__":
    unittest.main()
