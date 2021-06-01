#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode6.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/31 22:08 
'''
from typing import List
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2: return s
        res = ["" for _ in range(numRows)]
        i,flag = 0,-1
        for c in s:
            res[i] += c
            if i==0 or i==numRows-1 : flag = -flag
            i += flag
        return "".join(res)


def partition(nums,low,high):
    pivot = nums[low]
    while low<high:
        while nums[high]>=pivot:
            high -= 1
        nums[low] = nums[high]
        while nums[low]<pivot:
            low += 1
        nums[high] = nums[low]
        nums[low] = pivot
    return low
