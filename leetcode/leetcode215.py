#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode215.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/11 23:02 
'''
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = []
        heapq.heapify(res)
        for i in range(n):
            if nums[i] in res:
                continue
            heapq.heappush(res,nums[i])
            if len(res) > k:
                heapq.heappop(res)
        for i in range(k-1):
            heapq.heappop(res)
        return heapq.heappop(res)




