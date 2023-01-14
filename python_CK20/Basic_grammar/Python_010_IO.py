#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、字面量（literal）打印与格式化：
定义：以变量或常量给出的原始数据。在程序中可以直接使用字面量
类型：数值型、字符型、布尔型
字面量集合：列表 [list]、元组（tuple）、集合 {set}、字典 {dict_key:dict:value}
特殊字面量：None
"""
"""
字面量插值：就是将变量、常量以及表达式插入的一种技术，可以避免字符串拼接的问题
插值方法1：
1、格式化输出
格式化输出：%的用法：
%d、%i：转换为带符号的十进制整数
%o：转换为带符号的八进制整数
%x、%X：转换为带符号的十六进制整数
%e：转换为科学计数法表示的浮点数（e小写）
%E：转换为科学计数法表示的浮点数（E大写）
%f、%F：转换为十进制浮点数
%g：智能选用%f或%e格式
%G：智能选用%F或%E格式
%c：格式化字符及其ASCII码
%r：使用repr()函数将表达式转换为字符串
%s：使用str()函数将表达式转换为字符串
"""
# 字面量插值方法1：格式化输出
name = 'hogwarts'
age = 3
print("My name is %s,and my age is %d,and num is %.2f" % (name, age, 16.565656565))

# 插值方法2：format()方法
name = 'lili'
age = 26
print("my name is {1},age is {0}{1}  {0}".format(name, age))  # 可填写索引改变顺序，可多次填充

list_a = [1, 2, 3]
dict_a = {'name': 'tom', 'gender': 'male'}
print('my list is {},and my dict is {}'.format(dict_a, list_a))  # 大括号为空时，默认按照顺序填充值

print('my name is {},and my age is {},and my list is {}'.format("li", '17', [1, 2, 3, 4, 5]))
namelist = ['lili', 'tom', 'jerry']
print("my name is {1},her name is {0},his name is {2}".format(*namelist))  # 加*对列表解包后，可按下标传入值
# print('my name is {},her name is {},his name is {}'.format(namelist[1],namelist[2],namelist[3])) #错误写法
print('my name is {},her name is {},his name is {}'.format(*namelist))  # 加个*表示对列表解包,列表元素必须大于或等于须填充数
print('my name is {name},and my age is {gender}'.format(**dict_a))  # 字典解包加**，在{}里指定key，填充对应的value

"""
3、字面量插值方法3：Formatted string literals（缩写为：F-strings），字符串格式化机制（Python版本>=3.6）
官网介绍：https://docs.python.org/3/reference/lexical_analysis.html#f-strings
使用方法：f'{变量名/常量/表达式/函数}'
注意：大括号里可以是表达式/函数/变量/类/方法/常量，不可使用转义符，不能使用\，可以放在大括号外面
"""
name1 = 'lucy'
age1 = 17
mylist = [1, 2, 3, 4]
mydict = {'name': 'lili', 'age': 17, 'hometown': 'yy'}
# 字符串前面加个f，就会寻找引号里大括号里的是否变量/函数/表达式等等，列表元祖字典集合等，可以加索引或者key来指定某个值，无需加*或**解包
print(f"my name is \n{name1},and age is {age1},and my list is {mylist[1]},and my dict is {mydict['name']}")
print(f"my name is {name1.isupper()}")  # 大写函数
print(f"result is {(lambda x: x ** 3)(2)}")  # 大括号里不允许出现冒号，所以必须用小括号括起来
# print(f"result is {(lambda x:x**2) (for x in range(1,11))}")  #写法有误
print(f"my age is {17}")  # 支持传入常量

# f和.format()不可同时使用，否则{}里无法识别是变量，会作为字符串打印
print("my age is {1},her name is {0},his name is {3},tom's name is {2}".format(*mylist))  # 写法错误
