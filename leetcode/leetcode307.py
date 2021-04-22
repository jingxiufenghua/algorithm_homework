#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode307.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/22 11:39 
'''
# 307. 区域和检索 - 数组可修改
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            self.M = 0
        else:
            self.M = len(nums)
        self.presum = [0]*(self.M+1)
        for i in range(self.M):
            self.presum[i+1] = self.presum[i]+nums[i]

    def update(self, index: int, val: int) -> None:
        self.presum[index+1] =self.presum[index] + val
        for i in range(index+2,self.M):
            self.presum[i] = self.presum[i-1] +


    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right] - self.presum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
