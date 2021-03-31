class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n==2 or n==0 :return -1
        left,right = 0,0
        total_sum =sum(nums)
        for i in range(n):
            right = total_sum-left-nums[i]
            if left == right:
                return i
            left = left + nums[i]
        return -1