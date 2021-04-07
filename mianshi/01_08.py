# 面试题 01.08. 零矩阵
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)  # 行
        col = len(matrix[0])  # 列
        alphabet = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    alphabet.append((i, j))

        for k, v in alphabet:
            for j in range(col):
                matrix[k][j] = 0
            for i in range(row):
                matrix[i][v] = 0

        return matrix

作者：sheriff - 4
Xr297jhAo
链接：https: // leetcode - cn.com / problems / zero - matrix - lcci / solution / tong - guo - yuan - zu - ji - lu - mei - ci - huo - qu - dao - m39l /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
