class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        maxfreq = 0
        res = 0

        l = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxfreq = max(maxfreq, hashmap[s[r]])

            # window size - #.max frequent num = #.variable to change
            # shrinkage condition
            while (r-l+1) - maxfreq > k:
                hashmap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            
        return res
