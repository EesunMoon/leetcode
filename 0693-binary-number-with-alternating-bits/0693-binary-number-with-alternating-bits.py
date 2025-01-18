class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n, curr = divmod(n, 2) # convert to binary
        while n:
            if curr == n%2:
                return False
            n, curr = divmod(n, 2)
        return True