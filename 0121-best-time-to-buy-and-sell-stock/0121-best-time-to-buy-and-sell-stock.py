class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while r < len(prices):
            while r < len(prices) and prices[l] < prices[r]:
                res = max(res, prices[r]-prices[l])
                r +=1
            l = r
            r += 1
        return res