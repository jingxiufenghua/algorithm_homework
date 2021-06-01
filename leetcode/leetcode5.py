#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode5.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/28 19:04 
'''
from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        reserv = s[::-1]
        n = len(s)
        dp = [[0]*(n) for _ in range(n)]
        max_len,max_end = 0,0
        for i in range(n):
            for j in range(n):
                if s[i] == reserv[j]:
                    if i==0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    beforeRev = n-1-j
                    if beforeRev + dp[i][j]-1 == i:
                        max_len = dp[i][j]
                        max_end = i
        return s[max_end-max_len+1:max_end+1]

solution = Solution()
s = "babad"
result = solution.longestPalindrome(s)
print(result)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2: return s
        max_len = 1
        begin = 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for j in range(1,n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j-i<3:
                        dp[i][j] = True
                    else:
                        dp[i][j] =  dp[i+1][j-1]

                if dp[i][j] and j-i+1>max_len:
                    max_len = j-i+1
                    begin = i
        return s[begin:begin+max_len]
solution = Solution()
s = "ac"
result = solution.longestPalindrome(s)
print(result)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2: return s
        max_len = 1
        begin = 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for j in range(n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j-i<3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1>max_len:
                    max_len = j-i+1
                    begin= i
        return s[begin:begin+max_len]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2 : return s
        dp = [[0]*(n) for _ in range(n)]
        max_len = 0
        max_end = 0
        revers = s[::-1]
        for i in range(n):
            for j in range(n):
                if s[i] == revers[j]:
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j]>max_len:
                    beforeres = n-1-j
                    if beforeres+dp[i][j]-1 == i:
                        max_len = dp[i][j]
                        max_end = i
        return s[max_end-max_len+1:max_end+1]




