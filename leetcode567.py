import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        N = len(s2)
        left = 0
        right = len(s1) - 1
        counter2 = collections.Counter(s2[0:right])
        while right<N:
            counter2[s2[right]] += 1
            if counter1 ==counter2:
                return True
            counter2[s2[left]]-=1
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            left+=1
            right+=1
        return False

solution = Solution()
first_str = "abcda"
second_str = "abcdaa"
result = solution.checkInclusion(first_str,second_str)
print(result)
