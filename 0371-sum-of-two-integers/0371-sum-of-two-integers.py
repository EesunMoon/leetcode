class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # carry: AND -> one left shift
        # digit sum: XOR
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask # digit => sum result
            b = carry & mask # carry

        return a if a <= max_int else ~(a^mask) # apply appropriate range