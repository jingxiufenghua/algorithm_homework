#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1095.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/27 18:26 
'''
from typing import List
class MountainArray:
    def __init__(self,nums):
        self.nums = nums
    def get(self, index: int) -> int:
       return  self.nums[index]

    def length(self) -> int:
       return  len(self.nums)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        left,right = 0,length-1
        while left<right:
            mid = left + (right-left)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                left = mid + 1
            else:
                right = mid
        high_index = left
        if mountain_arr.get(high_index)<target or (mountain_arr.get(0)>target and mountain_arr.get(length-1)>target):
            return -1

        low,high = 0,high_index
        while low<high:
            mid = low + (high-low)//2
            if mountain_arr.get(mid) == target:
                return mid
            if mountain_arr.get(mid)<target:
                low = mid + 1
            else:
                high = mid - 1
        if mountain_arr.get(low) == target:
            return low

        low,high = high_index,length-1
        while low<high:
            mid = low + (high-low)//2
            if mountain_arr.get(mid) == target:
                return mid
            if mountain_arr.get(mid)>target:
                low = mid + 1
            else:
                high = mid - 1
        if mountain_arr.get(low) == target:
            return low
        return -1

solution = Solution()
nums = [0,1,2,4,2,1]
mount = MountainArray(nums)
k = 3
result = solution.findInMountainArray(k,mount)
print(result)



def binary_search(mountain, target, l, r, key=lambda x: x):
    target = key(target)
    while l <= r:
        mid = (l + r) // 2
        cur = key(mountain.get(mid))
        if cur == target:
            return mid
        elif cur < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        index = binary_search(mountain_arr, target, 0, peak)
        if index != -1:
            return index
        index = binary_search(mountain_arr, target, peak + 1, mountain_arr.length() - 1, lambda x: -x)
        return index



