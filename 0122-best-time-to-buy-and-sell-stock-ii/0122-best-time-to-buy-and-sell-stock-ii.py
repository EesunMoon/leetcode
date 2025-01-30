class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy
        res = 0
        for i in range(1, len(prices)):
            # if valley
            if prices[i] > prices[i-1]:
               res += (prices[i]-prices[i-1]) 
        return res