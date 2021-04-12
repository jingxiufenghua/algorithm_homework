from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        temp_list,res = list(s),[]
        def dfs(x):
            if x == len(temp_list)-1:
                res.append(''.join(temp_list))
                return
            dic = set()
            for i in range(x,len(temp_list)):
                if temp_list[i] in dic:continue
                dic.add(temp_list[i])
                temp_list[i],temp_list[x] = temp_list[x],temp_list[i]
                dfs(x+1)
                temp_list[x],temp_list[i] = temp_list[i],temp_list[x]
        dfs(0)
        return res

solution = Solution()
string = "aac"
result = solution.permutation(string)
print(result)
