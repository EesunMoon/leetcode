class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 0
        
        while n:
            n, curr = divmod(n, 2)
            if curr == 1:
                one += 1
        
        return one