#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1486.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 11:07 
'''
from typing import List
class Solution:
    # def xorOperation(self, n: int, start: int) -> int:
    #     dp = [0]*n
    #     dp[0] = start
    #     for i in range(1,n):
    #         dp[i] = dp[i-1]^(dp[0]+2*i)
    #     return dp[-1]

    def xorOperation(self, n: int, start: int) -> int:
        a = start
        for i in range(1,n):
            a,b = a^(start + 2*i),a
        return a

solution = Solution()
result = solution.xorOperation(n=4,start=3)
print(result)

