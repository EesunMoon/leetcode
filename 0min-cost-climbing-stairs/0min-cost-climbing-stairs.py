class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def dp(idx):
            # base case
            if idx == 0 or idx == 1:
                return 0
            
            if idx not in cache:
                cache[idx] = min(dp(idx-1)+cost[idx-1], dp(idx-2)+cost[idx-2])
            return cache[idx]
        

        cache = {}
        return dp(len(cost))