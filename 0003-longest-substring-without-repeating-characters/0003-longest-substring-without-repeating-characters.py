class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        subSet = set()
        l = 0
        for c in s:
            while subSet and c in subSet:
                subSet.remove(s[l])
                l+=1
            subSet.add(c)
            res = max(res, len(subSet))
        return res