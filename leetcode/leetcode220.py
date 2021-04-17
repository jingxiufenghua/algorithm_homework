#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode220.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/17 10:29 
'''
# 220. 存在重复元素 III
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:


solution = Solution()
nums = [1,2,3,1]
result = solution.containsNearbyAlmostDuplicate(nums,3,0)
print(result)