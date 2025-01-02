class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            # base case
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = helper(x*x, n//2)
            return x*res if n%2 else res
        
        res = helper(x, abs(n))
        return res if n>=0 else 1/res
        