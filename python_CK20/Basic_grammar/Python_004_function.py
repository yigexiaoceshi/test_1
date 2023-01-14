#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
1、函数
    概念：组织好的，可重复使用的，用来实现单一或相关功能的代码段
    优势：提高应用的模块性和代码的重复利用率
    定义：以def关键词开头，后面接函数名称和圆括号()
        a：由冒号的起始
        b：注意缩进
        c：圆括号()中定义参数
        d：函数说明文档：一般为字符串
    return表达式：用来结束函数，选择性的返回一个值给调用方，不写return或者return不写表达式或return None都默认相当于返回None
    注：其实定义在类里面的叫方法，类外面定义的叫函数，说法不同
2、函数的各类参数
3、Lambda表达式
"""


# 函数的定义，位置参数
def function1(a, b, c):  # 函数内部有使用到会高亮，如果函数内部没有使用到是置灰状态，这种传参叫做位置参数，须注意顺序
    """  #添加一对三引号，回车，会自动出现函数的说明文档编辑区域，对函数进行解释说明，入参及返回值
    :param a:
    :param b:
    :return:
    """
    # 使用tab键添加缩进
    print("这是一个函数")
    print("这是一个参数a:", a)
    print("这是一个参数b:", b)
    print("这是一个参数c:", c)
    return a


# 函数的调用
func1 = function1(1, 2, 3)  # 调用函数时，传参的顺序和定义的时候保持一致，位置参数为必传参数
print(func1)  # 返回值在调用的时候需要指定一个变量去接收返回值，不然会被忽略，打印也可以直接将返回值输出
function1(1, 2, 3)


# 默认参数：在"定义"函数的时候使用k=v的形式定义，调用函数时，如果没有传k，则使用默认参数给出的默认值进行调用
def function2(a=1):
    print("参数a的值是：", a)


function2()  # 未传参，使用默认参数值
function2(2)  # 传参则使用传递的参数


# 关键字参数：在"调用"函数时，使用k=v的形式进行传参，在函数"定义"、"调用"中，关键字参数必须跟随在位置参数后面
# 因为位置参数传参必须按照顺序，关键字参数可无顺序，如果以关键字参数打乱位置参数顺序，程序会无法识别
def function3(f, a, b, c, d, e):  # 如果需要同时定义位置参数和关键字参数，位置参数必须放在关键字参数前面
    print("这是关键字参数a", a)
    print("这是关键字参数b", b)
    print("这是关键字参数c", c)
    print("这是关键字参数d", d)
    print("这是关键字参数e", e)
    print("这是位置参数f", f)


function3(6, b=2, a=1, e=5, d=4, c=3)  # 关键字参数可以不按照顺序，位置参数必须按照定义的顺序放在前面


# 特殊参数：仅限关键字参数，在【仅限关键字】形参前面放置一个 *，并以逗号隔开
def function4(a, b, c, *, d):  # 参数d前面加 * ,并以逗号隔开，表明d一定是关键字参数，调用时一定要使用d=value的形式传参
    print("这是位置参数a", a)
    print("这是位置参数b", b)
    print("这是位置参数c", c)
    print("这是关键字参数d", d)


function4(1, 2, 3, d=4)  # 调用时，参数d就必须以d=value的形式传参，因为定义了d一定是关键字参数

"""
Lambda表达式
1、用lambda关键字创建匿名函数，主体是个表达式，不是个代码块，仅能在lambda表达式中封装有限的逻辑
2、格式为"lambda: 参数:传入该参数的表达式"，参数部分理解为传参，该表达式的计算结果作为返回值
"""
function5 = lambda x: x * 2  # 表达式的返回值也是需要print或者赋值给一个变量来接收，不然会被忽略
print(function5(3))


# 类似于
def function6(h):
    return h * 2


print(function6(3))