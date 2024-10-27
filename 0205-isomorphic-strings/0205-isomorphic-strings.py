from collections import Counter

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False

        
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))