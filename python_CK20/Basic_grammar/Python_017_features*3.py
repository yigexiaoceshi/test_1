#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
面向对象的好处：仅仅是一种编程思想，解决了系统的可维护性，可扩展性，可重用性
"""
"""
python面向对象的三大特性1：封装
"""


class Airplan:
    # 名字
    name = ""
    # 颜色
    color = ""

    def set_name(self, name):
        self.name = name  # 实例传过来的参数给类的默认属性赋值
        print(f"飞机命名为：{self.name}")

    def set_color(self, color):
        self.color = color
        print(f"飞机的颜色是：{self.color}")


# 类的实例化就是创建对象的过程，类可以理解为一个虚拟化对象
Airplan1 = Airplan()
Airplan1.set_name("第一架飞机")
Airplan1.set_color("红色")

Airplan2 = Airplan()
Airplan2.set_name("第二架飞机")
Airplan2.set_color("绿色")

"""
python面向对象的三大特性2：继承
继承：既想拥有某个类的所有属性和方法（通过继承），又希望有自己特定的属性和方法
"""


# 定义一个民用飞机的类别，继承飞机Airplan类，用于父类所有的属性和方法
class CiviAirplan(Airplan):
    weight = ""  # 可以有自己特定的属性

    def load_person(self, number):  # 可以自己特定的方法
        print(f"民用机能载人的数量为：{number}")

    def set_name(self, name):  # 和父类相同的方法，如果都存在默认优先调用自己的，会覆盖父类的方法
        # 下面皮print里的self.name，传入的"民用机1号"并没有赋值给self.name所以还是读取父类的默认值，为空
        print(f"民用机的set_name:{self.name}")  # 这里的使用name和self.name是不是一样的？？？？？？？？

    pass


Airplan3 = CiviAirplan()
Airplan3.set_name("第三架飞机：民用机1")
Airplan3.set_color("粉色")
Airplan3.load_person(100)
print(Airplan3.weight)
Airplan3.set_name("民用机1号")


# 再定义一个军用机的类别
class JunAirplan(Airplan):
    name = "军用机"

    def set_name(self, name):  # 此方法并没有使用self.name = name进行传参赋值，所以self.name还是默认值
        print(f"当前{self.name}的名字为：{name}")


Airplan4 = JunAirplan()
Airplan4.set_name("军用机1号")
print(Airplan4.set_color("紫色"))

"""
小结：
1、继承关系里，父类的改变会影响所有的子类，慎用
2、类的继承，只能继承某个类，不能继承某个实例或者某个类方法
"""

"""
python面向对象的三大特性3：多态
多态：一个或多个子类继承自父类，如果拥有相同的方法或属性，则优先会调用当前类的方法，父类的方法忽略，这也是多形态的提现
注：多态是依附于继承，以继承为基础的一个概念，指的是一些方法和属性的多种形态的体现
"""
