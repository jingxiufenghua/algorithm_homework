class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []

        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack

        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"

        #     if num[i]!= "0" and n-i-1>=k-count and count<k:
        #         stack.append(num[i])
        #     else:
        #         count+=1
        #     if count>=k:
        #         for j in range(i,n):
        #             stack.append(num[j])
        #         for i in stack:
        #             res = res + i
        #         return res
        # return "0"

solution = Solution()
num = "1432219"
num1 = "10200"
num2 = "112"
result = solution.removeKdigits(num2,1)
print(result)
