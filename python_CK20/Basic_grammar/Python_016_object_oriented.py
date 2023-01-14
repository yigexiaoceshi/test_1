#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
面向过程思想（C语言）：
1、一种以过程为中心的编程思想（按步骤思考并实现）
2、简单的事情
面向对象思想（Java，Python，C++等）：
1、一种更符合人类思维习惯的编程思想
2、面向对象编程开发就是不断的创建对象，使用对象，操作对象完成一些事情
3、复杂的事情（如果按照步骤思考的话会很复杂，通过定义对象，操作对象去完成步骤并实现，其实是有相似想通之处）

面向对象定义：
1、语言层面，封装代码和数据
2、规则层面，对象是一系列可被使用的公共接口
3、概念层面，对象是某种拥有责任的抽象

面向对象程序设计规则：
1、分析有哪些类
2、每个类有哪些属性和行为
3、类与类之间有哪些关联

类、实例、方法、变量
类(class)：抽象的概念，一类事物
方法(function)：类中定义的函数，对外提供的公共服务
类变量：在整个实例化的对象中是公用的
实例引用：实例化一个对象（可理解为是类其中的一个虚拟对象）
实例变量：以"self.变量名"的方式定义的变量
"""


class Person():  # 通过class关键字定义一个人的类别，为了实例化一个具体的实例去使用
    name = "default"  # 类里的属性，就是类变量，代表这个人的类别里的每个对象都有name
    age = 17
    gender = "male"
    weight = 55

    # 定义一个构造函数
    def __init__(self, name, AAA, BBB, CCC):
        # 像下面定义的set_name()和set_age()方法，如果实例化的对象需要自定义多个类属性的值，这种写法太复杂
        # 于是这里定义了一个构造函数，该函数在当前类"每次"被实例化成一个对象时调用，默认没有参数
        # 这里我们可以把实例化需要修改的属性传入属性值参数，在该方法的代码块替换掉类里该参数的默认值就比较方便
        self.name = name  # self.name表示类属性
        self.age = AAA
        self.gender = BBB
        self.weight = CCC
        print("__init__")

    # def set_name(self,name): #这个方法要求传入一个新的name值
    #     self.name = name #self.name代表类的属性值，=右侧的name为传入的新的name值，表示用新传入的值替换原来类里的name值
    #     return name
    # def set_age(self,AAA):
    #     self.age = AAA
    #     return AAA
    def eat(self):  # def定义这个类别所拥有的方法（可理解为能力）
        print("Person类里的对象拥有的能力1：eating")
        return self.name

    @classmethod
    def play(self):
        print("Person类里的对象拥有的能力2：playing")
        print(f"{self.name},正在playing")  # 类方法，self.name的值相当于Person.name

    def study(self):
        print(f'{self.name}正在study')
        print("Person类里的对象拥有的能力3：studying")

    def jump(self):
        print(self.name, "正在jump")
        print("Person类里的对象拥有的能力4：jumping")


# 实例化一个对象，赋值给zhangsan，仅仅是实例化类对象，默认是不需要传参数的，因为构造函数默认没有参数，也就默认不改变类里各种属性的默认值
# 但是上面定义了当前对象实例化的时候需要修改属性的默认值，并且构造函数定义了参数，所以此处需要传参
# 效果和上方注释的定义的两个方法效果一样
zhangsan = Person("张三", 18, "男", 54)
print(zhangsan.name)
# 那如果实例化的对象希望拥有自己独立的属性值，就需要在类里定义一个可以自定义自己属性值的方法（如set_name()）:
# zhangsan.set_name("张三三")  #代码执行到该方法里后，self.name已经被name替换，此时zhangsan.name已经变为了传入的name
# zhangsan.set_age(18)  #同理
print(f"zhangsan的名字是{zhangsan.name}，年龄是{zhangsan.age}")
print(f"zhangsan的性别是{zhangsan.gender},体重是{zhangsan.weight}")

# 再实例化一个对象
lisi = Person("李四", 19, "女", 44)  # 再次调用构造函数
print(f"lisi的姓名是{lisi.name},年龄是{lisi.age},性别是{lisi.gender},体重是{lisi.weight}")
zhangsan.jump()
lisi.study()
zhangsan.play()

"""
类变量name和实例变量self.name的理解：
1、定义：
类变量name：指的是当前人这个类别里的每个对象都拥有一个属性name
实例变量self.name：指的是当前人这个类别里的具体每个实例的name，同样拥有属性name，但是可能属性值不相同
2、访问的区别：
类变量name：通过类访问"Person.name"
实例变量self.name：通过实例访问"zhangsan.name"或"lisi.name"
"""
print(Person.name)  # 类变量，注意Person.name访问的是类变量的值，如果是Person().name表示某个实例的name值，是不相同的
print(zhangsan.name)  # 实例变量
print(lisi.name)  # 实例变量
# 也可以直接通过访问类变量和实例变量的方式修改类变量的默认值和实例变量的值，如下：
# Person.name  = "Lucy"
# zhangsan.name = "张三三三三三三三"
# lisi.name = "李四四四四四四四"
# print(Person.name)
# print(zhangsan.name)
# print(lisi.name)

"""
类方法和实例方法
"""
# Person.eat(self=zhangsan) #类不能直接访问类方法，必须传入一个实例化的对象，参数self代表一个实例
# zhangsan.eat()  #实例方法可以直接访问，默认将已经实例化的对象zhangsan传入该方法
# lisi.eat()
# 那么类如何访问自己模块定义的方法呢？可以在需要访问的方法上方加个装饰器@classmethod，就变成了类方法,如play()
print(Person.play())  # 类能访问该方法
print(zhangsan.play())  # 实例化对象也可以访问该方法

# 疑问：类和实例在访问类方法时，有何区别？（目前从执行结果来看，效果是一样的）
# 即使是实例访问，传入的属性值也都默认是类的默认属性值，不会传入实例的属性值
