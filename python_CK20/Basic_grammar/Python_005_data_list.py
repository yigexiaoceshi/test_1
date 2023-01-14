#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
列表定义：
1、方式：[1,"fsdf","防静电搜副驾驶的",2342343.909,True,(1,2,3),{1,2,3},{"a":"1","b":"2"},[1,2,"ab"]]
2、一个列表可以包含多个类型的元素，通常使用时列表内元素都是相同类型的
3、如果列表中只有一个元素，须在元素后面加逗号","来消除歧义，如：[1,],["aaa",],[[1,2,3],]等
列表的特性：
1、list.append(x)：在列表末尾加一个元素，相当于 list[len(list):]=[x]
2、list.insert(index,x)：在指定位置插入一个元素。index是要插入的元素的索引；list.insert(0,x)插入列表头部；list.insert(len(list),x)等同于list.append(x)
3、list.remove(x)：移除列表中从左至右匹配到的第一个值为x的元素，如果没有这样的元素，则抛出ValueError异常
4、list.pop([index])：删除列表中指定下标的元素并返回它，如果没有指定位置，list.pop()默认删除并返回列表中的最后一个元素
5、list.sort(key=None,reverse=False)：对列表中的元素进行排序（参数可用于自定义排序，解释请参见sorted())
6、list.reverse()：反转列表中的元素
"""
# 列表常用函数
list_hogwarts = [1, 2, 3]
print(list_hogwarts)
list_hogwarts.append(0)  # 不可指定位置，只能添加在末尾
print(list_hogwarts)
list_hogwarts.append(4)
print(list_hogwarts)
list_hogwarts.append(5)
print(list_hogwarts)
list_hogwarts.append(0)
print(list_hogwarts)
list_hogwarts.insert(1, 6)  # 下表为1的地方插入数字6，原来的下标1的元素往后挪
print(list_hogwarts)
list_hogwarts.remove(0)  # 删除从左至右匹配到的第一个0
print(list_hogwarts)
list_hogwarts.pop(1)  # 删除指定下标的元素，并返回被删除的元素，仅支持删除一个
print(list_hogwarts)
list_hogwarts.sort(reverse=False)  # 默认升序，参数取默认值时可以不写:list_hogwarts.sort()
print(list_hogwarts)
list_hogwarts.sort(reverse=True)  # 降序排列元素
print(list_hogwarts)
print(list_hogwarts[3])
list_hogwarts.reverse()  # 将列表的顺序倒置
print(list_hogwarts)

"""
7、list.clear()：删除列表中所有的元素，相当于 del list[:]
8、list.extend(iterable)：在列表末尾一次性追加另一个可迭代对象(可以是元组/列表/集合/字典，字典只会添加每个key)的多个值，相当于 list[len(list):] = iterable
9、list.index(x,start_index,end_index)：返回列表中第一个值等于x的元素的索引(start_index和end_index可不传，2个参数时，默认end_index不传)
如果没有这样的元素将会抛出ValueError异常，可选参数start_index和end_index是切片符号，用于将搜索限制为列表的特定子序列，前闭后开[start_index,end_index)
10、list.count(x)：返回元素x在列表中出现的次数
11、list.copy()：返回列表的一个浅拷贝，相当于 list[:]
12、list[:]：原样复制一个列表
13、cmp(list1.list2)：比较2个列表的元素
14、len(list)：获取列表元素个数，即列表长度
15、max(list)与min(list)：返回列表元素最大值和最小值
16、list(seq)：将元组转换成列表
17、list.insert(index,object)：指定位置插入值
注意：
1、insert、remove或者sort方法，仅修改列表，没有打印出返回值，默认返回None
2、并非所有的数据都可以排序或者比较（比如不同的数据类型，字符串和数字就无法比较大小或者排序）
"""
# 练习题自己补充

"""
列表推导式：一种更简单的创建列表的方法
[表达式 for 变量 in 可迭代对象]：变量依次从可迭代对象中循环取值，通过表达式计算后的结果依次作为元素添加到列表末尾，返回一个列表
"""

"""练习题：生成一个平方列表，比如[1,4,9...]"""
# 1、使用for循环
list_a = []
for i in range(1, 11):
    list_a.append(i ** 2)
print("list_a:", list_a)

# 2、使用列表生成式，可以加判断条件
list_b = [i ** 2 for i in range(1, 11)]  # 每循环一次，就执行i**2这个表达式，执行的结果就作为一个元素
print("list_b:", list_b)

list_c = [i ** 2 for i in range(1, 11)
          if i != 1]
print("list_c:", list_c)

# 3、使用嵌套循环生成列表，可加判断条件
list_d = []
for e in range(1, 11):
    for f in range(1, 11):
        if e == f:
            list_d.append(e * f)
print("list_d:", list_d)
# 使用列表推导式
list_e = [n * m for n in range(1, 11)
          for m in range(1, 11)
          if n == m]
print("list_e:", list_e)

"""
元素可变
"""
list_f = [1, 2, 3]
print("list_f:", list_f)
list_f[1] = 4
print("list_f:", list_f)
list_f[2] = "a"
print("list_f:", list_f)

"""
列表的嵌套
1、列表可以嵌套列表：
2、列表可以嵌套元组
3、列表可以嵌套集合
4、列表可以嵌套字典
注意：如果嵌套的元素只有一个时，直接print不会报错，但是在使用时须在末尾加个逗号消除歧义，如：
list_a = [[1,2,3],]
list_b = [(1,2,3),]
list_c = [{1,2,3},]
list_d = [{key1:key2},]
"""
