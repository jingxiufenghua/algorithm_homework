class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        stack = []
        for i in range(n-1,-1,-1):
            if stack and s[i]==" ":
                break
            if s[i]!=" ":
                stack.append(s[i])
        return len(stack)
solution = Solution()
s = "Hello World"
# s = "a  "
result = solution.lengthOfLastWord(s)
print(result)
