# 剑指 Offer 53 - I. 在排序数组中查找数字 I
from  typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<= target:
                left = mid + 1
            else:
                right = mid - 1
        right_index = left
        if right>=0 and nums[right] != target: return 0
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left_index = right
        return right_index - left_index - 1















