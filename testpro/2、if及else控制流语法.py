# -*- coding:utf-8 -*-
a = 9
if a == 0:
    print("a == 0")
elif a == 1:
    print("a == 1")
elif a == 2:  # 多重分支
    print("a ==2")
else:
    print("a不等于1，2，3")

"""
分段函数求值：
3x - 5       (X>1)
f(x) = x + 2 (-1<=x<=1)
5x + 3       (x<-1)
"""
# 多重分支
x = -2
if x > 1:
    y = 3 * x - 5
elif -1 <= x <= 1:
    y = x + 2
elif x < -1:
    y = 5 * x + 3
print(y)

"""
#分支结构
x = 0
if x>1:
    y = 3*x-5
else:
    if x<-1:
        y =5*x+3
    else:
        y =x+2
print(y)
"""
