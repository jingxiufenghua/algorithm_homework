#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode692.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/20 20:53 
'''
from typing import List
# 692. 前K个高频单词
import collections
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = collections.Counter(words)
        record = {}
        for key,v in dict.items():
            if v not in record:
                record[v] = [key]
            else:
                record[v].append(key)
        ans = sorted(record,reverse=True)
        res = []
        for i in ans:
            n = len(record[i])
            if  k - len(record[i])<0:
                res += sorted(record[i])[:k]
                break
            res += sorted(record[i])
            k = k - len(record[i])
        return res
solutions = Solution()
words = ["aaa","aa","a"]
k = 3
result =  solutions.topKFrequent(words,k)
print(result)






