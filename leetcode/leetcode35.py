# 35. 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        n = len(nums)
        left,right = 0,n-1
        while left<= right:
            mid = (left+right)>>1
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1
        return left

solution = Solution()
nums = [1,3]
result = solution.searchInsert(nums,2)
print(result)

