from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        start = 0
        mid = len(nums)//2
        last = len(nums)-1
        if nums[start] == target: return start
        if nums[last] == target: return last
        while mid<last and mid>start:
            while nums[mid]>target:
                if (nums[mid] > nums[last] and nums[start]>target) or (nums[mid]<nums[last]) :
                    start = mid
                else:
                    last = mid
                mid = (start+last)//2

            while nums[mid]<target:
                if (nums[mid]<nums[last] and nums[last]<target) or (nums[mid]>nums[last]):
                    last = mid
                else:
                    start = mid
                mid = (start+last)//2
            if nums[mid] == target:
                return mid
        return -1

solution =  Solution()
# list = [4,5,6,7,0,1,2]
list = [1,3,5]
target = 0
result = solution.search(list,target)
print(result)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if target>=nums[0]:
                if nums[mid]>=nums[0] and target>nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[mid]>=nums[0] or target >nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
