#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode91.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/21 22:20 
'''
from typing import List
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0]*n
        for i in range(1,n+1):
            if s[i-1] !='0':
                dp[i] += dp[i-1]
            if i>1 and s[i-2]!='0' and int(s[i-2:i])<=26:
                dp[i] += dp[i-2]
        return dp[n]

solution = Solution()
s = "125"
result = solution.numDecodings(s)
print(result)
