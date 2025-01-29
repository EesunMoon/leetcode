class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = ""

        def isPal(l, r):
            length = 0
            pair = None
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                else:
                    length = r-l+1
                    pair = [l, r]
                l -= 1
                r += 1
            return length, pair

        for center in range(len(s)):
            # odd number
            length1, pair1 = isPal(center, center)
            if maxLen < length1:
                maxLen = length1
                res = s[pair1[0]:pair1[1]+1]

            # even number
            length2, pair2 = isPal(center, center + 1)
            if maxLen < length2:
                maxLen = length2
                res = s[pair2[0]:pair2[1]+1]
            
        return res  
