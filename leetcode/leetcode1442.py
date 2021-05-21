#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1442.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/18 22:00 
'''
from typing import List
from collections import Counter
# 1442. 形成两个异或相等数组的三元组数目
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1]^val)
        cnt,total = Counter(),Counter()
        ans = 0
        for k in range(n):
            if s[k+1] in cnt:
                ans += cnt[s[k+1]]*k - total[s[k+1]]
            cnt[s[k]] += 1
            total[s[k]] += k
        return ans
solution = Solution()
arr = [2,3,1,6,7]
result = solution.countTriplets(arr)
print(result)


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        ans = 0
        for i in range(n):
            for k in range(i + 1, n):
                if s[i] == s[k + 1]:
                    ans += k - i

        return ans

