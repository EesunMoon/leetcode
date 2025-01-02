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

        ## two pointer ## => S O(1) T O(N)
        # initialize
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            # case1) increase
            if prices[l] < prices[r]:
                maxProfit=max(maxProfit, prices[r]-prices[l])
            # case2) green
            else:
                l = r
            r+=1

        return maxProfit