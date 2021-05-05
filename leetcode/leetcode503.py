#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode503.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 13:26 
'''
# 503. 下一个更大元素 II
from typing import List
class Solution:
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     if not nums: return []
    #     new_nums = nums[:] + nums[:]
    #     n = len(nums)
    #     res = []
    #     for i in range(n):
    #         for j in range(i+1,2*n-1):
    #             if nums[i]<new_nums[j]:
    #                 res.append(new_nums[j])
    #                 break
    #         if len(res)<=i:
    #             res.append(-1)
    #     return res

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)
        new_nums = nums[:] + nums[:]
        stack = [(0,new_nums[0])]
        res = [-1]*2*n
        for i in range(1,2*n):
            while stack and stack[-1][1]<new_nums[i]:
                origin_index,_ = stack.pop()
                res[origin_index] = new_nums[i]
            stack.append((i,new_nums[i]))
        return res[:n]

solution = Solution()
nums = [1,2,1]
result = solution.nextGreaterElements(nums)
print(result)