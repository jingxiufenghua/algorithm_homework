# 剑指 Offer 39. 数组中出现次数超过一半的数字
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        n = len(nums)
        if n==1:return nums[0]
        for i in nums:
            if i in count_dict:
                count_dict[i] +=1
                if count_dict[i]>(n//2):
                    return i
            else:
                count_dict[i] = 1

