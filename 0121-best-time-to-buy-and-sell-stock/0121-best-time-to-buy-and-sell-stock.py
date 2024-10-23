class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # base case
        if not prices:
            return 0
        
        max_profits= 0
        min_purchase = prices[0]

        for i in range(1, len(prices)):
            max_profits = max(max_profits, prices[i]-min_purchase)
            min_purchase = min(min_purchase, prices[i])
        return max_profits
        