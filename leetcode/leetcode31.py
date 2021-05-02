from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums,reverse = True)==nums:
            nums[:] = nums[::-1]
            return
        for i in range(len(nums)-1)[::-1]:
            if nums[i]<nums[i+1]:
                break
        for j in range(i+1,len(nums)):
            if j==len(nums)-1 or nums[j+1]<=nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                break
        nums[i+1:] = nums[i+1:][::-1]
        return
"""
具体地，我们这样描述该算法，对于长度为 nn 的排列 aa：

首先从后向前查找第一个顺序对 (i,i+1)(i,i+1)，满足 a[i] < a[i+1]a[i]<a[i+1]。这样「较小数」即为 a[i]a[i]。此时 [i+1,n)[i+1,n) 必然是下降序列。

如果找到了顺序对，那么在区间 [i+1,n)[i+1,n) 中从后向前查找第一个元素 jj 满足 a[i] < a[j]a[i]<a[j]。这样「较大数」即为 a[j]a[j]。

交换 a[i]a[i] 与 a[j]a[j]，此时可以证明区间 [i+1,n)[i+1,n) 必为降序。我们可以直接使用双指针反转区间 [i+1,n)[i+1,n) 使其变为升序，而无需对该区间进行排序。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
list = [3,2,1]
solution = Solution()
result = solution.nextPermutation(list)
print(list)
