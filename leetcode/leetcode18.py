from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets
        nums.sort()
        length = len(nums)
        for i in range(length-3):
            # 取第一个数
            if  i>0 and nums[i] == nums[i-1]:continue
            if  nums[i]+nums[length-1]+nums[length-2]+nums[length-3]<target: continue
            if  nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:break
            for j in range(i+1,length -2):
                # 锁定第二个数
                if j>i+1 and nums[j]==nums[j-1]: continue
                if j<length-3 and nums[i] + nums[j] + nums[j+1] + nums[j+2]>target:break
                if nums[i]+nums[j] + nums[length-1] + nums[length-2] < target: continue
                left,right = j+1,length-1
                while left<right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left] == nums[left+1]:
                            left +=1
                        while left<right and nums[right] == nums[right-1] :
                            right -=1
                        right -=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return quadruplets

solution = Solution()
nums = [1,2,3,4,9,0]
target = 6
result = solution.fourSum(nums,target)
print(result)