#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：14_I.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/4 13:58 
'''
from typing import List
# 动态规划
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(2,i):
                dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j]))
        return dp[n]



