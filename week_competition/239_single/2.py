#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：2.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/2 10:10 
'''
from typing import List
class Solution:
    def splitString(self, s: str) -> bool:
        n =len(s)
        def dfs(idx,last):
            if idx == n:
                return True
            if last == 0:
                return False
            for i in range(idx,n):
                y = int(s[idx:i+1])
                if y>=last:
                    break
                if (last-1) == y:
                    if dfs(i+1,y)==True:
                        return True
            return False

        for i in range(0,n-1):
            cur = int(s[0:i+1])
            if cur>9999999999:
                break
            if dfs(i+1,cur)==True:
                return True
        return False









solution = Solution()
s =  "200100"
result = solution.splitString(s)
print(result)
