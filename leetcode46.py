class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                return res.append(nums[:])
            for i in range(first,n):
                nums[i],nums[first] = nums[first],nums[i]
                backtrack(first+1)
                nums[i],nums[first] = nums[first],nums[i]
        n = len(nums)
        res = []
        backtrack()
        return res

