from typing import List
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows,cols = len(nums),len(nums[0])
        if rows==0 or cols==0 or rows*cols!=r*c:
            return nums
        res = [[0]*c for _ in range(r)]
        temp = []
        for i in range(rows):
            for j in range(cols):
                temp.append(nums[i][j])
        temp = temp[::-1]
        for x in range(r):
            for y in range(c):
                res[x][y] = temp.pop()
        return res

solution = Solution()
nums = [[1,2],[3,4]]
res = solution.matrixReshape(nums,1,4)
print(res)

