# # 34. 在排序数组中查找元素的第一个和最后一个位置
from  typing import List
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums:return [-1,-1]
#         left,right = 0,len(nums)-1
#         res = []
#         while left<=right:
#             mid = (left+right)//2
#             if target<nums[mid]:
#                 right = mid - 1
#             elif target>nums[mid]:
#                 left = mid + 1
#             elif target==nums[mid]:
#                 for i in range(mid,-1,-1):
#                     if nums[i] == target:
#                         res.append(i)
#                     else:
#                         break
#                 for j in range(mid,right+1):
#                     if nums[j]==target:
#                         res.append(j)
#                     else:
#                         break
#                 return [min(res),max(res)]
#         return [-1,-1]
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # 二分查找，搜索左右边界
#         if not nums:
#             return [-1, -1]
#         return [self._search_left(nums, target), self._search_right(nums, target)]
#
#     def _search_left(self, nums, target):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] > target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] == target:
#                 right = mid - 1                         # 改动这里，使搜索区间向左侧收缩
#         if left >= len(nums) or nums[left] != target:   # 判断索引越界情况
#             return -1
#         return left
#
#     def _search_right(self, nums, target):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] > target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] == target:
#                 left = mid + 1                          # 改动这里，使搜索区间向右侧收缩
#         if right < 0 or nums[right] != target:          # 判断索引越界情况
#             return -1
#         return right
#
# solution = Solution()
# nums = [2,2]
# result = solution.searchRange(nums,2)
# print(result)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bi_search(nums,start,end,target):
            while start<=end:
                mid = start + (end - start) // 2
                if nums[mid]<target:
                    start = mid + 1
                elif nums[mid] == target:
                    return mid
                else:
                    end = mid-1
            return -1
        n = len(nums)
        target_index = bi_search(nums,0,n-1,target)
        res = [target_index,target_index]
        if target_index<0: return res
        for i in range(target_index):
            left_index = bi_search(nums,0,target_index-i,target)
            if left_index>= 0:
                res[0] = left_index
            else:
                break
        for i in range(n-target_index):
            right_index = bi_search(nums,target_index+i,n-1,target)
            if right_index>=0:
                res[1] = right_index
            else:
                break
        return res


solution = Solution()
nums = [1,1,1,1]
target = 1
result = solution.searchRange(nums,target)
print(result)

