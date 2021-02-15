import collections
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # cache = collections.Counter(words)
        if len(words)==0:return []
        unilen = len(words[0])
        res,sets=[],{}
        for word in words:
            sets[word] = sets.setdefault(word,0) + 1
        for i in range(unilen):
            count,start,match_set = len(words),i,{}
            for j in range(i,len(s),unilen):
                substr = s[j:j+unilen]
                if substr in sets:
                    match_set[substr] = match_set.setdefault(substr,0) + 1
                    count-=1
                    while(match_set[substr]>sets[substr]):
                        remove = s[start:start+unilen]
                        start += unilen
                        match_set[remove] -=1
                        count+=1
                    if count==0:
                        res.append(start)
                else:
                    count,start,match_set=len(words),j+unilen,{}
        return res
solution = Solution()
str="barfoothefoobarman"
str2 = ["foo","bar"]
result = solution.findSubstring(str,str2)
print(result)
