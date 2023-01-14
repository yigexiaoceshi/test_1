# -*- coding:utf-8 -*-
import unittest


class test_equal(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpclass")

    def setUp(self) -> None:
        print("setUp")

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 1, "断言不相等")

    def test_notequal(self):
        print('断言不相等')
        self.assertNotEqual(1, 2)

    def test_equalTrue(self):
        print('断言为真')
        self.assertTrue(1 == 1)

    def test_equalFalse(self):
        print('断言为假')
        self.assertFalse(1 == 3)

    def tearDown(self) -> None:
        print('tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')


if __name__ == '__main__':
    # 执行方法1：执行当前文件所有的unittest测试用例
    unittest.TestCase()
# 执行方法2：加入容器中执行，执行指定的测试用例，批量执行
# suite = unittest.TestSuite()
# suite.addTest(test_equal("test_equal"))
# suite.addTest(test_equal("test_notequal"))   #suite.addTest(类名("方法名"))
# suite.addTest(test_equal("test_equalTrue"))
# suite.addTest(test_equal("test_equalFalse"))
# unittest.TextTestRunner().run(suite)
# 执行方法3：执行某个测试类，批量执行测试类
# suite1 = unittest.TestLoader().loadTestsFromTestCase(TestClass_name1)
# suite2 = unittest.TestLoader().loadTestsFromTestCase(TestClass_name2)
# suite = unittest.TestSuite([suite1,suite2])
# unittest.TextTestRunner(verbosity=2).run(suite)  #verbosity:执行测试套件个数
# suite1 = unittest.TestLoader().loadTestsFromTestCase(test_equal)
# suite = unittest.TestSuite(suite1)
# unittest.TextTestRunner().run(suite)
# 执行方法4：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例，discover可以一次性调用多个脚本
# test_dir = "./test_case"   #被调用测试脚本的路径
# discover = unittest.defaultTestLoader.discover(test_dir,pattern = "test*.py")   #pattern是在指定文件里用例名称匹配的规则
# unittest.TextTestRunner(verbosity=2).run(discover)
# 执行方法5：导入htmetestrunner，生成带日志的测试报告
# http://tungwaiyip.info/software/HTMLTestRunner.html   #Python2的版本
# https://github.com/huilansame/HTMLTestRunner_PY3      #Python3的版本
