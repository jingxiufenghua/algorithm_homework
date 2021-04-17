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
        if not nums: return False
        temp = nums[:]
        nums.sort()
        i,j = 0,len(nums)-1
        while i<=j:
            if nums[j]-nums[i]<=t:
                break
            j -= 1
        list_i = [i  for i,x in enumerate(nums) if x == nums[i]]
        list_j = [j  for j,x in enumerate(nums) if x == nums[j]]
        for (i,j) in zip(list_i,list_j):
            print(i,j)
        return False
solution = Solution()
nums = [1,2,3,1]
result = solution.containsNearbyAlmostDuplicate(nums,3,0)
print(result)