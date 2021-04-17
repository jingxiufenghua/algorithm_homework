class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        stack,local_list = [],{}
        res = ""
        for i in range(n):
            local_list[s[i]] = i
        for i in range(n):
            if s[i] in stack:
                continue
            while stack and stack[-1]>s[i] and local_list[stack[-1]]>i:
                stack.pop()
            stack.append(s[i])
        for i in stack:
            res = res + stack[i]
        return res