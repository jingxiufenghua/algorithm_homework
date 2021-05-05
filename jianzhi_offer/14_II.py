#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：14_II.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/4 15:54
'''
# 剑指 Offer 14- II. 剪绳子 II
from typing import List
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(2,i):
                dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j]))
        # return int(dp[n]%(1e9+7))
        return int(dp[n]%1000000007)  # 1e9+7 不对，我也不知道为什么

class Solution(object):
    def cuttingRope(self, n):
        # 如果 n = 2, 则结果为 1 * 1 = 1
        # 如果 n = 3, 则结果为 1 * 2 = 2
        # 这里和dp[2], dp[3]不一样，因为题目要求至少要切一刀
        if n <= 3:
            return 1 if n == 2 else 2

        # dp[i] 表示 长度为 i 的绳子的最大乘积（包含切 0 刀的情况）
        dp = [0 for _ in range(n+1)]

        dp[0] = 0   # 绳长为0，怎么切都是0
        dp[1] = 1   # 绳长为1，一刀也不切乘积最大
        dp[2] = 2   # 绳长为2，一刀也不切乘积最大
        dp[3] = 3   # 绳长为3，一刀也不切乘积最大

        # 当 n >= 4 时，切一刀的乘积 不再小于 一刀也不切的，开始动态规划

        '''
        dp[i] = max(dp[j]*dp[i-j], dp[i]) 的意思是，选择是否要在j的位置切一刀。
            切完后，总乘积就变成了：j左边的最大乘积 * 右边的最大乘积 （dp[j-0]*dp[i-j]）
            不切的话，总乘积保持不变

        想要dp[n]，需要 {dp[i], i < n}, 所以正向计算dp
        对于每一个i，尝试所有的可以切的位置（0 ~ i-1），取他们中最大的那个
        '''

        for i in range(4,n+1):
            for j in range(0,i-1):
                dp[i] = max(dp[j]*dp[i-j], dp[i])

        # dp[n] 即为长度为n的绳子的最大乘积，根据题意取模
        return dp[n]%1000000007


