#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode67.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 21:07 
'''
from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na,nb = len(a),len(b)
        if na>nb:
            b = "0"*(na-nb) + b
        else:
            a = '0'*(nb-na) + a
        res = ""
        flag = 0
        for i in range(max(na,nb)-1,-1,-1):
            add =  int(a[i]) + int(b[i]) + flag
            res += str(add%2)
            flag = add//2
        if flag == 1: res += '1'
        return res[::-1]

class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))  # 将二进制字符串转换为十进制整形 int(xxx,2)


class Solution:
    def addBinary(self, a, b) -> str:
        x,y = int(a,2) , int(b,2)
        while y:
            answer = x^y
            carry  = (x&y)<<1
            x,y  = answer,carry
        return bin(x)[2:]

solution = Solution()
a = "11"
b = "1111111"
result = solution.addBinary(a,b)
print(result)


