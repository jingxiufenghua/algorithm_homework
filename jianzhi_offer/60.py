#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：60.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/28 10:32 
'''
from typing import List
# 剑指 Offer 60. n个骰子的点数
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0]*6*n]*n
        ans = [0]*(5*n+1)
        for i in range(6):
            dp[0][i] = 1
        for i in range(1,n):
            for j in range(i,6*n):
                for k in range(1,6+1):
                    if  j-k>=0:
                        dp[i][j] += dp[i-1][j-k]
        import math
        all = math.pow(6.0,n)
        for i in range(5*n+1):
            ans[i] = dp[n-1][i+n-1]/all
        return ans