class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        stack = []
        up_flag = 0
        res = ""
        num1 = list(num1)
        num2 = list(num2)
        while num1 or num2:
            first = int(num1.pop()) if num1 else 0
            second = int(num2.pop()) if num2 else 0
            cur_sum = first + second + up_flag
            stack.append(cur_sum%10)
            up_flag = cur_sum//10
        if up_flag>0:
            stack.append(up_flag)
        for i in stack[::-1]:
            res = res + str(i)
        return  res


solution = Solution()
num1 = "123"
num2 = "456"
result = solution.addStrings(num1, num2)
print(result)

