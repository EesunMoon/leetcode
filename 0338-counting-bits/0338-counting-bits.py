class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n+1): # O(n)
            one = 0
            while i: # O(32) -> O(1)
                i = i & (i-1)
                one += 1
            res.append(one)
        return res
        