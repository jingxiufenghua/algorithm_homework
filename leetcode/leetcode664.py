#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode664.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/24 21:49 
'''
from typing import List
class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = [[1]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                dp[i][j] = dp[i][j-1] if s[i] == s[j] else min([dp[i][k] + dp[k+1][j] for k in range(i,j)])
        return dp[0][len(s)-1]




