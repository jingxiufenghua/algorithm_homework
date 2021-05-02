#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：third.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/1 22:15 
'''
from typing import List
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] != 1: arr[0] = 1
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]>1:
                arr[i] = arr[i-1] +1
        return arr[-1]