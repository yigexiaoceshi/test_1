# -*- coding:utf-8 -*-
"""
for循环，知道循环次数
1、计算1-100的和
2、加入分支结构实现1-100之间的偶数求和
3、使用Python实现1-100之间的偶数求和
"""
result = 0
for i in range(101):
    print(i)
    result = i + result  # 如果result赋值为1，那第一循环就加了1，第二循环成了1+1，多加了个1了
print(result)

result1 = 0
for j in range(101):
    if j % 2 == 0:  # 除以2余数为0的是偶数
        result1 = result1 + j
print(result1)

result2 = 0
for k in range(2, 101, 2):  # 下标2（对应数字2）开始到101（对应数字100），步长为2，k取值都为偶数
    result2 = result2 + k
print(result2)

# while循环
# while True:
#     print("死循环") #True条件一直成立，一直循环打印

a = 1
while a == 1:
    a = a + 1  # 如果while条件后面只有一行语句，可以直接写到冒号后面，写在一行
else:
    print("a!=1")
    print(a)

for g in range(1, 10):
    if g == 5:
        break  # if条件不成立时，跳出整个循环体，不再执行当前循环体任何语句
    print(g)

for h in range(1, 10):
    if h == 5:
        continue  # if条件不成立时，今天跳出当前循环，继续执行循环体的下一轮循环
    print(h)

"""
猜数字游戏：
计算机给出一个随机数字，由人输入一个数字去猜，计算机根据人猜的数字给出提示"大一点"，"小一点"，"猜对了"，猜对时跳出
"""
import random

computer_number = random.randint(1, 101)
print(computer_number)
while True:
    person_number = int(input("请输入您猜的数字："))
    if person_number < computer_number:
        print("小一点！")
    elif person_number > computer_number:
        print("大一点")
    else:
        print("猜对了！")
        break
