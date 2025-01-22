class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = ""

        for i in range(len(s)):
            # i: consider as center

            # odd length
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                length = (r-l)+1
                if length > maxLen:
                    maxLen = length
                    res = s[l:l+length]
                l -= 1
                r += 1
            
            # even length
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                length = (r-l)+1
                if length > maxLen:
                    maxLen = length
                    res = s[l:l+length]
                l -= 1
                r += 1


        return res