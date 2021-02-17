from typing import List
class Solution:
    #1716
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        res_day = n%7
        first_part = 28*weeks + (weeks-1)*weeks//2*7
        first_part = max(0,first_part)
        for i in range(1,res_day+1):
            first_part = first_part + (i+weeks)
        return first_part

    #1717
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        def count(s, target, score):
            nonlocal res
            n = len(s)
            stack = []
            for i in range(n):
                if stack and stack[-1] + s[i] == target:
                    print(stack.pop())
                    res += score
                else:
                    stack.append(s[i])
            return stack
        if x > y:
            stack = count(s, "ab", x)
            count(stack, "ba", y)
        else:
            stack = count(s, "ba", y)
            count(stack, "ab", x)
        return res



        #1718
    def constructDistancedSequence(self, n: int) -> List[int]:
        pass


    #1719




solution = Solution()
result = solution.totalMoney(26)
result2 = solution.maximumGain("cdbcbbaaabab",4,5)
print(result2)



