class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        subSet = deque()
        for c in s:
            while subSet and c in subSet:
                subSet.popleft()
            subSet.append(c)
            res = max(res, len(subSet))
        return res