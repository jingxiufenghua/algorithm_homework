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
        self.n = len(nums)
        self.tree = [0]*2*self.n
        for i in range(self.n,2*self.n):
            self.tree[i] = nums[i-self.n]
        for j in range(self.n-1,-1,-1):
            self.tree[j] = self.tree[2*j] + self.tree[2*j+1]

    def update(self, index: int, val: int) -> None:
        pos = self.n + index
        self.tree[pos] = val
        while pos>0:
            left = pos if pos%2 == 0 else pos - 1
            right = pos+1 if pos%2 == 0 else pos
            self.tree[pos//2] = self.tree[left] + self.tree[right]
            pos //= 2

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        left_index = self.n + left
        right_index = self.n + right
        while  right_index>=left_index:
            if left_index%2 == 1:
                sum += self.tree[left_index]
                left_index += 1
            if right_index%2 == 0:
                sum += self.tree[right_index]
                right_index -=1
            left_index //= 2
            right_index //= 2
        return sum

# Your NumArray object will be instantiated and called as such:
nums = [1,3,5]
obj = NumArray(nums)
param_2 = obj.sumRange(0,2)
print(param_2)
obj.update(1,2)
param_2 = obj.sumRange(0,2)
print(param_2)

