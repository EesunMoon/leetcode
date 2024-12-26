class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        res, reslen = [-1, -1], float("inf")
        need, have = len(countT), 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                # update
                if (r-l+1) < reslen:
                    res, reslen = [l, r], (r-l+1)

                # shrink
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1

        l, r = res    
        return s[l:r+1] if reslen != float("inf") else ""