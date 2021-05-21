#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1143.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/21 10:44 
'''
from typing import List
# 1143. 最长公共子序列
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[M][N]

solution = Solution()
text1 = "aced"
text2 = "bcd"
result = solution.longestCommonSubsequence(text1,text2)
print(result)

