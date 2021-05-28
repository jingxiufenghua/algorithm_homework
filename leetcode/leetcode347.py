#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode347.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/26 20:42 
'''
from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        res = []
        ans = []
        heapq.heapify(res)
        for key,v in dict.items():
            heapq.heappush(res,[-v,key])
        for i in range(k):
            ans.append(heapq.heappop(res)[1])
        return ans
solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
result = solution.topKFrequent(nums,k)
print(result)





