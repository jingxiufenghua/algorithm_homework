#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：336.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/26 17:02 
'''
from typing import List
class Solution:
  def squre_test(self,nums=8):
    if not nums: return -1
    for i in range(1,nums):
      if i**2 == nums: return i
      elif i**2>nums:
        break   # 找到大于 i**2 》 nums
    if i>=1 and (i-1)**2<nums:
      for j in range(1,10):
        if ((i-1)+j/10)**2 - nums>0:  # 0.1  小于精度
          return i-1+(j-1)/10

solution = Solution()
nums = 8
result = solution.squre_test()
print(result)