#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode525.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/6/3 9:45 
'''
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0:-1}
        counter = ans = 0
        for i,num in enumerate(nums):
            if num:
                counter += 1
            else:
                counter -= 1
            if counter in hashmap:
                ans = max(ans,i-hashmap[counter])
            else:
                hashmap[counter] = i
        return ans





solution = Solution()
nums = [1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1]
result = solution.findMaxLength(nums)
print(result)



