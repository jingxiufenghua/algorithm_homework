#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode554.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/2 16:48 
'''
from typing import List
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefixSum = defaultdict(int)
        n = len(wall)
        for i in range(0,n):
            currSum = 0
            for j in range(len(wall[i])-1):
                currSum += wall[i][j]
                prefixSum[currSum] += 1
        return n-max(prefixSum.values(),default=0) # 学会了default = 0
solution = Solution()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
result = solution.leastBricks(wall)
print(result)
