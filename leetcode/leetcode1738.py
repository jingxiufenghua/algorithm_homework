#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode1738.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/5/19 11:36 
'''
from typing import List
# 1738. 找出第 K 大的异或坐标值
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        row,col = len(matrix),len(matrix[0])
        pre = [[0]*(col+1) for _ in range(row+1)]
        result = []
        for i in range(1,row+1):
            for j in range(1,col+1):
                pre[i][j] = pre[i-1][j]^pre[i][j-1]^pre[i-1][j-1]^matrix[i-1][j-1]
                result.append(pre[i][j])
        result.sort(reverse=True)
        return result[k-1]