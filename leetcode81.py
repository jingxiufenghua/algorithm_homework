from typing import  List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left,right = 0,n-1
        if n == 1 : return nums[0] == target
        while left<=right:
            mid = (left + right) //2
            if nums[mid] == target:
                return  True
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif target>=nums[left]:
                if nums[mid]>=nums[left] and target>nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid]>=nums[left] or target>nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
solution = Solution()
nums = [1,0,1,1,1]
result = solution.search(nums,0)
print(result)
