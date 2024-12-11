class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        ## dynamic programming approach ##
        # base case
        if not prices:
            return 0
        
        max_profits= 0
        min_purchase = prices[0]

        for i in range(1, len(prices)):
            max_profits = max(max_profits, prices[i]-min_purchase)
            min_purchase = min(min_purchase, prices[i])
        return max_profits
        """

        ## two pointer ##
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+= 1
        return maxP
        