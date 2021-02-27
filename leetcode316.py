class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack,last_loccal= [],{}
        res = ''
        for i in range(n):
            last_loccal[s[i]] = i
        for i in range(n):
            if s[i] in stack:
                continue
            while stack and stack[-1]>s[i] and last_loccal[stack[-1]]>i :
                stack.pop()
            stack.append(s[i])
        for j in stack:
            res = res+j
        return res

solution = Solution()
# s = "bcabc"
s = "cbacdcbc"
# s = "abacb"
result = solution.removeDuplicateLetters(s)
print(result)

