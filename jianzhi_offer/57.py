# 剑指 Offer 57 - II. 和为s的连续正数序列
from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target==1 : return []
        nums_list = [i for i in range(1,target)]
        i,limit = 0,int((target-1)/2)
        res = []
        while i<=limit:
            temp = 0
            for j in range(i,target-1):
                if temp + nums_list[j] <target:
                    temp += nums_list[j]
                elif temp + nums_list[j] == target:
                    res.append(nums_list[i:j+1])
                else:
                    break
            i += 1
        return res
     # def findContinuousSequence(self, target: int) -> List[List[int]]:
        #     i = 1 # 滑动窗口的左边界
        #     j = 1 # 滑动窗口的右边界
        #     sum = 0 # 滑动窗口中数字的和
        #     res = []

        #     while i <= target // 2:
        #         if sum < target:
        #             # 右边界向右移动
        #             sum += j
        #             j += 1
        #         elif sum > target:
        #             # 左边界向右移动
        #             sum -= i
        #             i += 1
        #         else:
        #             # 记录结果
        #             arr = list(range(i, j))
        #             res.append(arr)
        #             # 左边界向右移动
        #             sum -= i
        #             i += 1

        #     return res

solution = Solution()
nums = 9
result = solution.findContinuousSequence(nums)
print(result)






