class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # state: max_profit
        dp = {} # [cache] key: (i, buying), value: max_profit

        def dfs(i, buying):
            # base case: out of bound
            if i >= len(prices):
                return 0
            # base case: already compute
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if buying:
                # buying
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(cooldown, buy)
            else:
                # selling: we must have cooldown for next day
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(cooldown, sell)
            return dp[(i, buying)]
        return dfs(0, True)