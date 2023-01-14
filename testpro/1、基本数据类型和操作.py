# -*- coding:utf-8 -*-
print("hello")
str_a = 'abc123'
print(str_a)
print(type(str_a))

str_b = "fsfs44\nfsdfdsf"  # 转义\+n为换行意思
print(str_b)

str_b = "fsfs44\\nfsdfdsf"  # 取消转义
print(str_b)

str_b = r"fsfs44\nfsdfdsf"  # 取消转义
print(str_b)

print(str_a + str_b)

var = "abcdefg"  # 索引
print(var[1])

print(var[1:])
print(var[1:5])  # 冒号前面是闭区间，冒号之后为开区间，所以取下标1-4时，[1:5]
print(var[1:5:3])  # 2为步长：start:stop:step

var_list = [1, 2, 3, 4, 5, "a", "b", "c", True]
print(var_list)
print(var_list[-1])  # 取最后一位
print(var_list[2:-2])  # 顺手下标2为数字3，倒数第二开区间字母为c，打印结果应该是【3,4,5,"a","b"】
print(var_list[2::2])  # 顺手下表2的元素（数字3）取到最后，步长为2
