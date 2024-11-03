class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        def dp(idx):
            if idx == 0:
                return 0
            elif idx ==1:
                return 1
            elif idx == 2:
                return 1
            
            if idx not in cache:
                cache[idx] = dp(idx-1) + dp(idx-2) + dp(idx-3)
            return cache[idx]
        
        cache={}
        return dp(n)
        