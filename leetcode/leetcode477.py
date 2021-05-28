#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode477.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/28 10:08 
'''
from typing import List
import collections
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        nums_1 = collections.defaultdict(int)
        nums_0 = {}
        for j in range(32):
            for index in range(len(nums)):
                last_bit = nums[index]&1
                if last_bit == 1:
                    nums_1[j] += 1
                else:
                    nums_0[j] += 1
                nums[index] >>=1
        count = 0
        for i in range(32):
            count += nums_1[i]*nums_0[i]
        return count



class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans



