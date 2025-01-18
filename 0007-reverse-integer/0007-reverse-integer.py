class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX, MIN = 2**31-1, -(2**31)
        res = 0

        isNegative = True if x < 0 else False
        
        x = abs(x)
        while x:
            digit = x % 10
            x = x // 10
            res = (res*10)+digit

        if isNegative:
            res = -res

        return res if MIN <= res <= MAX else 0