class Solution:
    def reverseWords(self, s: str) -> str:
        list_word = s.split(" ")
        res = ""
        def revers(word):
            n = len(word)
            s_list = list(word)
            res_word = ""
            for i in range(n):
                if i>=n-i-1:
                    break
                s_list[i],s_list[n-i-1] = s_list[n-i-1],s_list[i]
            for j in s_list:
                res_word = res_word+str(j)
            return res_word


        for i in list_word:
            res = res + revers(i)+" "
        s = res[:-1]
        return s



solution = Solution()
s  = "Let's take LeetCode contest"
result =  solution.reverseWords(s)


