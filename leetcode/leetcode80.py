class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:return n
        i,j = 0,0
        while i<n:
            prev = nums[i]
            count = 1
            while i+1<n and nums[i+1] == prev:
                if count<=2:
                    nums[j] = nums[i]
                    j += 1
                count += 1
                i += 1
            if count<=2:
                nums[j] = nums[i]
                i += 1
                j += 1
            else:
                i +=1
        return j

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:return n
        j = 0
        for num in nums:
            if j<2 or num != nums[j]:
                nums[j] = num
                j += 1
        return j
