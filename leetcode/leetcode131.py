#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode131.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 23:32 
'''
# 131. 分割回文串
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]

        ret = []
        ans = []

        def dfs(i:int):
            if i == n:
                ret.append(ans[:])
                return
            for i in range(i,n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()
        dfs(0)
        return ret


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()
        dfs(0)
        return ret
solution = Solution()
s = "aab"
result = solution.partition(s)
print(result)


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                f[i][j] = (s[i]==s[j]) and f[i+1][j-1]
        ret = []
        ans = []

        def dfs(i:int):
            if i == n:
                ans.append(ret[:])
            for j in range(i,n):
                if f[i][j]:
                    ret.append(s[i:j+1])
                    dfs(j+1)
                    ret.pop()
        dfs(0)
        return ans





