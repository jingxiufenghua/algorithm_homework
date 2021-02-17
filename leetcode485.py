class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len,count = 0,0
        for i in nums:
            if i == 1:
                count+=1
            else:
                count = 0
            max_len = max(max_len,count)
        return max_len
