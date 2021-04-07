class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers: return  -1
        n = len(numbers)
        left,right = 0,n-1
        while left<right:
            mid = (left + right)//2
            if numbers[mid]>numbers[right]:
                left = mid + 1
            elif numbers[right]==numbers[mid]:
                right -=1
            else:
                right = mid
        return numbers[left]
