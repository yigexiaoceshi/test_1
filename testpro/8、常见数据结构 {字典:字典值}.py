# -*- coding:utf-8 -*-
"""
字典的定义：
1、以"关键字"为索引（键、值）
2、关键字可以是任意不可变类型，通常是字符串或数字
3、如果一个元组质保函字符串、数字或元组，那么这个元组也可以用作关键字
"""
# 字典定义：大括号直接定义字典，为空或者包含有效的键值对
dict_a = {}
print("dict_a的格式是", type(dict_a), "，", "其值为：", dict_a)
# 使用dict(key1=value1,key2=value2)函数创建字典
dict_b = dict(a=1, b=2)
print("dict_b的格式是", type(dict_b), "，", "其值为：", dict_b)

"""
注：
1、函数.fromkeys()传入的第一个参数是元组或者是列表，效果都一样，依次读取其中的元素作为key，传入的第二个元素会区分元组和列表，作为value
2、函数.fromkeys()仅支持传入2个参数，一个作为key，一个作为value，都可以是元组，列表或单个字符串或数字
"""
# 使用函数.fromkeys(key,value)创建字典
dict_d = {}
dict_dd = dict_d.fromkeys((1, 2, 3), ("a", "b", "c"))  # 函数.fromkeys()第一个参数可以是元组，也可以是列表
print(dict_dd)
dict_ddd = dict_d.fromkeys((1, 2, 3), "a")
print(dict_ddd)
dict_dddd = dict_d.fromkeys([1], ("a", "b", "c"))
print("字典dict_dddd为：", dict_dddd)
dict_eeee = dict_d.fromkeys("a", (1, 2, 3))
print("字典dict_eeee为：", dict_eeee)

dict_e = {}
dict_ee = dict_e.fromkeys([1, 2, 3], "a")
print(dict_ee)
dict_eee = dict_e.fromkeys([1, 2, 3], ["a", "b", "c"])
print(dict_eee)

"""
字典指导式
"""
dict_f = {x: x ** 2 for x in range(1, 6)}
print("字典dict_f为：", dict_f)

dict_ff = {y: z for y in range(1, 6)
           for z in range(6, 11)}  # 注：此处以key值所在的主循环体为主，value所在的子循环体只取最后一个值和key组成一对
print("字典dict_ff为：", dict_ff)

"""
字典的内置函数
"""
print(dict_a.keys())  # 获取字典所有的key

print((dict_b.values()))  # 获取字典里的所有的value

print(dict_b.pop("a", "b"))  # 删除key=a的键值对，并且返回这个value值,pop函数只接受key为参数，不接受value值
print(dict_b)  # dict.pop()仅支持接收一个key作为参数，写入多个key也只会删除第一个key对应的键值对，并返回value1

dict_c = dict(a=3, b=4, c=5, d=6)
print("字典dict_c被删除的随机键值对是：", dict_c.popitem())  # 随机删除一个键值对，并返回一个键值对元组
print("字典dict_c为：", dict_c)
