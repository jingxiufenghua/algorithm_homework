from typing import  List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        save = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in save:
                save[nums[i]] = save.get(nums[i])+1
            else:
                save[nums[i]] = 1
        for k,v in save.items():
            if v>n/2:
                return k
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

solution = Solution()
nums = [3,2,3]
result = solution.majorityElement(nums)
print(result)

