#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode263.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 17:20 
'''
from typing import List
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1 : return True
        while n>=2:
            tmp = n
            for i in [2,3,5]:
                if n % i == 0:
                    n = n // i
                    if n == 1: return True
                    break
            if tmp == n:
                break
        return False

    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        factor = [2,3,5]
        for factor in factors:
            while n%factor == 0:
                n //= factor
        return n == 1

solution = Solution()
result = solution.isUgly(25)
print(result)