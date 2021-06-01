from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[nums[i]] = i
        return []
solution = Solution()
nums = [3,2,4]
target = 6
result = solution.twoSum(nums,target)
print(result)











class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[target-nums[i]] = i
            else:
                return [dict[nums[i]],i]
