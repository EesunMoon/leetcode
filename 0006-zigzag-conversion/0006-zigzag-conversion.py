class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # base case
        if numRows == 1:
            return s

        ans = ""
        for r in range(numRows):
            increment = 2 * (numRows-1)
            for i in range(r, len(s), increment):
                # first, last rows
                ans += s[i]
                # middle row
                if (r != 0 and r != numRows-1 and i+increment-2*r < len(s)):
                    ans += s[i+increment- 2*r]
        return ans

        
        