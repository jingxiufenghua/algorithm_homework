#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：61.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 15:08 
'''
from typing import List
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma,mi = 0,14
        for num in nums:
            if num == 0: continue
            ma = max(ma,num)
            mi = min(mi,num)
            if num in repeat: return False
            repeat.add(num)
        return ma-mi<5

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i+1]: return False
        return nums[4] - nums[joker]<5
solution = Solution()
nums = [0,0,2,2,5]
result = solution.isStraight(nums)
print(result)

