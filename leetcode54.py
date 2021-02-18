from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result: List[int] = []

        # def left_right_append(matrix,rows,cols_list):
        #     nonlocal result
        #     for i in cols_list:
        #         result.append(matrix[rows][i])
        #     return rows,i
        #
        # def up_down_append(matrix,rows_list,cols):
        #     for i in rows_list:
        #         result.append(matrix[i][cols])
        #     return cols,i
        # def right_left_append(matrix,rows,cols_list):
        #     for i in cols_list:
        #         result.append(matrix[rows][i])
        #     return rows,i
        # def down_up_append(matrix,rows_list,cols):
        #     for i in rows_list:
        #         result.append(matrix[i][cols])
        #     return cols,i
        #
        # rows,cols = 0,0
        #
        # cols_list = list(range(cols,len(matrix[0])))
        # rows,lable = left_right_append(matrix,rows,cols_list)
        #
        # rows_list = list(range(rows + 1, len(matrix)))
        # cols,lable = up_down_append(matrix,rows_list,lable)
        #
        # print(cols,lable)
        #
        # cols_list = reversed(list(range(cols)))
        # rows,lable = right_left_append(matrix,lable,cols_list)
        # print(cols, lable)
        #
        # rows_list = range(len(matrix)-1,rows-1)
        # down_up_append(matrix,rows_list,lable)

        row = len(matrix)
        col = len(matrix[0])
        if row==0 or col==0:
            return []
        res = matrix[0]
        if row>1:
            for i in range(1,row):
                res.append(matrix[i][col-1])
            for j in range(col-2,-1,-1):
                res.append(matrix[row-1][j])
            if col>1:
                for i in range(row-2,0,-1):
                    res.append(matrix[i][0])
        M = []
        for k in range(1,row-1):
            t = matrix[k][1:-1]
            M.append(t)
        return res+self.spiralOrder(M)




solution = Solution()
solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
