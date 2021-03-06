from typing import List
class Solution:
    # 回溯法
    def grayCode(self, n: int) -> List[int]:
        trace = []
        graycode = []
        def decode(gray_code):
            """二进制转十进制"""
            decimal = 0
            for bit in gray_code:
                decimal = decimal * 2 + bit
            return decimal
        def backtrack(choice_list=(0,1)):
            if len(trace)==n:
                graycode.append(trace[:])
                return
            trace.append(choice_list[0])
            backtrack((0,1))
            trace.pop()
            trace.append(choice_list[1])
            backtrack((1,0))
            trace.pop()
        backtrack()
        return [decode(code) for code in graycode]





solution = Solution()
n = 3
result = solution.grayCode(3)
print(result)
