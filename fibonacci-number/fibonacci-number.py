class Solution(object):
    def __init__(self):
        self.cache = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in self.cache:
            return self.cache[n]
        
        if n < 2:
            result = n
        else:
            result = self.fib(n-1) + self.fib(n-2)

        self.cache[n] = result
        return result


        # without memoization
        """
        if n < 2:
            return n
        
        return self.fib(n-1) + self.fib(n-2)
        """
        