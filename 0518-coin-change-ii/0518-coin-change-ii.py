class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = {}
        def dfs(i, total):
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i,total)] = dfs(i, total + coins[i]) + dfs(i+1, total)
            return dp[(i, total)]
        
        return dfs(0,0)