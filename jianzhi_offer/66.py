#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：66.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/29 16:28 
'''
# 剑指 Offer 66. 构建乘积数组
from typing import List
class Solution:
    # 超出时间限制，卡在最后一个测试用例上了
    def constructArr(self, a: List[int]) -> List[int]:
        if not a : return []
        n = len(a)
        dp = [0]*(n)
        dp[0] = a[0]
        b = []
        for i in range(1,n):
            dp[i] = dp[i-1] * a[i]
        for i in range(n):
            product = dp[i-1] if i-1>=0 else a[0]
            for j in range(i+1,n):
                product *= a[j]
            b.append(product)
        return b

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1] # 下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1] # 上三角
            b[i] *= tmp # 下三角 * 上三角
        return b

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b,tmp = [1]*len(a),1
        for i in range(1,len(a)):
            b[i] = b[i-1] * a[i-1]
        for i in range(len(a)-2,-1,-1):
            tmp *= a[i+1]
            b[i] *= tmp
        return b

solution = Solution()
nums = [7, 2, 2, 4, 2, 1, 8, 8, 9, 6, 8, 9, 6, 3, 2, 1]
result = solution.constructArr(nums)
print(result)
