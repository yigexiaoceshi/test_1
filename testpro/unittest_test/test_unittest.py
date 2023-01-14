# -*- coding:utf-8 -*-
"""
Unittest
1、提供test cases、test suites、test fixtures、test runner相关组件
2、必须先import unittest
3、测试类必须继承 unittest.TestCase
4、测试方法（测试用例）必须以 'test_' 开头
"""
import unittest


class TestStringMethods(unittest.TestCase):  # 继承了unittest的TestCase类后，变成了一个单元测试类

    def setUp(self) -> None:  # 默认返回None，每条测试用例执行之前执行
        print("setup")

    def tearDown(self) -> None:  # 默认返回None，每条测试用例执行之后执行
        print("tearDown")

    @classmethod  # 整个类执行之前执行
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod  # 整个类执行完之后执行
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_abc(self):
        print("abc")

    def defg(self):
        print("defg")

    def test_upper(self):
        print("test_uppeer")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("tes_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
