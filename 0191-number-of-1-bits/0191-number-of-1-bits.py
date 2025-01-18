class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 0
        
        while n:
            n = n & (n-1)
            one += 1
        
        return one