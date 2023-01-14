# -*- coding:utf-8 -*-
import unittest


class Search:

    def search_fun(self):
        print("search")
        return True


class TestSearch(unittest.TestCase):

    def test_search1(self):
        print("test_search1")
        search = Search()  # 实例化类
        print(search)
        assert True == search.search_fun()  # 先执行右边的表达式得出print("search")，得到返回值和True比较是否通过


"""
1、每个Python的模块（即Python文件）都包含一个内置的__name__变量，该模块被执行的时候，__name__等于文件名（包含后缀.py)
2、__main__始终指向当前模块名称，所以当前模块直接被执行的时候，if __name__ = '__main__'为真，模块内的语句能被执行，被调用时则不为真
"""
if __name__ == "__main__":
    unittest.main()
    print(Search().search_fun())
    # Search.search_fun()
