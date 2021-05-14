from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        res_dict = {}
        for i in range(n):
            while stack and T[stack[-1]]<T[i]:
                res_dict[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return [res_dict.get(x,0) for x in range(n)]
solution = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
result = solution.dailyTemperatures(temperatures)
print(result)


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:return []
        stack = []
        n = len(T)
        res = [0]*n
        for i in range(n):
            while stack and T[stack[-1]]<T[i]:
                cur = stack.pop()
                res[cur] = i-cur
            stack.append(i)
        return res