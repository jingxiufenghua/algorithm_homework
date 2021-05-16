#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode191.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/15 11:29 
'''
from typing import List
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            if n&1==1:
                count += 1
            n >>=1
        return count
solution = Solution()
n = 9
result = solution.hammingWeight(n)
print(result)
