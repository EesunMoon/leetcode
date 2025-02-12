class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {} # char: freq
        
        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
        
        for i, c in enumerate(s):
            if hashmap[c] == 1:
                return i
        return -1