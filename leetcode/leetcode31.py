from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums,reverse = True)==nums:
            nums[:] = nums[::-1]
            return
        for i in range(len(nums)-1)[::-1]:
            if nums[i]<nums[i+1]:
                break
        for j in range(i+1,len(nums)):
            if j==len(nums)-1 or nums[j+1]<=nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                break
        nums[i+1:] = nums[i+1:][::-1]
        return

list = [3,2,1]
solution = Solution()
result = solution.nextPermutation(list)
print(list)
