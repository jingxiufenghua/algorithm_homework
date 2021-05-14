#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode378.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/13 11:40 
'''
from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        print(pq)
        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
            print(pq)
        return heapq.heappop(pq)[0]

solution = Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
result = solution.kthSmallest(matrix,k)
print(result)



