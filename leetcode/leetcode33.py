#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode33.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/27 9:42 
'''

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums : return -1
        left,right = 0,len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if target == nums[mid]:
                return mid
            if nums[0]<=nums[mid]:
                if nums[0]<=target<nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



# 789123456
# 456789123
solutions = Solution()
nums = [4,5,6,7,0,1,2]
result = solutions.search(nums,0)
print(result)



