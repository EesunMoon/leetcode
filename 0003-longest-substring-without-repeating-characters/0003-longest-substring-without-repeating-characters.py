class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashset = set()
        res = 0 # length of the longest substring

        while r < len(s):
            # shrink window size
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            r += 1
            res = max(res, len(hashset))

        return res