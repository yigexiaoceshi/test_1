#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Person():
    name = "name1"

    def __init__(self, name):  # 创建实例化对象的时候调用，此时self理解为实例化对象zhang_3
        self.name = name  # 将传入的"zhang_3"赋值给实例化对象的属性值self.name（此时的self.name等于zhang_3.name）

    @classmethod  # 加入装饰器后，eat方法变为类方法
    def eat(self):  # 类方法的self参数就理解为类本身，所以下方的print里self.name就是类变量
        print(f"{self.name}正在eating.")


Person.eat()
#
# zhang_3 = Person("张三")
# zhang_3.eat()
# print(zhang_3.name)
