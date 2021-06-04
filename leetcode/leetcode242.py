#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode242.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/6/1 22:49 
'''
from typing import List
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        for k,v in s_dict.items():
            if k not in t_dict :
                return False
            if v != t_dict[k]:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        return s_dict == t_dict
