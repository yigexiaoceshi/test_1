# -*- coding:utf-8 -*-
import unittest


class Test_class_a():
    def test_fun_a(self):
        print('这是未继承unittest的普通类')
        return True


class Test_class_b(unittest.TestCase):
    def test_fun_b(self):
        if Test_class_a().test_fun_a() == True:
            print("测试通过")
        else:
            print('测试不通过')
        print('这是继承了unittest的测试类')


if __name__ == '__main__':
    # unittest.TestCase()
    # unittest.main()
    Test_class_a().test_fun_a()
