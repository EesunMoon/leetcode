class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # base case
        if len(s1) > len(s2):
            return False

        # make hashmap
        h1, h2 = {}, {}
        for i in range(len(s1)):
            h1[s1[i]] = 1 + h1.get(s1[i], 0)
            h2[s2[i]] = 1 + h2.get(s2[i], 0)
        
        if h1 == h2:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            h2[s2[l]] -= 1
            if h2[s2[l]] == 0:
                del h2[s2[l]]
            l += 1
            h2[s2[r]] = 1 + h2.get(s2[r], 0)

            if h1 == h2:
                return True
        return False

