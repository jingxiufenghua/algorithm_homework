#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode56.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/14 11:45 
'''
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = sorted(intervals,key=lambda x:(x[0],x[1]))
        n = len(new)
        i = 1
        while i<len(new):
            if new[i][0]<=new[i-1][1]:
                new[i-1] = [new[i-1][0],max(new[i-1][1],new[i][1])]
                new.remove(new[i])
            else:
                i += 1
        return new

solution = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
result = solution.merge(intervals)
print(result)
