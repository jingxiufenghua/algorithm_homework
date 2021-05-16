#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：1.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/15 22:29 
'''
from operator import xor
from typing import List
# class Solution:
#     def sortSentence(self, s: str) -> str:
#         words = s.split(" ")
#         dicts = {}
#         res = [0]*(len(words))
#         for i in range(len(words)):
#             dicts[int(words[i][-1])] = words[i][:-1]
#         for k,v in dicts.items():
#             res[k-1] = v
#         return " ".join(res)
# solution = Solution()
# s ="is2 sentence4 This1 a3"
# result = solution.sortSentence(s)
# print(result)

# class Solution:
#     def memLeak(self, memory1: int, memory2: int) -> List[int]:
#         cache = [memory1,memory2]
#         i = 1
#         while cache[0]>=i or cache[1]>=i:
#             if cache[0]>=cache[1]:
#                 cache[0] -= i
#             else:
#                 cache[1] -= i
#             i += 1
#         return [i,cache[0],cache[1]]
# solution = Solution()
# result = solution.memLeak(8,11)
# print(result)
#
# from collections import deque
#
# class Solution:
#     def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
#         row,col = len(box),len(box[0])
#         res = []
#         for i in range(row):
#             tmp = []
#             deque(tmp)
#             index = 0
#             for j in range(col):
#                 if box[i][j] == "#":
#                     tmp.append("#")
#                 elif box[i][j] == ".":
#                     tmp.insert(index,".")
#                 elif box[i][j] == "*":
#                     tmp.append("*")
#                     index = j+1
#             res.append(tmp)
#         ans = [[""]*row for _ in range(col)]
#         for i in range(row-1,-1,-1):
#             for j in range(col):
#                 ans[j][row-i-1] = res[i][j]
#         return ans
# solution = Solution()
# box = [["#","#","*",".","*","."], ["#","#","#","*",".","."], ["#","#","#",".","#","."]]
# result = solution.rotateTheBox(box)
# print(result)

# class Solution:
#     def sumOfFlooredPairs(self, nums: List[int]) -> int:
#         def floor(m,n):
#             return  m//n
#         nums.sort()
#         dp = []
#         n = len(nums)
#         tmp = 0
#         score = 0
#         for i in range(n-1,0,-1):
#             if nums[i] != nums[i-1]:
#                 score = nums[i]//nums[i-1]
#             tmp += score
#         return tmp



# import bisect
# class Solution:
#     def sumOfFlooredPairs(self, nums: List[int]) -> int:
#         nums.sort()
#         mem = {}
#         ans = 0
#         for n in nums:
#             if n in mem:
#                 ans += mem[n]
#             else:
#                 cur = 0
#                 pre = 0
#                 for k in range(0, nums[-1] // n + 2):
#                     loc = bisect.bisect_left(nums, (k + 1) * n)
#                     # if loc != len(nums) and nums[loc] == (k + 1) * n:
#                         # loc += 1
#                     cur += (loc - pre) * k
#                     pre = loc
#                 mem[n] = cur
#                 ans += cur
#         return ans % int(1e9 + 7)
# solution = Solution()
# nums = [7,7,7,7,7,7,7]
# result = solution.sumOfFlooredPairs(nums)
# print(result)

from functools import reduce

# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n<1: return 0
#         if n==1 :return nums[0]
#         res = []
#         ans = 0
#         def dfs(nums,index,temp):
#             temp = temp[:]
#             if index==n:
#                 return
#             for i in range(index,n):
#                 temp.append(nums[i])
#                 res.append(temp[:])
#                 dfs(nums,i+1,temp)
#                 temp.pop()
#         dfs(nums,0,[])
#         for i in res:
#             ans += reduce(xor,i)
#         return ans
#
# solution = Solution()
# nums = [5,1,6]
# # nums = [3,4,5,6,7,8]
# result = solution.subsetXORSum(nums)
# print(result)


# from collections import Counter
class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        n0, n1 = s.count('0'), s.count('1')
        res = float("INF")
        # "1010..."
        if n1 == (n + 1) // 2 and n0 == n // 2:   # 不同字符个数相等
            diff1 = 0
            for i in range(n):
                if int(s[i]) == i % 2:   # 对应位数不同
                    diff1 += 1
            res = min(res, diff1 // 2)
        # "0101..."
        if n0 == (n + 1) // 2 and n1 == n // 2:   # 不同字符个数相等
            diff2 = 0
            for i in range(n):
                if int(s[i]) != i % 2:   # 对应位数不同
                    diff2 += 1
            res = min(res, diff2 // 2)
        if res == float("INF"):
            return -1   # 不存在
        else:
            return res

solution = Solution()
s = "1110001"
result = solution.minSwaps(s)
print(result)


#
# from collections import Counter
# class FindSumPairs:
#
#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1 = nums1
#         self.nums2 = nums2
#         self.cnt = Counter(self.nums2)
#
#     def add(self, index: int, val: int) -> None:
#         vo = self.nums2[index]
#         self.nums2[index] += val
#         nv = self.nums2[index]
#         self.cnt[vo] -= 1
#         if nv not in self.cnt:
#             self.cnt[nv] = 1
#         else:
#             self.cnt[nv] += 1
#
#     def count(self, tot: int) -> int:
#         count = 0
#         for i in self.nums1:
#             if tot-i in self.cnt:
#                 count += self.cnt[tot-i]
#         return count
#
# # Your FindSumPairs object will be instantiated and called as such:
# nums1 = [1, 1, 2, 2, 2, 3]
# nums2 = [1, 4, 5, 2, 5, 4]
# obj = FindSumPairs(nums1, nums2)
# param_2 = obj.count(7)
# print(param_2)