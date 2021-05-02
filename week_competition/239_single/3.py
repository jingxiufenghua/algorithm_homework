#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：3.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/2 10:10 
'''
# 这道题是 leetcode31 题的加强版
import bisect
from typing import List
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def upg(num):
            for i in range(len(num) - 1):
                if num[-2 - i] >= num[-1 - i]:
                    continue
                cand = num[-1 - i:][::-1]
                pt = bisect.bisect(cand, num[-2 - i] + 0.01)
                num = num[:-2 - i] + [cand[pt]] + cand[:pt] + [num[-2 - i]] + cand[pt + 1:]
                break
            return num

        num = rnum = [int(t) for t in num]    # num  和 rnum 是两个 List，修改其中一个不影响另一个
        for _ in range(k):
            num = upg(num)

        to_ret = 0
        for pst in num:
            for pr in range(len(rnum)):
                if rnum[pr] == pst:
                    to_ret += pr
                    rnum.pop(pr)  # pop() 可以指定彈出位置
                    break
        return to_ret
        # return ''.join([str(t) for t in num])
solution = Solution()
nums = "5489355142"
result = solution.getMinSwaps(nums,4)
print(result)