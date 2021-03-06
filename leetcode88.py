from typing import List
class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     if not nums1 or not nums2: return nums1 if nums1 else nums2
    #     n1, n2 = len(nums1), len(nums2)
    #     first, second = 0, 0
    #     stack = []
    #     while first < n1 - n2 and second < n2:
    #         while first < n1 - n2 and second < n2 and nums1[first] > nums2[second]:
    #             stack.append(nums2[second])
    #             second += 1
    #         while first < n1 - n2 and second < n2 and nums1[first] <= nums2[second]:
    #             stack.append(nums1[first])
    #             first += 1
    #     res = nums1[first:n1 - n2] if first < n1 - n2 else nums2[second:]
    #     stack = stack + res
    #     print(stack)
    #     for i in range(len(stack)):
    #         nums1[i] = stack[i]
    #     return nums1

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of nums1.
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]


solution = Solution()
nums1 = [2,0]
m = 2
nums2 = [1]
n = 1
result = solution.merge(nums1,m,nums2,n)
print(result)






