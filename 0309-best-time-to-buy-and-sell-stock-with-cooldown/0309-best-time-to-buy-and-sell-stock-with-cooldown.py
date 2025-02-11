class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp variables: (index, buy or not), states: maximum profit
        dp = {}

        def dfs(i, buying):
            # base case: out of the bound
            if i >= len(prices):
                return 0
            # base case: already in cache
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying) # in case of cooldown
            # 1) buying
            if buying:
                buy = dfs(i+1, not buying) - prices[i] # in case of buying
                dp[(i, buying)] = max(buy, cooldown) # store in cache
            # 2) selling
            else:
                sell = dfs(i+2, not buying) + prices[i] # in case of selling (with cooldown)
                dp[(i, buying)] = max(sell, cooldown) # store in cache
            
            return dp[(i, buying)]
        return dfs(0, True)