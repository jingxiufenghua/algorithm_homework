#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1310. 子数组异或查询.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/12 16:48 
'''
from operator import xor
from typing import List
from functools import reduce
class Solution:
    # 超出时间限制
    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    #     list = sorted([(k,v) for k,v in enumerate(queries)],key=lambda x:(x[1][0],x[1][1]))
    #     res = [0]*len(list)
    #     for k,v in list:
    #         res[k] = reduce(xor,[arr[i] for i in range(v[0],v[1]+1)])
    #     return res

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        list = sorted([(k,v) for k,v in enumerate(queries)],key=lambda x:(x[1][0],x[1][1]))
        res = [0]*len(list)
        for ord,(k,v) in enumerate(list):
            if ord == 0:
                a = reduce(xor, [arr[i] for i in range(v[0], v[1] + 1)])
                start,end = v[0],v[1]
            while v[0]>start:
                a ^= arr[start]
                start += 1
            while v[1]<end:
                a ^= arr[end]
                end -= 1
            while v[1]>end:
                end += 1
                a ^= arr[end]
            res[k] = a
        return res


solution = Solution()
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
result =solution.xorQueries(arr,queries)
print(result)
