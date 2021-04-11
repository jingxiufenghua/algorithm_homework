from typing import List
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first=0):
#             if first == n:
#                 return res.append(nums[:])
#             for i in range(first,n):
#                 nums[i],nums[first] = nums[first],nums[i]
#                 backtrack(first+1)
#                 nums[first],nums[i] = nums[i],nums[first]
#         res = []
#         n = len(nums)
#         backtrack()
#         # res = list(set([i for i in res]))  一维的list去重可以用set(list)，但是二维的list转set就会报错 unhashable type: ‘list’
#         """
#         原因是set传进来的是不可哈希的变量
#         Python中那么哪些是可哈希元素？哪些是不可哈希元素？
#         可哈希的元素有：int、float、str、tuple
#         不可哈希的元素有：list、set、dict
#         为什么 list 是不可哈希的，而 tuple 是可哈希的
#         （1）因为 list 是可变的在它的生命期内，你可以在任意时间改变其内的元素值。
#         （2）所谓元素可不可哈希，意味着是否使用 hash 进行索引
#         （3）list 不使用 hash 进行元素的索引，自然它对存储的元素有可哈希的要求；而 set 使用 hash 值进行索引
#         """
#         res = list(set([tuple(t) for t in res]))
#         res = [list(v) for v in res]
#         return res
#
# solution = Solution()
# nums = [1,2,3]
# result = solution.permuteUnique(nums)
# print(result)
# from typing import List


# class Solution:
#
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#
#         def dfs(nums, size, depth, path, used, res):
#             if depth == size:
#                 res.append(path.copy())
#                 return
#             for i in range(size):
#                 if not used[i]:
#
#                     if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:  # 剪枝操作
#                         continue
#
#                     used[i] = True
#                     path.append(nums[i])
#                     dfs(nums, size, depth + 1, path, used, res)
#                     used[i] = False
#                     path.pop()
#
#         size = len(nums)
#         if size == 0:
#             return []
#
#         nums.sort()
#
#         used = [False] * len(nums)
#         res = []
#         dfs(nums, size, 0, [], used, res)
#         return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n =len(nums)-1
        res = []
        def dfs(x):
            if x == len(nums)-1:
                res.append(nums)
                return
            dic = set()
            for i in range(x,len(nums)):
                if nums[i] in dic:continue
                dic.add(nums[i])
                nums[i],nums[x] = nums[x],nums[i]
                dfs(x+1)
                nums[i],nums[x] = nums[x],nums[i]
        dfs(0)
        return res
solution = Solution()
nums = [1,1,2]
result = solution.permuteUnique(nums)
print(result)

