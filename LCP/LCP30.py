import heapq

class Solution:
    def magicTower(self, nums):
        if sum(nums)<0:
            return -1
        hurts = []
        blood = 0
        counts = 0
        heapq.heapify(hurts)
        for i in nums:
            blood += i
            if i<0:heapq.heappush(hurts,i)
            if blood<0:
                counts += 1
                blood -= heapq.heappop(hurts)
        return counts