import collections
class Solution:
    def isUnique(self, astr: str) -> bool:
        res = list(astr)
        hash_map = collections.Counter(res)
        for k,v in hash_map.items():
            if v>1:
                return False
        return True

# class Solution:
#     def isUnique(self, astr: str) -> bool:
#         return len(astr) == len(set(astr))
# 
# 作者：biemx
# 链接：https: // leetcode - cn.com / problems / is -unique - lcci / solution / tou - lan - ye - neng - ji - bai - 100 - by - biemx - 4j
# dp /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

solution = Solution()
s = "leetcode"
result = solution.isUnique(s)
print(result)

