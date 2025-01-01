class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = ""
        for num in digits:
            ans += str(num)
        digits = list(str(int(ans)+1))

        for i in range(len(digits)):
            digits[i] = int(digits[i])
        return digits