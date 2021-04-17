# 剑指 Offer 58 - II. 左旋转字符串

# class Solution:
#     def reverseLeftWords(self, s: str, n: int) -> str:
#         if not s :return s
#         alph = list(s)
#         save = []
#         for i in range(n):
#             save.append(alph[0])
#             del alph[0]
#         new_list = alph + save
#         return "".join(new_list)


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if not s :return s
        return "".join(s[n:] + s[:n])

solution = Solution()
s = "lrloseumgh"
result = solution.reverseLeftWords(s,2)
print(result)
