#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
一、顺序结构：一条条语句按照顺序执行
二、分支结构：某个判断条件后，只选择其中一条分支去执行
1、关键字：if,elif,else
2、缩进
3、建议尽量扁平化，嵌套分支层次太深影响可读性
"""
# 多重分支示例1：
# a = 0
# if a ==1:
#     print(a==1)
# elif a == 2:
#     print(a==2)
# elif a ==3:
#     print(a==3)
# else:
#     print("a不等于1，2，3")
# 多重分支示例2：
# x = -2
# if x > 0:
#     y = 2*x+2
# elif -1<= x <=0:
#     y = x+1
# elif x<-1:
#     y = 5*x+3
# else:
#     print("以上各分支都不成立！")
# print(y)
# 分支嵌套示例：
# A = -2
# if A<0:
#     if -1<A<0:
#         B = A+1
#     elif A<=-1:   #仅走进了这条分支
#         B = 5*A+3
#     else:
#         print("A肯定大于0")  #没有进入嵌套的else模块，所以该句不打印
#     print("A大于0")  #if模块在走进嵌套的elif时通过，打印该语句
# else:  #if语句通过，else块不执行
#     B = 5*A+3
#     print(B)
# print(B)  #执行打印B

"""简写方式1：代码块1 if 表达式 else 代码块2"""
# 解读：如果if表达式成立，执行代码块1，否则执行代码块2
a, b = 1, 2
print(a) if a == b else print("你好，Python")
# 等同于：
# if a == b:
#     print(a)
# else:
#     print(b)

"""简写方式2：print([a,b][表达式])"""
# 解读：如果后面[]里的表达式返回False，取前面列表里第一个值a(索引下标为0)，为True则取第二个值
x, y, z = 1, 2, 3
z = [x, y][x > 0]
# 等同于：
# if x>0:
#     z = y
# else:
#     z = x
print(x, y, z)

"""简写方式3：变量 = 表达式 and 代码块1 or 代码块2"""
# 解读：如果表达式返回True，执行代码块1，表达式返回False时，变量 = 执行代码块2
c = ''
a = ''
b = "你好，我不为空"
d = c and a or b  # c为空字符串，返回False，执行b，得d = b
print(d)  # 输出"你好，我不为空"
# 等同于：
# if c:
#     d = a
# else:
#     d = b


"""
三、循环结构
1、for in循环：明确知道循环的次数，或者对一个容器进行迭代时推荐使用
2、while循环：要构造不知道具体循环次数的循环结构，可以和else结合使用，主要是通过一个能够产生或者转换出bool值的表达式来控制循环是否继续，表达式的值为True则继续，反之循环结束
3、range函数：可用来产生一个不变的数值序列，通常用在循环中
    写法：range(a,b,c)
    a省略不写时，默认为0，比如：range(101)，产生0-100的整数序列
    b不包含，同样符合前闭后开规则，比如：range(1,101)，产生1-100的整数序列
    c为步长，比如想产生1-100之间的偶数，可以这样写：range(2,101,2)，1-100的奇数可以这么写：range(1,101,2) 
4、break关键字：跳出for和while的"循环体"，循环体的任何语句不再执行
5、continue关键字：跳出当前"循环块"中剩余的语句，继续下一轮循环
"""
# for-in循环示例1：计算整数1~100的和
# Number = 0  #Number初始值只能赋值数值0，如果赋值数值1的话，则会在for-in第一个循环里多加一个1，就要写成range(2,101)
# for l in range(1,101):
#     Number = Number + l
# print(Number)
# for-in循环示例2：加入分支结构实现1~100之间的偶数之和
# Number1 = 0
# for n in range(0,101):
#     if n%2 == 0:
#         Number1 = Number1 + n
#     else:
#         print(n,"为奇数")
# print(Number1)
# for-in循环示例3：使用Python实现1~100的偶数求和
# Number2 = 0
# for m in range(2,101,2):
#     Number2 = Number2 + m
# print(Number2)

# while-else循环示例：如果while语句冒号后面只有一行语句，可以直接写在冒号后面，写做一行
# a = 1
# while a == 1:
#     print("a==1")
#     a = a+1   #等同于：a += 1
# else:
#     print("a不等于1")
#     print(a)

# break示例：
# k = []
# for i in range(1,11):
#     k.append(i)
#     if i == 5:
#         break
#     print(i,end='')
#     print(k)
# continue示例
# for j in range(1,11):
#     if j == 5:
#         continue
#     print(j,end='')

# 练习1：乘法口诀表
"""
思路：
1、第一个值第一次取1，第二次取2，一直到10，所以range(1,11)
2、p=1时，q取1，p=2时，q要取1和2，p=3时，q要取1和2和3，依次类推，所以q的取值从1开始，循环次数和p相同，因为range(a,b)函数前开后闭区间的原因，所以b得+1，得range(1,p+1)
3、每一个嵌套循环循环一次，就平铺一次打印数据，所以加个空格更美观
4、每个嵌套循环完成，进入上一级循环，最好回车换行一次，更加美观，所以在第一个循环的print里加了end="    "
"""
# aa = "  "
# for p in range(1,11):
#     for q in range(p,11):
#         result = p*q
#         print(q,"*",p,"=",result,aa,end='')
#     print()
#
for i in range(1, 11):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='  ')
    print()
# 练习2：冒泡排序从小到大排列
"""
思路：
1、取下标做2个嵌套循环，取第一个值和第二个值比，小的往前靠，第二个和第三个比，小的往前靠，以此类推
2、所以第一个循环，第一次取值0须比较7次，取1须比较6次，类推取6时比较1次就不用取索引7了，第一个循环用来控制比较次数，即"range(7)",或"range(len(a)-1)"
3、k=0时，h分别要取值0和1比较，1和2，2和3，3和4，4和5，5和6，6和7，所以h第一个循环比较7次，且h从0到6和h+1做比较
4、从第3点得出，k取0时，h取0123456，k取1时，h取012345，所以h取值range(0,len(a)-1-k)
"""
a = [3, 5, 7, 2, 71, 1, 12, 4.5]
# print(len(a))
for k in range(len(a) - 1):  # range(7)
    # print(k)
    for h in range(0, len(a) - k - 1):  # range(0,6-k)
        if a[h] > a[h + 1]:
            a[h], a[h + 1] = a[h + 1], a[h]
        else:
            pass
print(a)
# 练习3：猜数字游戏，电脑给出1~100随机数，由人输入一个值与之比较，分别给出提示"猜大了"，"猜小了"，"猜对了"
import random  # 一般模块的导入建议放在文件最上方

computer_number = random.randint(1, 101)
try:  # 加入异常捕捉及处理，已经定义将用户的输入转化为整型做比较，如果输入非整数或不输入，系统报异常程序终止
    while True:
        person_number = input("请输入一个1~100内的整数：")
        if int(person_number) == computer_number:
            print("猜对了")
            break
        elif int(person_number) < computer_number:
            print("猜小了")
        elif int(person_number) > computer_number:
            print("猜大了")
        else:
            pass
except(ValueError):
    print("用户未正确输入整数")
