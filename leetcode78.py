from typing import List
class Solution:
    # 迭代法
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     res = [[]]
    #     for i in range(n):
    #         len_res = len(res)
    #         for j in range(len_res):
    #             temp = res[j].copy()
    #             temp.append(nums[i])
    #             res.append(temp)
    #     return res
    # 迭代法
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res




solution = Solution()
nums = [1,2,3]
result = solution.subsets(nums)
print(result)



