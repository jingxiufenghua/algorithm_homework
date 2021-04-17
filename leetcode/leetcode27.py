from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j= 0
        while j<len(nums):
            if nums[j] == val:
                nums.remove(nums[j])
                j-=1
            j+=1
        return len(nums)

solution = Solution()
nums =[0,1,2,2,3,0,4,2]
ListNode1 = solution.removeElement(nums,2)
print(nums)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i ,last = 0 ,len(nums)-1
        while i<=last:
            if nums[i]==val:
                nums[i],nums[last] = nums[last],nums[i]
                last -=1
            else:
                i +=1
        return last+1





