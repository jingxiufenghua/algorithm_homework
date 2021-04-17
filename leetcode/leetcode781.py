# 781. 森林中的兔子
from typing import List
from  math import ceil
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if not answers: return 0
        n = len(answers)
        answers.sort()
        i,j = 0,0
        save_list = []
        while j<n:
            if answers[i] == answers[j]:
                j += 1
            else:
                save_list.append(answers[i:j])
                i = j
        if i<n:
            save_list.append(answers[i:])

        return sum(ceil(len(list)/(list[0]+1))*(list[0]+1) for list in save_list)
solution = Solution()
nums = [1,0,1,0,0]
result = solution.numRabbits(nums)
print(result)

