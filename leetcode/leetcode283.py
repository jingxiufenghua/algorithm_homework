class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums :return -1
        n = len(nums)
        zero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i],nums[zero] = nums[zero],nums[i]
                zero += 1
        return nums
