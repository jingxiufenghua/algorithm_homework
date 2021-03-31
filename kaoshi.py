# [1,2,3,4,5,6]

# [4,5,6,1,2,3]
#didi 面试题，二分法
#自己当时主要考虑使用双指针，但是由于数组其实是有序的所以二分查找才更能利用数据的特性

from typing import List
class Solution:
    # 二分法
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        if not numbers:return -1
        left,right = 0,n-1
        while left<right:
            mid = left + (right-left)//2
            if numbers[mid]>numbers[right]:
                left = mid + 1
            elif numbers[mid]<numbers[right]:
                right = mid
            else:
                right-=1
        return numbers[left]

solution = Solution()
nums = [1,2,1]
result = solution.minArray(nums)

print(result)









