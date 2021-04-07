from typing import List
class Solution:
    # def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    #     if not matrix:return False
    #     row,col = len(matrix),len(matrix[0])
    #     for i in range(row):
    #         for j in range(col):
    #             if matrix[i][j] == target:
    #                 return True
    #     return False

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i,j = len(matrix)-1,0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]>target: i-=1
            elif matrix[i][j]<target:j+=1
            else: return True
        return False



solution = Solution()
nums = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
result = solution.findNumberIn2DArray(nums,20)
print(result)


















        # for i in range(row):
        #     if matrix[i][0]<=target and matrix[i][-1]>=target:
        #         left,right = 0,col-1
        #         while left<=right:
        #             mid = (left+right)//2
        #             if matrix[i][mid]>target:
        #                 right = mid
        #             elif matrix[i][mid]<target:
        #                 left = mid + 1
        #             else:
        #                 return True


