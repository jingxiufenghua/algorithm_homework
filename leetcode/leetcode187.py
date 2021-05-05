#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode187.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/3 22:23 
'''
# 187. 重复的DNA序列
from typing import List
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         if not s : return []
#         s_list = list(s)
#         hash_map = {"A":1,"C":2,"G":3,"T":4}
#         n = len(s)
#         for i in range(n):
#             s_list[i] = hash_map[s_list[i]]
#         ans = []
#         for j in range(n-10):
#             res = 0
#             k = j
#             while k<n:
#                 if k-j == 10 and res == 0:
#                     ans.append(s_list[j:k])
#                     break
#                 res ^= s_list[k]
#                 k += 1
#         return ans

class Solution:
    def findRepeatedDnaSequences(self,s: str) -> List[str]:
        seen, patterns = set(), set()
        n = len(s)
        for i in range(0,len(s)-10+1):
            p = s[i:i+10]
            if p in seen: patterns.add(p)
            else: seen.add(p)
        return list(patterns)

solution = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result = solution.findRepeatedDnaSequences(s)
print(result)
