#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：3.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/9 10:24 
'''
from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        n = len(logs)
        list = sorted(logs,key=lambda x:x[0])
        recoder = []
        for i in range(n-1,-1,-1):
            count = 1
            for j in range(i-1,-1,-1):
                if list[j][1]-1>=list[i][0]:
                    count += 1
            recoder.append([list[i][0],count])
        res = sorted(recoder,key=lambda x:(-x[1],x[0]))
        return res[0][0]
solution = Solution()
logs = [[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]
result = solution.maximumPopulation(logs)
print(result)




