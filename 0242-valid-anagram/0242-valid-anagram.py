class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        
        countS, countT = {}, {}
        for idx in range(len(s)):
            countS[s[idx]] = countS.get(s[idx], 0) + 1
            countT[t[idx]] = countT.get(t[idx], 0) + 1
        
        return countS == countT