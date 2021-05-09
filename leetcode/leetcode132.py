#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode132.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/7 23:24 
'''
from typing import List
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[0] =