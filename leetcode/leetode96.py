#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetode96.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/11 16:22 
'''
from typing import List
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0],dp[1] = 1,1
        for i in range(2,n+1):
            for j in range(i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
