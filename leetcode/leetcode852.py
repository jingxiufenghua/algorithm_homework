#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode852.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/27 17:21 
'''
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right = 0,len(arr)-1
        while left<right:
            mid = left + (right-left)//2
            if arr[mid]<arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left




