class Solution(object):
    def climb_stairs(self, i, n, cache):
        if i > n:
            return 0
        if i == n:
            return 1
        if cache[i] > 0:
            return cache[i]
        
        cache[i] = self.climb_stairs(i+1, n, cache) + self.climb_stairs(i+2, n, cache)
        
        return cache[i]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [0] * (n+1)
        return self.climb_stairs(0, n, cache)
        
        