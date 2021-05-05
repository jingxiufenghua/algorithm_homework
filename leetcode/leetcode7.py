#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode7.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 0:02 
'''
from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        res = ""
        sign = 1
        if string[0] == "-":
            sign = -1
            res = string[1:][::-1]

        else:
            res = string[::-1]
        nums = int("".join(res))
        return sign*nums if nums>-2**31 and nums <2**31-1 else 0

solution = Solution()
result = solution.reverse(-2147483648)
print(result)