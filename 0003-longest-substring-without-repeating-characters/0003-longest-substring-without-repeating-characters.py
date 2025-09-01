class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hashset = set()
        l = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, r - l + 1)
        return res