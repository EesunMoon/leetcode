class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def SumOfSquareOfDigits(num):
            res = 0
            while num:
                res += ((num%10)**2)
                num = num//10
            return res
        
        cycle = set()
        while n != 1:
            n = SumOfSquareOfDigits(n)
            if n == 1:
                return True
            
            if n in cycle:
                return False
            cycle.add(n)
        
        return True
        