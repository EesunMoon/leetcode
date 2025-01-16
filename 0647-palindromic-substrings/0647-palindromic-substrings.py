class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def isPalindrome(l, r):
            res = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        
        total = 0
        for i in range(len(s)):
            total += isPalindrome(i,i)
            total += isPalindrome(i,i+1)
        return total