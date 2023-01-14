#!/usr/bin/python3
# -*- coding:utf-8 -*-


def sum_beishu(n: int):
    # a = []
    if n <= 0:
        # a = [0]
        result = 0
    else:
        result = 0
        for i in range(1, n):
            if i < n and i % 3 == 0 or i % 5 == 0:
                result = result + i
    # for j in a:
    #     result = result + j
    return result


print(sum_beishu(6))