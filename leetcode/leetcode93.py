#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode93.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/15 22:19 
'''
from typing import List
# 93. 复原 IP 地址
from collections import Counter
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        dp = [[000]*n]
        res = []
        for i in range(1,4):
            dp[i] = dp[i-1]

