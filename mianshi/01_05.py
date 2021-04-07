import collections
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n1 = len(first)
        n2 = len(second)
        if abs(n1-n2)>=2: return False
        res = 0
        i,j = 0,0
        while i<n1 and j<n2:
            if first[i] != second[j]:
                res += 1
                if res>2:
                    return False
                if i+1<n1 and first[i+1] == second[j]:
                    i = i + 1
                    continue
                elif j+1<n2 and first[i] == second[j+1]:
                    j = j + 1
                    continue
            i+=1
            j+=1
        if i<n1 or j<n2:
            res = res+1
        return res<2

solution = Solution()
first = "ab"
second = "bc"
result = solution.oneEditAway(first,second)
print(result)





