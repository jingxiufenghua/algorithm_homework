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

