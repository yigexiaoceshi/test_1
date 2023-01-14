#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
一、变量：
1、一种存储数据的载体，可被读取和修改
2、由字母，数字（不能开头），下划线构成；大小写敏感；不要和关键字和系统保留字冲突

二、常见数字类型（Number）和运算符：
1、int（整型）：
    赋值：=
    加减乘除：+ - * /
    整除：// （对商取整数部分）
    取余：%
    乘方：**
    修改运算优先级：()
    等于和不等于：==  !=
2、float（浮点型）：只要包含小数点，包括正数和负数
"""
# a = 1
# b = 0.2
# print(type(a))
# print(type(b))
# print(1+0.9)
# print(1-0.9)
# print(2*0.9)
# print(9/3)
# print(7%3)
# print(2**4)
# print((2+4)*3)
# print(2==2.0)
# print(3!=3.0)

"""
三、字符串（string）
1、转义符：\
2、忽略转义符：r
3、多个字符串拼接：+
4、索引
5、切片:前闭后开原则，可理解为前闭后开集合，数学符号表示为[2:3)
"""
# str_a = 'abc\ndef'   #\n：转义符后面跟n，代表换行
# str_b = "abc\\ndef"  #两个转移符号在一起，如果后面的转移符号拼接了转义关键字，则取消转义效果
# str_c = r'abc\ndef'  #r拼接字符串，忽略该字符串里所有的转义符号\
# print(str_a,str_b,str_c)
# print(type(str_a),type(str_b),type(str_c))
# print(str_a[2:5]+str_b[1:3]+str_c[4:])  #str_a取下标索引234即c、换行、d；str_b取下标12即bc；str_c取下标4到最后即ndef，进行拼接

# #切片：str_x[start:stop:step]
# str_d = "1234567890"
# #前闭后开原则：[2,9)，即索引下标为2345678，对应字符串中数字为3456789，3为步长，即369
# print(str_d[2:9:3])
# #前闭后开原则一样，下标为2的元素（包含）开始，到倒数第一个元素（不包含）
# print(str_d[2:-1:3])


"""
四、列表:[list}
"""
list_a = [1, 2, "1", "fsfsf", True, [1, "3", 'fsdfs'], (1, 2, "fdd"), {'key1:value1', 'key2:value2'}]
print(type(list_a), list_a)
