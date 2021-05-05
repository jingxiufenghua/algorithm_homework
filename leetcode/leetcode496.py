from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1,len2 = len(nums1),len(nums2)
        res_list = []
        for i in range(len1):
            local = nums2.index(nums1[i])
            res = -1
            while local<len2:
                if nums1[i]<nums2[local]:
                    res = local
                    break
                else:
                    local+=1
            if res<0:
                res_list.append(res)
            else:
                res_list.append(nums2[res])
        return res_list
# 单调递减栈
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack,result_dict= [],{}
        len1,len2 = len(nums1),len(nums2)
        for i in range(len2):
            while stack and stack[-1]<nums2[i]:
                result_dict[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        result_dict[nums2[len2-1]] = -1  # 最后一位后面没有数，所以后面没有比他更大的数据，直接设置为-1
        return [result_dict.get(x,-1) for x in nums1]


solution = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
# result = solution.nextGreaterElement(nums1,nums2)
# nums1 = [2,4]
# nums2 = [1,2,3,4]
result = solution.nextGreaterElement1(nums1,nums2)
print(result)
