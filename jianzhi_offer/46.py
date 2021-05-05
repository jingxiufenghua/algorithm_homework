#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：46.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 17:06 
'''
# 剑指 Offer 46. 把数字翻译成字符串
from typing import List
class Solution:
    def translateNum(self, num: int) -> int:
        str_num = str(num)
        n = len(num)
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(1,n):
            dp[i+1] = dp[i]
            if int(str_num[i-1:i+1])<26 and int(str_num[i-1:i+1])>9:
                dp[i+1] = dp[i] + dp[i-1]
        return dp[n]

