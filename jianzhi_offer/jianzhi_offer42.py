class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums : return 0
        if max(nums)<0:return max(nums)
        sub_pro = 0
        max_pro = 0
        for i in nums:
            sub_pro = max(sub_pro+i,0)
            max_pro = max(max_pro,sub_pro)
        return max_pro



