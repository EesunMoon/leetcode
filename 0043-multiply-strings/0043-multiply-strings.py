class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if "0" in [num1, num2]:
            return "0"

        res = [0]*(len(num1)+len(num2))
        num1, num2 = num1[::-1], num2[::-1] # reverse

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])

                res[i1+i2] += digit
                res[i1+i2+1] += (res[i1+i2]//10) # carry
                res[i1+i2] %= 10

        # reverse, edge case: 0100 - eliminate zero
        res, begin = res[::-1], 0
        while begin<len(res) and res[begin] == 0:
            begin += 1
        
        res = map(str, res[begin:])
        return "".join(res)