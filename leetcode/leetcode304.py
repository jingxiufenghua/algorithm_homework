#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode304.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/22 11:11 
'''
# 304. 二维区域和检索 - 矩阵不可变
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0] :
            M,N = 0,0
        else:
            M,N = len(matrix),len(matrix[0])
        self.presum = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                self.presum[i+1][j+1] = self.presum[i][j+1]+self.presum[i+1][j] - self.presum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1]-self.presum[row2+1][col1]-self.presum[row1][col2+1] + self.presum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
