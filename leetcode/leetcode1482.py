#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1482.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/31 10:27 
'''
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k>n: return -1
        def canMake(days):
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers==k:
                        bouquets += 1
                        if bouquets==m:
                            break
                        flowers = 0
                else:
                    flowers = 0
            return bouquets == m

        low,high = min(bloomDay),max(bloomDay)
        while low<high:
            mid = low + (high-low)//2
            if canMake(mid):
                high = mid
            else:
                low = mid + 1
        return low