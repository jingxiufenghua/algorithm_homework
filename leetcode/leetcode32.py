#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode32.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/16 23:32 
'''
from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n==0:return 0
        dp = [0]*n
        for i in range(n):
            if s[i] == ")" and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2]+2
        return max(dp)
solution = Solution()
s = "()"
result = solution.longestValidParentheses(s)
print(result)


