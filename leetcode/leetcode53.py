from typing import List
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         """
#
#         :param nums:
#         :return:
#         """


def divide_two_part(nums:List[int]):
    pivot = len(nums)//2
    first_part = nums[:pivot]
    second_part = nums[pivot:]
    return first_part,second_part

def sub_sum(nums:List[int],result=-2**31):
    if len(nums)<2:
        return sum(nums),nums
    first_part,second_part = divide_two_part(nums)
    first_part_sum,first_result_list= sub_sum(first_part,result)
    second_part_sum,second_result_list= sub_sum(second_part,result)
    two_part_list = first_part + second_part
    two_part_sum = sum(two_part_list)
    max_sum = max(first_part_sum,second_part_sum,two_part_sum)
    if max_sum == two_part_sum and result<two_part_sum:
        result = two_part_sum
        result_list = two_part_list
    elif max_sum ==first_part_sum and result<first_part_sum:
        result = first_part_sum
        result_list = first_result_list
    elif max_sum==second_part_sum and result<second_part_sum:
        result = second_part_sum
        result_list = second_result_list
    else:
        result_list = []
    return  result,result_list


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if max(nums)<0 : return max(nums)
        max_pro = 0
        sub_pro = 0
        for price in nums:
            sub_pro = max(sub_pro + price,0)
            max_pro = max(sub_pro,max_pro)
        return max_pro


nums = [-2,1,-3,4,-1,2,1,-5,4]
result = sub_sum(nums)
print(result)
print(123>>1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if max(nums)<0: return max(nums)
        sub_sum,max_sum = 0,0
        for i in range(n):
            sub_sum = max(0,sub_sum+nums[i])
            max_sum = max(max_sum,sub_sum)
        return max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if max(nums)<0: return max(nums)
        sub_sum,max_sum = 0,0
        for i in range(n):
            sub_sum = max(0,sub_sum+nums[i])
            max_sum = max(max_sum,sub_sum)
        return max_sum
