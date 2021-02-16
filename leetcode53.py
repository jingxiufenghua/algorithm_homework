from typing import List
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         """
#
#         :param nums:
#         :return:
#         """
#         if not nums:return 0
#
#         def divide_two_part(nums:List[int]):
#             pivot = len(nums)//2
#             first_part = nums[:pivot]
#             second_part = nums[pivot:]
#             return first_part,second_part
#
#         def sub_sum(nums:List[int]):
#             if len(nums)<=2:
#                 return sum(nums)
#             first_part,second_part = divide_two_part(nums)
#             first_part_sum,second_part_sum = sub_sum(first_part),sub_sum(second_part)

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

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = sub_sum(nums)
print(result)


