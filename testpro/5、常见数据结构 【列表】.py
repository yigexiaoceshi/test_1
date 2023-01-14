# -*- coding:utf-8 -*-
"""
列表定义：
1、方式：[1,"fsdf","防静电搜副驾驶的",2342343.909]
2、一个列表可以包含多个类型的元素，通常使用时列表内元素都是想同类型的
列表的特性：
1、list.append(x)：在列表末尾加一个元素，相当于 a[len(a):]=[x]
2、list.insert(i,x)：在指定位置插入一个元素。i是要插入的元素的索引；a.insert(0,x)插入列表头部；a.insert(len(a),x)等同于a.append(x)
3、list.remove(x)：移除列表中第一个值为x的元素，如果没有这样的元素，则抛出ValueError异常
4、list.pop([i])：删除列表中指定位置的元素并返回它，如果没有指定位置，a.pop()将会删除并返回列表中的最后一个元素
5、list.sort(key=None,reverse=False)：对列表中的元素进行排序（参数可用于自定义排序，解释请参见sorted())
6、list.reverse()：反转列表中的元素
"""
list_hogwarts = [1, 2, 3]
print(list_hogwarts)
list_hogwarts.append(0)  # 不可指定位置，只能添加在末尾
print(list_hogwarts)
list_hogwarts.append(4)
print(list_hogwarts)
list_hogwarts.append(5)
print(list_hogwarts)
list_hogwarts.insert(1, 6)  # 下表为1的地方插入数字6，原来的下标1的元素往后挪
print(list_hogwarts)
list_hogwarts.remove(0)  # 删除所有值为0的元素
print(list_hogwarts)
list_hogwarts.pop(1)  # 删除指定下标的元素，并返回被删除的元素，仅支持删除一个
print(list_hogwarts)
list_hogwarts.sort()  # 默认升序
print(list_hogwarts)
list_hogwarts.sort(reverse=True)  # 降序排列元素
print(list_hogwarts)
list_hogwarts.reverse()  # 将列表的顺序倒置
print(list_hogwarts)

"""
7、list.clear()：删除列表中所有的元素，相当于 del a[:]
8、list.extend(iterable)：使用可迭代对象中的所有元素来扩展列表，相当于 a[len(a):] = iterable
9、list.index(x[,start[,end]])：返回列表中第一个值为x，从0开始的索引，如果没有这样的元素将会抛出ValueError异常，可选参数start和end是切片
符号，用于将搜索限制为列表的特定子序列，返回的索引是相对于整个序列的开始计算的，而不是start参数
10、list.count(x)：返回元素x在列表中出现的次数
11、list.copy()：返回列表的一个浅拷贝，相当于 a[:]

注意：
1、insert、remove或者sort方法，仅修改列表，没有打印出返回值，默认返回None
2、并非所有的数据都可以排序或者比较（比如不同的数据类型，字符串和数字就无法比较大小或者排序）
"""
# 练习题自己补充

"""
列表推导式：一种更简单的创建列表的方法
练习题：生成一个平方列表，比如[1,4,9...]
1、使用for循环
"""
list_a = []
for i in range(1, 11):
    list_a.append(i ** 2)
print(list_a)
"""
2、使用列表生成式
"""
list_b = [i ** 2 for i in range(1, 11)]  # 每循环一次，就执行i**2这个表达式，执行的结果就作为一个元素
print(list_b)

list_c = [i ** 2 for i in range(1, 11)
          if i != 1]
print(list_c)
"""
3、使用嵌套循环
"""
list_d = []
for e in range(1, 11):
    for f in range(1, 11):
        if e == f:
            list_d.append(e * f)
print(list_d)
# 使用列表推导式
list_e = [n * m for n in range(1, 11)
          for m in range(1, 11)
          if n == m]
print(list_e)

"""
元素可变
"""
list_f = [1, 2, 3]
print(list_f)
list_f[1] = 4
print(list_f)
list_f[2] = "a"
print(list_f)
