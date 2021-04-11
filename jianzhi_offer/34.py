# 34. 在排序数组中查找元素的第一个和最后一个位置
from  typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:return [-1,-1]
        left,right = 0,len(nums)-1
        res = []
        while left<=right:
            mid = (left+right)//2
            if target<nums[mid]:
                right = mid - 1
            elif target>nums[mid]:
                left = mid + 1
            elif target==nums[mid]:
                for i in range(mid,-1,-1):
                    if nums[i] == target:
                        res.append(i)
                    else:
                        break
                for j in range(mid,right+1):
                    if nums[j]==target:
                        res.append(j)
                    else:
                        break
                return [min(res),max(res)]
        return [-1,-1]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找，搜索左右边界
        if not nums:
            return [-1, -1]
        return [self._search_left(nums, target), self._search_right(nums, target)]

    def _search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1                         # 改动这里，使搜索区间向左侧收缩
        if left >= len(nums) or nums[left] != target:   # 判断索引越界情况
            return -1
        return left

    def _search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1                          # 改动这里，使搜索区间向右侧收缩
        if right < 0 or nums[right] != target:          # 判断索引越界情况
            return -1
        return right

作者：jue-qiang-zha-zha
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/34-zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-irqc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

solution = Solution()
nums = [2,2]
result = solution.searchRange(nums,2)
print(result)




