#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：algorithm_homework 
@File    ：leetcode220.py
@IDE     ：PyCharm 
@Author  ：无名
@Date    ：2021/4/17 10:29 
'''
# 220. 存在重复元素 III
from typing import List
import bisect
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedSet
        st  = SortedSet()
        left,right = 0,0
        res = 0
        while right<len(nums):
            if right-left>k:
                st.remove(nums[left])
                left += 1
            index = bisect.bisect_left(st,nums[right]-t)
            if st and index>=0 and  index<=len(st) and abs(st[index]-nums[right])<=t:
                return True
            st.add(nums[right])
            right += 1
        return False


solution = Solution()
nums = [7,1,3]
result = solution.containsNearbyAlmostDuplicate(nums,2,3)
print(result)