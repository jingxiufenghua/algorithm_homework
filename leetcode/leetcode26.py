from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        while count<len(nums)-1:
            if nums[count] == nums[count+1]:
                nums.remove(nums[count+1])
            else:
                count += 1
        return len(nums)

nums = [1,2,2,2,3]
solution = Solution()
solution.removeDuplicates(nums)
print(nums)
# 腾讯面试题
#function2
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[count]!=nums[i]:
                count += 1
                nums[count] = nums[i]
        return count+1

# 26. 删除有序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return 1
        nums.sort()
        i = 0
        while i < len(nums)-1:
            while  i<len(nums) and nums[i]==nums[i+1]:
                del nums[i+1]
            i += 1
        return len(nums)
