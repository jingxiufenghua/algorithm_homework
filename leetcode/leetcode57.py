# 剑指 Offer 57. 和为s的两个数字
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for i in range(len(nums)):
            if nums[i] not in hash_set:
                hash_set[target-nums[i]] = nums[i]
            else:
                return [target-nums[i],nums[i]]
        return []

