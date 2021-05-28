#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：week_competion_238.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/25 10:27 
'''
from typing import List
# class Solution: 5738
# #     def sumBase(self, n: int, k: int) -> int:
# #         res = []
# #         while n>=k:
# #             temp = n%k
# #             n = n//k
# #             res.append(temp)
# #         res.append(n)
# #         print(res)
# #
# #         return sum(res)
# # solution = Solution()
# # result = solution.sumBase(10,10)
# # print(result)

# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         nums.sort()
#         diff = []
#         for i in range(n-1):
#             diff.append(nums[i+1] - nums[i])
#         diff.sort(reverse=True)
#         count = 1
#         while k>0:
#             k = k-diff.pop()
#             count += 1


# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)
#         l = 0
#         total = 0
#         res = 1
#         for r in range(1, n):
#             total += (nums[r] - nums[r - 1]) * (r - l)
#             while total > k:
#                 total -= nums[r] - nums[l]
#                 l += 1
#             res = max(res, r - l + 1)
#         return res

# import  collections
# class Solution:
#     def longestBeautifulSubstring(self, word: str) -> int:
#         hash_map = collections.Counter(word)
#         if len(hash_map)<5: return 0
#         n = len(word)
#         i,j = 0,0
#         ans = 0
#         while i<n:
#             temp = 0
#             next = 0
#             while j<n-1:
#                 if word[j]>word[j+1]:
#                     break
#                 temp += 1
#                 j +=  1
#             if len(collections.Counter(word[i:j+1]))==5:
#                 if ans >= j-i+1:
#                     i = j-1
#                 ans = max(ans, j - i + 1)
#             i += 1
#             while i<n and word[i]!='a':
#                 next += 1
#                 i += 1
#             if next>=temp:
#                 j = i
#             else:
#                 j = i + temp - next -1
#         return ans

# def GP(it): return [[ch,len(list(g))] for ch,g in groupby(it)]
# class Solution:
#     def longestBeautifulSubstring(self, word: str) -> int:
#         d={"a":1,"e":2,"i":3,'o':4,"u":5}
#         word=list(word)
#         word=map(lambda x:d[x],word)
#         g=GP(word)
#         n=len(g)
#         dp=[0]*n
#         ans=0
#         #print(g)
#         for i,(ch,l) in enumerate(g):
#             if ch==1:
#                 dp[i]=l
#             else:
#                 if i and dp[i-1] and ch==g[i-1][0]+1:
#                     #print(i)
#                     dp[i]=dp[i-1]+l
#                     if ch==5:
#                         ans=max(ans,dp[i])
#         #print(dp)
#         return ans

import itertools
class Solution(object):
    def longestBeautifulSubstring(self, word):
        res = 0
        A = [[c, len(list(s))] for c, s in itertools.groupby(word)]
        print(A)
        for i in range(len(A) - 4):
            if ''.join(A[j][0] for j in range(i, i + 5)) == 'aeiou':
                res = max(res, sum(A[j][1] for j in range(i, i + 5)))
        return res

solution = Solution()
word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
result = solution.longestBeautifulSubstring(word)
print(result)


from itertools import groupby

# 对字符串进行分组
for k, g in groupby('11111234567111'):
  print(k, list(g))
d = {1: 1, 2: 2, 3: 2}
# 按照字典value来进行分组
for k, g in groupby(d, lambda x: d.get(x)):
  print(k, list(g))




