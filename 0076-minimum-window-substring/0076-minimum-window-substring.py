class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # TC O(n) SC O(m)
        # n: the length of the string s, 
        # m: the total number of unique characters in the strings t and s

        if t == "":
            return ""

        hasht, window = {}, {} # c: freq
        for c in t:
            hasht[c] = 1 + hasht.get(c, 0)
        
        need, have = len(hasht), 0
        res, reslen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in hasht and window[c] == hasht[c]:
                have += 1
            
            while have == need:
                # update result
                if (r-l+1) < reslen:
                    res = [l, r]
                    reslen = (r-l+1)
                
                # shrink
                window[s[l]] -= 1
                if s[l] in hasht and window[s[l]] < hasht[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""