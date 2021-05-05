#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：48.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 20:51 
'''
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dict = set()
        res = 0
        left,right = 0,0
        while right<n:
            while left<right and s[right] in dict:
                    dict.remove(s[left])
                    left += 1
            dict.add(s[right])
            res = max(res,len(dict))
            right +=1
        return res

