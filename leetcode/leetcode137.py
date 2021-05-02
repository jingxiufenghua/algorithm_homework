#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode137.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/30 22:05 
'''
from typing import List
import collections
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums_count = collections.Counter(nums)
#         ans = [k for k,v in nums_count.items() if v == 1]
#         return ans

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num>>i)&1 for num in nums)
            if total % 3:
                if i==31:
                    ans -= (1<<i) # -5 二进制  '0b  111 1111 1111 1111 1111 1111 1111 1011'  1<<31 '0b 1000 0000 0000 0000 0000 0000 0000 0000'
                else:
                    ans |= (1<<i)
        return ans
solution = Solution()
nums = [1,1,1,-5]
result = solution.singleNumber(nums)
print(result)


