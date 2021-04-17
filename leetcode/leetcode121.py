from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:return 0
        n = len(prices)
        # max_pro = 0
        # diff = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         diff =max(diff, prices[j] - prices[i])
        # return diff

        minprice = int(1e9)
        max_pro = 0
        for price in prices:
            max_pro = max(price-minprice,max_pro)
            minprice = min(minprice,price)
        return max_pro




