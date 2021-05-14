#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode132.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 23:24 
'''
from typing import List


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                g[i][j] = (s[i]==s[j]) and g[i+1][j-1]
        f = [float("inf")]*n
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if g[j+1][i]:
                        f[i] = min(f[i],f[j]+1)
        return f[n-1]

solution = Solution()
s = "aab"
result = solution.minCut(s)
print(result)
